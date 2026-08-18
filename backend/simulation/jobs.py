"""
Job / occupation definitions for Solum.

Each job describes what an NPC does at their workplace, what resource
it consumes/produces, and what skill it trains. This is intentionally
simple for the first milestone — no requirements, wages, or unlock
conditions yet (see docs/DESIGN.md section 6 for the full future model).
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Job:
    name: str
    workplace: str          # logical location type this job is tied to
    produces: str | None    # resource key in World.resources, or None
    output_per_tick: float
    energy_cost: float
    trains_skill: str


JOBS: dict[str, Job] = {
    "Farmer": Job("Farmer", "farm", "food", 1.5, 2.0, "farming"),
    "Fisher": Job("Fisher", "coast", "food", 1.2, 2.0, "fishing"),
    "Lumberjack": Job("Lumberjack", "forest", "wood", 1.5, 2.5, "lumberjacking"),
    "Miner": Job("Miner", "hills", "stone", 1.2, 3.0, "mining"),
    "Builder": Job("Builder", "construction_site", None, 0.0, 2.5, "building"),
    "Craftsman": Job("Craftsman", "workshop", "tools", 0.5, 1.5, "crafting"),
    "Merchant": Job("Merchant", "market", "money", 1.0, 1.0, "trading"),
    "Cook": Job("Cook", "kitchen", None, 0.0, 1.5, "cooking"),
    "Healer": Job("Healer", "clinic", None, 0.0, 1.0, "healing"),
    "Explorer": Job("Explorer", "wilds", None, 0.0, 2.0, "exploring"),
    "General Worker": Job("General Worker", "village", None, 0.0, 1.5, "general"),
}


def get_job(occupation: str) -> Job:
    """Look up a job, defaulting to General Worker for unknown occupations."""
    return JOBS.get(occupation, JOBS["General Worker"])