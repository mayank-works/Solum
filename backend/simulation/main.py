"""
Solum backend — runs the simulation as a background task and streams
world state to every connected browser over a shared WebSocket, so all
visitors see the same live civilization (docs/DESIGN.md section 16).

Run with:
    uvicorn main:app --reload
"""

from __future__ import annotations

import asyncio
import sys
from pathlib import Path

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

# the simulation core is a standalone package one directory up
sys.path.append(str(Path(__file__).resolve().parent.parent / "simulation"))
from world import World  # noqa: E402

TICK_SECONDS = 1.0  # real-world seconds between simulation ticks

app = FastAPI(title="Solum")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten this before deploying publicly
    allow_methods=["*"],
    allow_headers=["*"],
)

world = World()
connections: set[WebSocket] = set()


@app.on_event("startup")
async def start_simulation_loop() -> None:
    asyncio.create_task(_simulation_loop())


async def _simulation_loop() -> None:
    """Advance the world and broadcast the new state to every client.
    This is the one and only place world.tick() is called — the world
    keeps running even with zero connected browsers."""
    while True:
        world.tick()
        await _broadcast(world.to_dict())
        await asyncio.sleep(TICK_SECONDS)


async def _broadcast(payload: dict) -> None:
    dead: list[WebSocket] = []
    for ws in connections:
        try:
            await ws.send_json(payload)
        except Exception:
            dead.append(ws)
    for ws in dead:
        connections.discard(ws)


@app.get("/world")
async def get_world() -> dict:
    """One-shot snapshot of current world state (useful for debugging)."""
    return world.to_dict()


@app.websocket("/ws")
async def world_stream(websocket: WebSocket) -> None:
    await websocket.accept()
    connections.add(websocket)
    try:
        # send an immediate snapshot so the client doesn't wait for the next tick
        await websocket.send_json(world.to_dict())
        while True:
            # this endpoint is broadcast-only for now; keep the connection open
            await websocket.receive_text()
    except WebSocketDisconnect:
        pass
    finally:
        connections.discard(websocket)