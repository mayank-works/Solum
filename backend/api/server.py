"""
Solum backend API server.

Wraps the simulation core (solum.simulation) in a long-running FastAPI
process: a background task advances the world in real time (DESIGN.md
§16 "the world should continue running even when nobody is viewing
it"), and WebSocket clients receive the resulting event deltas
(DESIGN.md §20) as they happen. REST endpoints provide a way to fetch
the current state on demand (e.g. for an initial page load before the
WebSocket connects).

Run with:
    uvicorn solum.api.server:app --reload --port 8000

Configuration (env vars):
    SOLUM_TICK_INTERVAL   seconds of real time per simulated hour (default 2.0)
    SOLUM_SEED            random seed for reproducibility (default: unset/random)
    SOLUM_CORS_ORIGINS    comma-separated allowed origins (default: localhost dev ports)
"""

from __future__ import annotations

import asyncio
import logging
import os
from contextlib import asynccontextmanager

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

from solum.api.connection_manager import ConnectionManager
from solum.api.schemas import npc_to_dict, world_event_to_dict, world_snapshot
from solum.simulation.world import World

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("solum.api")

TICK_INTERVAL_SECONDS = float(os.environ.get("SOLUM_TICK_INTERVAL", "2.0"))
SEED = os.environ.get("SOLUM_SEED")
CORS_ORIGINS = os.environ.get(
    "SOLUM_CORS_ORIGINS",
    "http://localhost:3000,http://127.0.0.1:3000,http://localhost:5173,http://127.0.0.1:5173",
).split(",")

manager = ConnectionManager()


class SimulationRunner:
    """Owns the World instance and the background real-time tick loop."""

    def __init__(self, seed: int | None = None) -> None:
        self.world = World.new_founding_world(seed=seed)
        self._task: asyncio.Task | None = None
        self._running = False

    async def _loop(self) -> None:
        self._running = True
        while self._running:
            await asyncio.sleep(TICK_INTERVAL_SECONDS)
            events = self.world.tick()
            for event in events:
                await manager.broadcast(world_event_to_dict(event))
            if self.world.hour == 0:
                await manager.broadcast(
                    {"type": "day_summary", **self.world.summary()}
                )

    def start(self) -> None:
        if self._task is None:
            self._task = asyncio.create_task(self._loop())
            logger.info(
                "Simulation loop started (tick every %.1fs)", TICK_INTERVAL_SECONDS
            )

    async def stop(self) -> None:
        self._running = False
        if self._task is not None:
            self._task.cancel()
            try:
                await self._task
            except asyncio.CancelledError:
                pass
            self._task = None
        logger.info("Simulation loop stopped")


runner = SimulationRunner(seed=int(SEED) if SEED else None)


@asynccontextmanager
async def lifespan(app: FastAPI):
    runner.start()
    yield
    await runner.stop()


app = FastAPI(title="Solum API", version="0.1.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --- REST endpoints ---------------------------------------------------------

@app.get("/api/health")
async def health() -> dict:
    return {"status": "ok", "connected_clients": manager.active_count}


@app.get("/api/world")
async def get_world() -> dict:
    """Full world snapshot — day/hour, resources, and all NPCs."""
    return world_snapshot(runner.world)


@app.get("/api/npcs")
async def get_npcs() -> list[dict]:
    return [npc_to_dict(npc) for npc in runner.world.npcs]


@app.get("/api/npcs/{npc_id}")
async def get_npc(npc_id: int) -> dict:
    for npc in runner.world.npcs:
        if npc.id == npc_id:
            return npc_to_dict(npc)
    return {"error": f"No NPC with id {npc_id}"}


# --- WebSocket ---------------------------------------------------------------

@app.websocket("/ws/world")
async def world_ws(websocket: WebSocket) -> None:
    """
    On connect: send a full world_snapshot so the client can render
    immediately. After that, only event deltas are pushed (npc_moved,
    npc_worked, day_changed, etc.) per DESIGN.md §20.
    """
    await manager.connect(websocket)
    try:
        await websocket.send_json(world_snapshot(runner.world))
        while True:
            # This endpoint is currently push-only from the server; we
            # still need to await something so we notice disconnects.
            await websocket.receive_text()
    except WebSocketDisconnect:
        pass
    finally:
        await manager.disconnect(websocket)