"""
Serialization helpers.

The simulation core (solum.simulation) is intentionally plain
dataclasses with no web/JSON concerns — see DESIGN.md §2 ("the
simulation engine is authoritative; the frontend visualizes the
world"). This module is the boundary that turns those dataclasses
into JSON-safe dicts for REST responses and WebSocket events, without
adding any web framework dependency into the simulation package
itself.
"""

from __future__ import annotations

from solum.simulation.npc import NPC
from solum.simulation.world import World, WorldEvent


def npc_to_dict(npc: NPC) -> dict:
    return {
        "id": npc.id,
        "name": npc.name,
        "age": npc.age,
        "position": {"x": npc.position.x, "y": npc.position.y},
        "occupation": npc.occupation,
        "alive": npc.alive,
        "health": round(npc.health, 1),
        "hunger": round(npc.hunger, 1),
        "energy": round(npc.energy, 1),
        "money": round(npc.money, 2),
        "skills": {k: round(v, 1) for k, v in npc.skills.items()},
        "inventory": {k: round(v, 1) for k, v in npc.inventory.items()},
        "goals": list(npc.goals),
        "relationships": dict(npc.relationships),
        "house": npc.house,
        "current_action": npc.current_action.value,
    }


def world_event_to_dict(event: WorldEvent) -> dict:
    return event.as_dict()


def world_snapshot(world: World) -> dict:
    """Full world state — sent once on WebSocket connect and available via GET /api/world."""
    return {
        "type": "world_snapshot",
        "day": world.day,
        "hour": world.hour,
        "is_night": world.is_night,
        "tick_count": world.tick_count,
        "population": world.population,
        "resources": {k: round(v, 1) for k, v in world.resources.items()},
        "npcs": [npc_to_dict(npc) for npc in world.npcs],
    }