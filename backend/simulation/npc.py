"""
NPC — a single inhabitant of Solum.

Implements the data model from docs/DESIGN.md section 5, plus a simple
rule-based decision loop (walk / eat / sleep / work / rest). This
stands in for the future AI Agent Architecture (docs/DESIGN.md section 14):
right now NPCs choose actions with fixed rules, but the interface —
observe needs -> choose action -> world validates & executes -> state
changes — is the same shape an AI-driven decision would plug into.
"""

from __future__ import annotations

import itertools
import random
from dataclasses import dataclass, field

from jobs import get_job

_id_counter = itertools.count(1)


@dataclass
class NPC:
    name: str
    occupation: str
    x: float
    y: float
    age: int = field(default_factory=lambda: random.randint(18, 55))
    id: int = field(default_factory=lambda: next(_id_counter))

    health: float = 100.0
    hunger: float = 20.0     # 0 = full, 100 = starving
    energy: float = 100.0
    money: float = 0.0

    skills: dict[str, float] = field(default_factory=dict)
    inventory: dict[str, float] = field(default_factory=dict)
    relationships: dict[int, float] = field(default_factory=dict)
    goals: list[str] = field(default_factory=list)
    memory: list[str] = field(default_factory=list)

    house: str | None = None
    current_action: str = "idle"
    target: tuple[float, float] | None = None

    # -- decision making ---------------------------------------------------

    def decide_action(self) -> str:
        """Pick the next action based on current needs. Rule-based for now;
        this is the seam where an AI-driven policy plugs in later."""
        if self.hunger > 70:
            return "eat"
        if self.energy < 20:
            return "sleep"
        if 22 <= (self._time_of_day or 12) or (self._time_of_day or 12) < 6:
            return "sleep"
        return "work"

    # -- per-tick update -----------------------------------------------------

    def step(self, world) -> None:
        self._time_of_day = world.hour
        action = self.decide_action()
        self.current_action = action

        if action == "eat":
            self._eat(world)
        elif action == "sleep":
            self._sleep()
        elif action == "work":
            self._work(world)

        # needs drift every tick regardless of action
        self.hunger = min(100.0, self.hunger + 0.4)
        self.energy = max(0.0, self.energy - 0.15)
        if self.hunger >= 100:
            self.health = max(0.0, self.health - 0.5)

    def _eat(self, world) -> None:
        if world.resources.get("food", 0) >= 1:
            world.resources["food"] -= 1
            self.hunger = max(0.0, self.hunger - 40)
            self._move_randomly(radius=2)
        else:
            # nothing to eat — keep hunting for food instead of standing still
            self._move_randomly(radius=8)

    def _sleep(self) -> None:
        self.energy = min(100.0, self.energy + 8)

    def _work(self, world) -> None:
        job = get_job(self.occupation)
        if self.energy < job.energy_cost:
            self._sleep()
            return

        self.energy -= job.energy_cost
        self.skills[job.trains_skill] = self.skills.get(job.trains_skill, 0) + 0.05

        if job.produces:
            world.resources[job.produces] = (
                world.resources.get(job.produces, 0) + job.output_per_tick
            )
            if job.produces == "money":
                self.money += job.output_per_tick

        self._move_randomly(radius=3)

    def _move_randomly(self, radius: float) -> None:
        self.x += random.uniform(-radius, radius)
        self.y += random.uniform(-radius, radius)

    # internal, set each step from world.hour
    _time_of_day: int | None = field(default=None, repr=False, compare=False)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "occupation": self.occupation,
            "age": self.age,
            "x": round(self.x, 1),
            "y": round(self.y, 1),
            "health": round(self.health, 1),
            "hunger": round(self.hunger, 1),
            "energy": round(self.energy, 1),
            "money": round(self.money, 1),
            "action": self.current_action,
            "skills": {k: round(v, 1) for k, v in self.skills.items()},
        }