````markdown
# SOLUM

### One Island. Twenty Lives. Infinite Outcomes.

> A persistent multi-agent civilization simulation where autonomous inhabitants build, survive, trade, adapt, and evolve in a continuously running world.

<p align="center">
  <img src="https://img.shields.io/badge/Status-In%20Development-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/AI-Multi--Agent-purple?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Simulation-Live%20World-2ea44f?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" />
</p>

---

## The Idea

Solum begins with almost nothing.

```text
                         DAY 0

                    ONE ISLAND

                       20 PEOPLE

                    0 BUILDINGS
                    0 FARMS
                    0 ROADS
                    0 ECONOMY
                    0 TECHNOLOGY

                         |
                         v

                   SIMULATION STARTS
````

Twenty people.

One island.

No civilization.

The world then begins to evolve.

---

## A World That Thinks

The inhabitants of Solum are autonomous agents rather than predefined scripted characters.

Each NPC has its own:

```text
Personality
Goals
Skills
Needs
Memory
Relationships
Wealth
Occupation
Knowledge
```

They observe their surroundings, make decisions, experience consequences, and influence the world around them.

---

## The Founders

The initial population consists of 20 inhabitants.

|  # | Name  | Starting Occupation |
| -: | ----- | ------------------- |
| 01 | Nikos | Farmer              |
| 02 | Alex  | Builder             |
| 03 | Leo   | Fisher              |
| 04 | Theo  | Farmer              |
| 05 | Dina  | Lumberjack          |
| 06 | Anna  | Farmer              |
| 07 | Milo  | Craftsman           |
| 08 | Lena  | Healer              |
| 09 | Gio   | Farmer              |
| 10 | Kris  | Merchant            |
| 11 | Mia   | Farmer              |
| 12 | Eli   | Fisher              |
| 13 | Nia   | Builder             |
| 14 | Iris  | Explorer            |
| 15 | Ema   | Cook                |
| 16 | Tia   | Farmer              |
| 17 | Niko  | Craftsman           |
| 18 | Lia   | Lumberjack          |
| 19 | Aris  | Miner               |
| 20 | Zoe   | General Worker      |

These are starting occupations, not permanent assignments.

A person's skills, goals, economic conditions, and personal circumstances can cause their occupation to change.

---

## The Economy

Solum contains a dynamic resource and economic system.

```text
                    FARMERS
                       |
                       v
                     FOOD
                       |
                       v
                    MARKET
                   /       \
                  v         v
             MERCHANTS    PEOPLE
                  |         |
                  v         v
                MONEY      NEEDS
                  |
        ----------+----------
        |         |         |
        v         v         v
     BUILDERS   FISHERS   CRAFTSMEN
```

Resources become scarce.

Scarcity affects prices.

Prices affect decisions.

Decisions affect production.

Production changes the economy again.

Wealth is not assigned manually.

It emerges from the simulation.

---

## Occupations

NPCs are not defined by a single permanent job.

A job has its own requirements, inputs, outputs, workplace, working hours, and potential income.

```text
Job
├── Requirements
├── Skills
├── Workplace
├── Inputs
├── Outputs
├── Salary
├── Working Hours
└── Unlock Conditions
```

Initial occupations include:

```text
Farmer
Fisher
Lumberjack
Miner
Builder
Craftsman
Merchant
Cook
Healer
Storekeeper
Explorer
Guard
```

As the civilization develops, new professions can emerge.

---

## Skills Are Not Jobs

An NPC's skills are separate from their occupation.

A farmer can have strong building skills.

A merchant can become a builder.

A builder can become a farmer.

A person can become unemployed.

A person can eventually have multiple jobs.

Example:

```text
MAYA

Occupation: Farmer

Skills:
Farming       87
Cooking       42
Building      31
Trading       65
Fishing       20
Mining        12
Healing       38
```

If construction demand increases and Maya has strong building skills, she may decide to change occupations.

```text
Construction Demand
        |
        v
Builder Wages Increase
        |
        v
Maya Evaluates Options
        |
        v
Occupation Changes
        |
        v
Farmer -> Builder
```

This creates a dynamic labor market rather than a fixed set of NPC roles.

---

## From Nothing

The civilization evolves through stages.

```text
DAY 0
  |
  v
CAMP
  |
  v
FIRST HOMES
  |
  v
FARMS
  |
  v
VILLAGE
  |
  v
MARKET
  |
  v
WORKSHOPS
  |
  v
