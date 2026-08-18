"""
WebSocket connection manager.

Tracks connected clients and broadcasts world events to all of them —
DESIGN.md §16 ("all visitors should observe the same persistent world
state") and §20 (compact event deltas rather than full state on every
update). A disconnect during broadcast is treated as a normal
occurrence (browser tab closed, network drop) and the client is
dropped silently rather than raising.
"""

from __future__ import annotations

import asyncio
import logging

from fastapi import WebSocket

logger = logging.getLogger("solum.api")


class ConnectionManager:
    def __init__(self) -> None:
        self._connections: set[WebSocket] = set()
        self._lock = asyncio.Lock()

    async def connect(self, websocket: WebSocket) -> None:
        await websocket.accept()
        async with self._lock:
            self._connections.add(websocket)
        logger.info("Client connected (%d total)", len(self._connections))

    async def disconnect(self, websocket: WebSocket) -> None:
        async with self._lock:
            self._connections.discard(websocket)
        logger.info("Client disconnected (%d total)", len(self._connections))

    async def broadcast(self, message: dict) -> None:
        """Send a JSON-serializable message to every connected client."""
        async with self._lock:
            targets = list(self._connections)

        stale: list[WebSocket] = []
        for connection in targets:
            try:
                await connection.send_json(message)
            except Exception:
                stale.append(connection)

        if stale:
            async with self._lock:
                for connection in stale:
                    self._connections.discard(connection)

    @property
    def active_count(self) -> int:
        return len(self._connections)