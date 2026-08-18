"""
World — the authoritative simulation state for Solum.

Owns the 20 NPCs, resources, and time/weather. The frontend and AI
layers only ever observe or request actions through this class; the
World is the single source of truth (docs/DESIGN.md sections 2 & 14).
"""

from __future__ import annotations

import random

from npc import NPC

FOUNDING_NPCS: list[tuple[str, str]] = [
    ("Nikos", "Farmer"), ("Alex", "Builder"), ("Leo", "Fisher"),
    ("Theo", "Farmer"), ("Dina", "Lumberjack"), ("Anna", "Farmer"),
    ("Milo", "Craftsman"), ("Lena", "Healer"), ("Gio", "Farmer"),
    ("Kris", "Merchant"), ("Mia", "Farmer"), ("Eli", "Fisher"),
    ("Nia", "Builder"), ("Iris", "Explorer"), ("Ema", "Cook"),
    ("Tia", "Farmer"), ("Niko", "Craftsman"), ("Lia", "Lumberjack"),
    ("Aris", "Miner"), ("Zoe", "General Worker"),
]

WEATHER_STATES = ["clear", "rain", "storm", "fog"]

# island bounds NPCs wander within (arbitrary world-space units)
ISLAND_WIDTH = 100
ISLAND_HEIGHT = 100

MINUTES_PER_TICK = 30  # each tick advances the world clock by this much


class World:
    def __init__(self, seed: int | None = None) -> None:
        if seed is not None:
            random.seed(seed)

        self.day = 0
        self.hour = 6
        self.minute = 0
        self.weather = "clear"

        self.resources: dict[str, float] = {
            "food": 100,
            "wood": 200,
            "stone": 100,
        }

        self.npcs: list[NPC] = [
            NPC(
                name=name,
                occupation=occupation,
                x=random.uniform(0, ISLAND_WIDTH),
                y=random.uniform(0, ISLAND_HEIGHT),
            )
            for name, occupation in FOUNDING_NPCS
        ]

        self.event_log: list[str] = []

    # -- time -----------------------------------------------------------

    def _advance_clock(self) -> None:
        self.minute += MINUTES_PER_TICK
        while self.minute >= 60:
            self.minute -= 60
            self.hour += 1
        if self.hour >= 24:
            self.hour -= 24
            self.day += 1
            self._maybe_change_weather()

    def _maybe_change_weather(self) -> None:
        if random.random() < 0.3:
            new_weather = random.choice(WEATHER_STATES)
            if new_weather != self.weather:
                self.weather = new_weather
                self.event_log.append(f"Day {self.day}: weather changed to {self.weather}")

    # -- simulation step --------------------------------------------------

    def tick(self) -> None:
        self._advance_clock()

        deaths: list[NPC] = []
        for npc in self.npcs:
            npc.step(self)
            if npc.health <= 0:
                deaths.append(npc)

        for npc in deaths:
            self.event_log.append(f"Day {self.day}: {npc.name} has died")
            self.npcs.remove(npc)

        # keep the log from growing forever in a long-running process
        if len(self.event_log) > 200:
            self.event_log = self.event_log[-200:]

    # -- serialization ------------------------------------------------------

    def to_dict(self) -> dict:
        return {
            "day": self.day,
            "hour": self.hour,
            "minute": self.minute,
            "weather": self.weather,
            "resources": self.resources,
            "population": len(self.npcs),
            "npcs": [npc.to_dict() for npc in self.npcs],
            "events": self.event_log[-20:],
        }