SCHOOL / CLINIC
  |
  v
TOWN
  |
  v
UNKNOWN
```

The final state of the civilization is not completely predetermined.

---

## A Dynamic Environment

The world changes continuously.

### Seasons

```text
SPRING
   |
   v
SUMMER
   |
   v
AUTUMN
   |
   v
WINTER
   |
   +----------------+
                    |
                    v
                  SPRING
```

Seasons can affect:

* Crop growth
* Food production
* Water availability
* Working conditions
* Resource consumption
* Survival

### Weather

Possible events include:

```text
Storm
Flood
Drought
Forest Fire
Disease
Locust Infestation
Exceptional Harvest
Resource Discovery
```

The important part is not the event itself.

It is how the inhabitants respond to it.

---

## NPC Simulation

An NPC continuously evaluates the world around them.

```text
WORLD STATE
     |
     v
NPC OBSERVATION
     |
     +---- Needs
     +---- Goals
     +---- Economy
     +---- Weather
     +---- Relationships
     +---- Resources
     |
     v
AI DECISION
     |
     v
INTENTION
     |
     v
SIMULATION ENGINE
     |
     v
WORLD UPDATE
```

The AI does not directly modify the world.

The simulation engine remains authoritative.

This keeps the system deterministic, testable, and reproducible.

---

## A Living World

Solum is designed to run continuously on a server.

When someone opens the website, they are observing the current state of the same civilization.

```text
                    SOLUM SERVER
                         |
                    WORLD STATE
                         |
             +-----------+-----------+
             |           |           |
             v           v           v
          Browser A   Browser B   Browser C
```

If an NPC moves, everyone observing the world sees the change.

If a storm begins, everyone sees the storm.

If a building is completed, everyone sees the new building.

---

## The World Interface

The frontend will display the actual world rather than only statistics.

```text
+-------------------------------------------------------+
| SOLUM                         DAY 427 | AUTUMN | 14:32 |
+-------------------------------------------------------+
|                                                       |
|                     ISLAND                            |
|                                                       |
|       FARM                 VILLAGE                   |
|                                                       |
|    [CROPS]       [HOUSE] [HOUSE] [MARKET]            |
|                                                       |
|             [NPC]       [NPC]                        |
|                                                       |
|                       [FARM]                          |
|                                                       |
|          FOREST                         RIVER         |
|                                                       |
+-------------------------------------------------------+
| Population | Food | Wealth | Buildings | Weather      |
+-------------------------------------------------------+
| LIVE EVENTS                                            |
| Nikos harvested wheat                                 |
| Alex completed House #12                              |
| Rain started                                          |
+-------------------------------------------------------+
```

Users will eventually be able to:

* Zoom and pan around the island
* Follow individual NPCs
* Inspect NPCs
* Inspect farms
* Inspect buildings
* Inspect resources
* Observe weather
* View the economy
* Explore civilization history
* Watch experiments in real time

---

## Individual NPCs

Every inhabitant has an individual state.

```text
MAYA

Age:          27
Health:       94%
Hunger:       21%
Energy:       67%

Occupation:   Farmer

Skills:
Farming       87
Cooking       42
Building      31
Trading       65

Wealth:       1,284

Current Goal:
Prepare enough food before winter

Current Action:
Harvesting wheat
```

The system can also provide a high-level explanation of observable decisions:

> Maya chose to harvest because food reserves were below her target and winter was approaching.

---

## The Island

The world will contain:

```text
Island
├── Coastline
├── Forest
├── Mountains / Hills
├── River
├── Lake
├── Village
├── Farms
├── Roads
├── Resource Deposits
├── Houses
└── Public Buildings
```

The island itself can evolve as the civilization develops.

---

## The Farm

Farms are active parts of the simulation.

```text
Farm
├── ID
├── Position
├── Owner
├── Crop
├── Growth
├── Water
├── Soil Quality
├── Health
└── Workers
```

Crops progress through visible growth stages:

```text
Seed
  |
  v
Sprout
  |
  v
Growing
  |
  v
Mature
  |
  v
Harvest
```

Future systems can include:

* Multiple crop types
* Irrigation
* Fertilizer
* Soil degradation
* Pests
* Crop disease
* Crop storage
* Weather effects
* Seasonal yields

---

## Camera and World Interaction

The frontend should allow the user to explore the world.

```text
Zoom
Pan
Follow NPC
Follow Event
Island Overview
Village View
Farm View
```

Clicking an NPC opens their information.

Clicking a farm shows its current state.

Clicking a building shows its owner, purpose, condition, and activity.

Clicking weather or environmental events shows their current impact.

---

## Real-Time Events

The server should send compact world changes rather than repeatedly transmitting the entire world.

Example:

```json
{
  "type": "npc_moved",
  "npc_id": 7,
  "x": 421,
  "y": 193
}
```

Another example:

```json
{
  "type": "weather_changed",
  "weather": "rain"
}
```

Other possible events:

```text
NPC moved
NPC changed occupation
NPC bought food
Farm harvested
Farm planted
Building completed
Building damaged
Weather changed
Storm started
Resource depleted
Technology unlocked
Market price changed
NPC became sick
NPC recovered
```

---

## Solum Labs

The live civilization is also an experimental environment.

Users can eventually introduce controlled problems and observe the resulting behavior.

```text
LIVE WORLD
    |
    v
CHECKPOINT
    |
    v
EXPERIMENT
    |
    v
INTRODUCE EVENT
    |
    v
SIMULATE
    |
    v
RESULTS
    |
    +----------+
    |          |
    v          v
 ANALYZE     REBIRTH
```

Possible experiments:

```text
Drought
Flood
Food Shortage
Inflation
Climate Change
Crop Disease
Water Shortage
Population Growth
Migration
Infrastructure Failure
New Technology
Education Policy
```

The results are simulation outcomes, not predictions of guaranteed real-world behavior.

---

## Civilization Collapse

Solum does not guarantee survival.

A civilization can fail.

```text
DAY 692

POPULATION: 0

CAUSE OF COLLAPSE

Drought
   |
   v
Crop Failure
   |
   v
Food Shortage
   |
   v
Price Increase
   |
   v
Starvation
   |
   v
CIVILIZATION COLLAPSE
```

A civilization can reach complete extinction.

This is a valid outcome of the simulation.

---

## Rebirth

Solum uses checkpoints and simulation branches.

```text
                    DAY 417
                       |
                  CHECKPOINT
                       |
                +------+------+
                |             |
                v             v
           LIVE WORLD     EXPERIMENT
                              |
                              v
                           Drought
                              |
                              v
                          COLLAPSE
                              |
                              v
                           REBIRTH
                              |
                              v
                          DAY 417
```

The original world is preserved.

The experiment is discarded.

The civilization continues from the previous state.

---

## Event-Based World State

Rebirth is designed around snapshots and events rather than constantly duplicating the entire database.

```text
WORLD STATE
DAY 417
   |
   v
SNAPSHOT
   |
   +-- Event 418: Rainfall decreased
   +-- Event 419: Farm harvested
   +-- Event 420: Maya bought wheat
   +-- Event 421: Storm started
   +-- Event 422: House damaged
   |
   v
RECONSTRUCTED STATE
```

This introduces event sourcing and state reconstruction into the architecture.

---

## Experiment Branching

The live world should remain unaffected by experiments.

```text
                    LIVE WORLD
                        |
                        v
                   CHECKPOINT
                        |
              +---------+---------+
              |                   |
              v                   v
          LIVE WORLD          EXPERIMENT
                                  |
                                  v
                            MODIFIED STATE
                                  |
                                  v
                              SIMULATE
                                  |
                                  v
                              RESULTS
```

This allows the same civilization state to be used as the starting point for multiple experiments.

---

## Experiment Comparison

The same checkpoint can be used to compare different interventions.

```text
                     DAY 417
                        |
                   CHECKPOINT
                        |
              +---------+---------+
              |                   |
              v                   v
         SCENARIO A          SCENARIO B
         No Irrigation       Irrigation
              |                   |
              v                   v
          SIMULATE             SIMULATE
              |                   |
              +---------+---------+
                        |
                        v
                     COMPARE
```

Example:

| Metric         | Scenario A | Scenario B |
| -------------- | ---------: | ---------: |
| Population     |         14 |         20 |
| Food           |         83 |        612 |
| Average Wealth |      2,130 |      4,920 |
| Deaths         |          6 |          0 |
| Farms          |          7 |         14 |

The system can analyze why the scenarios diverged.

---

## Architecture

```text
                         SOLUM
                           |
             +-------------+-------------+
             |                           |
        WORLD ENGINE                 AI ENGINE
             |                           |
      +------+------+              +-----+-----+
      |      |      |              |     |     |
     Time  Weather Economy        Goals Memory Decisions
      |      |      |              |     |     |
      +------+------+              +-----+-----+
             |                           |
             +-------------+-------------+
                           |
                     WORLD STATE
                           |
                  +--------+--------+
                  |                 |
                  v                 v
             PostgreSQL          Redis
                  |                 |
                  +--------+--------+
                           |
                       WebSocket
                           |
                           v
                    SOLUM FRONTEND
```

---

## Technology Stack

### Frontend

```text
Next.js
React
TypeScript
Tailwind CSS
Canvas
PixiJS / Three.js
```

### Backend

```text
Python
FastAPI
WebSockets
```

### Database

```text
PostgreSQL
Redis
```

### AI

```text
LLMs
Agent Memory
Embeddings
Decision Systems
```

---

## Development Strategy

Solum will be developed from the simulation core outward.

```text
Simulation Engine
        |
        v
Backend API
        |
        v
Database
        |
        v
WebSocket Layer
        |
        v
Frontend World
        |
        v
AI Agents
        |
        v
Advanced Civilization
        |
        v
Solum Labs
```

The first version should not attempt to implement every system simultaneously.

Each milestone should produce a functioning piece of the world.

---

## Development Roadmap

### Phase I — The World

* [ ] Create island
* [ ] Create village
* [ ] Create 20 NPCs
* [ ] NPC movement
* [ ] Basic jobs
* [ ] Basic resources
* [ ] Basic farm
* [ ] Day/night cycle

### Phase II — Civilization

* [ ] Hunger
* [ ] Energy
* [ ] Health
* [ ] Inventory
* [ ] Economy
* [ ] Trading
* [ ] Buildings
* [ ] Seasons
* [ ] Weather
* [ ] Dynamic occupations

### Phase III — Intelligence

* [ ] NPC personality
* [ ] NPC goals
* [ ] NPC memory
* [ ] Relationships
* [ ] AI decision making
* [ ] Agent planning
* [ ] Emergent behavior

### Phase IV — Persistence

* [ ] PostgreSQL
* [ ] World persistence
* [ ] Event system
* [ ] Snapshots
* [ ] WebSockets
* [ ] Real-time public world
* [ ] Historical replay

### Phase V — Civilization

* [ ] Village upgrades
* [ ] Technology progression
* [ ] Advanced economy
* [ ] Infrastructure
* [ ] Population changes
* [ ] Resource depletion
* [ ] Advanced professions

### Phase VI — Solum Labs

* [ ] Experiment branches
* [ ] Scenario injection
* [ ] Simulation comparison
* [ ] Historical replay
* [ ] Civilization collapse
* [ ] Rebirth
* [ ] Experiment analytics

---

## First Milestone

The first objective is intentionally small.

> **When Solum is opened, an island should contain a village, a farm, and 20 NPCs. The NPCs should move continuously according to their basic needs.**

No advanced AI.

No complex economy.

No experiments.

No authentication.

Just a world that is alive.

---

## First Simulation Loop

```text
TIME
  |
  v
NPC NEEDS
  |
  v
NPC ACTIONS
  |
  v
RESOURCE CHANGES
  |
  v
WORLD UPDATE
```

The simulation engine will eventually become the foundation for the backend, AI system, and frontend.

---

## Project Status

```text
SOLUM

Simulation Engine       [ PLANNED ]
NPC System              [ PLANNED ]
Occupation System       [ PLANNED ]
Economy                 [ PLANNED ]
Weather                 [ PLANNED ]
AI Agents               [ PLANNED ]
Real-Time World         [ PLANNED ]
Solum Labs              [ PLANNED ]
Rebirth System          [ PLANNED ]

Status: EARLY DEVELOPMENT
```

---

## Why Solum?

Solum is not intended to be another AI wrapper or CRUD application.

The project combines:

```text
Artificial Intelligence
        +
Multi-Agent Systems
        +
Simulation
        +
Real-Time Systems
        +
Distributed State
        +
Economics
        +
Algorithms
        +
Data Visualization
        +
Frontend Engineering
        +
Backend Engineering
```

The visible island is only the surface.

Underneath it is a persistent simulation engine capable of producing, storing, branching, replaying, and analyzing complex world states.

---

## License

This project is licensed under the MIT License.

See [LICENSE](LICENSE) for details.

---

<p align="center">

## SOLUM

### One Island. Twenty Lives. Infinite Outcomes.

</p>
```
