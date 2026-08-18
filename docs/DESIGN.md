# Solum — Design Document

This document contains the full design specification for Solum. The top-level [README.md](../README.md) is the short public-facing overview; this file is the detailed reference for systems, data models, and long-term architecture.

## Table of Contents

- [1. Project Overview](#1-project-overview)
- [2. Core Philosophy](#2-core-philosophy)
- [3. Starting World — Day 0](#3-starting-world--day-0)
- [4. The 20 Founding NPCs](#4-the-20-founding-npcs)
- [5. NPC Data Model](#5-npc-data-model)
- [6. Jobs and Occupations](#6-jobs-and-occupations)
- [7. Skills vs Occupation](#7-skills-vs-occupation)
- [8. Basic NPC Actions](#8-basic-npc-actions)
- [9. World Systems](#9-world-systems)
- [10. Farm System](#10-farm-system)
- [11. Economy](#11-economy)
- [12. Seasons and Weather](#12-seasons-and-weather)
- [13. Village and Civilization Progression](#13-village-and-civilization-progression)
- [14. AI Agent Architecture](#14-ai-agent-architecture)
- [15. Emergent Behavior](#15-emergent-behavior)
- [16. Real-Time Public World](#16-real-time-public-world)
- [17. Frontend Vision](#17-frontend-vision)
- [18. NPC Inspection UI](#18-npc-inspection-ui)
- [19. Camera and World Interaction](#19-camera-and-world-interaction)
- [20. Real-Time Event Model](#20-real-time-event-model)
- [21. Solum Labs — Real-World Problem Simulation](#21-solum-labs--real-world-problem-simulation)
- [22. Simulation Branching and Rebirth](#22-simulation-branching-and-rebirth)
- [23. Event Sourcing / State Reconstruction](#23-event-sourcing--state-reconstruction)
- [24. A/B Experimentation](#24-ab-experimentation)
- [25. Main Frontend / Backend Architecture](#25-main-frontend--backend-architecture)
- [26. Proposed Technology Stack](#26-proposed-technology-stack)
- [27. Development Strategy](#27-development-strategy)
- [28. Development Milestones](#28-development-milestones)
- [29. Time and Difficulty Estimate](#29-time-and-difficulty-estimate)
- [30. Why the Project Is Technically Valuable](#30-why-the-project-is-technically-valuable)
- [31. Project Positioning](#31-project-positioning)
- [32. Branding](#32-branding)
- [33. First Concrete Goal](#33-first-concrete-goal)
- [34. First Simulation Loop](#34-first-simulation-loop)

---

## 1. Project Overview

Solum is a persistent AI-driven civilization simulation. A small island begins from ground zero with 20 inhabitants. The inhabitants are autonomous NPCs who work, eat, sleep, trade, build, form relationships, respond to weather and seasons, accumulate or lose wealth, and collectively develop their village. The simulation runs continuously on a server and can be observed in real time by anyone who opens the website.

The long-term goal is to turn Solum into an experimental sandbox: real-world-inspired problems can be introduced into the simulated civilization, the system can observe how the agents respond, and the result can be analyzed. Experiments can be branched from checkpoints and the world can be restored using a Rebirth mechanism.

## 2. Core Philosophy

- Solum should feel like a living world, not a static dashboard or a conventional CRUD application.
- The simulation engine is authoritative; the frontend visualizes the world rather than deciding what happens.
- AI should make high-level decisions for agents, while deterministic simulation rules validate and execute those decisions.
- The world should continue running even when nobody is viewing it.
- All visitors should observe the same persistent world state.
- The population should develop naturally rather than following a fixed script.
- The project should be technically substantial enough to demonstrate frontend, backend, AI, databases, algorithms, real-time systems, and system design skills.

## 3. Starting World — Day 0

| | |
|---|---|
| Population | 20 people |
| Houses | 0 |
| Farms | 0 |
| Roads | 0 |
| Money | 0 |
| Shops | 0 |
| Technology | 0 |

**Resources:** Food: 100 · Wood: 200 · Stone: 100 · Water: unlimited

The initial world is deliberately primitive. The civilization should gradually evolve from a small settlement into a more developed village or town.

## 4. The 20 Founding NPCs

The initial population uses simple Greek-inspired first names. These are starting occupations, not permanent assignments.

| # | Name | Starting Job | # | Name | Starting Job |
|---|------|---------------|---|------|---------------|
| 1 | Nikos | Farmer | 11 | Mia | Farmer |
| 2 | Alex | Builder | 12 | Eli | Fisher |
| 3 | Leo | Fisher | 13 | Nia | Builder |
| 4 | Theo | Farmer | 14 | Iris | Explorer |
| 5 | Dina | Lumberjack | 15 | Ema | Cook |
| 6 | Anna | Farmer | 16 | Tia | Farmer |
| 7 | Milo | Craftsman | 17 | Niko | Craftsman |
| 8 | Lena | Healer | 18 | Lia | Lumberjack |
| 9 | Gio | Farmer | 19 | Aris | Miner |
| 10 | Kris | Merchant | 20 | Zoe | General Worker |

## 5. NPC Data Model

```
NPC
├── id
├── name
├── age
├── position
├── health
├── hunger
├── energy
├── money
├── occupation
├── skills
├── inventory
├── personality
├── goals
├── relationships
├── house
└── memory
```

## 6. Jobs and Occupations

Not everyone is a farmer. Solum needs a real occupation system. An NPC's occupation is separate from their skills and can change over time based on demand, personal ability, goals, income, and circumstances.

| Role | Responsibility | Provides |
|------|-----------------|----------|
| Farmer | Crops, planting, harvesting | Food |
| Fisher | Fishing | Food |
| Lumberjack | Cutting trees | Wood |
| Miner | Mining | Stone and minerals |
| Builder | Houses and infrastructure | Buildings |
| Craftsman | Tools and items | Tools/items |
| Merchant | Trading | Trade |
| Cook | Preparing food | Meals |
| Healer | Health | Healthcare |
| Storekeeper | Storage and logistics | Logistics |
| Explorer | Finding resources | Information |
| Guard | Village security | Safety |

Initially only a subset needs to be implemented. More professions can unlock as the village develops.

```
Job
├── requirements
├── skills
├── workplace
├── inputs
├── outputs
├── salary
├── working hours
└── unlock conditions
```

**Example: Farmer**
- Required skill: Farming > 20
- Workplace: Farm
- Inputs: Seeds, water, labor
- Outputs: Wheat, vegetables
- Consumes: Energy
- Risks: Weather, disease, drought

## 7. Skills vs Occupation

An NPC should not be permanently defined by their job. A farmer can have strong building skills. A merchant can become a builder. A builder can become a farmer. A person can become unemployed or eventually hold multiple jobs.

```
MAYA
Occupation: Farmer

Skills:
Farming    87
Cooking    42
Building   31
Trading    65
Fishing    20
Mining     12
Healing    38
```

Example emergent behavior: construction demand increases, builder wages rise, and an NPC with high building skill may switch from farming to construction.

## 8. Basic NPC Actions

Walk · Eat · Sleep · Work · Rest

Farmers additionally perform: Plant · Grow · Harvest

## 9. World Systems

The world should eventually contain: Island and coastline · Forest · Mountains or hills · River and/or lake · Village · Farms · Roads · Resource locations · Houses · Markets and other buildings · Weather · Day/night cycle · Seasons · Economy · Technology progression · Village upgrades

## 10. Farm System

```
Farm
├── id
├── position
├── owner
├── crop
├── growth
├── water
└── health
```

Multiple crops can eventually exist. Crops progress visually through growth stages. Farm productivity depends on water, soil, weather, health, and labor. Later systems can include irrigation, fertilizer, pests, crop disease, storage, and harvest.

## 11. Economy

Money and wealth should emerge from production, wages, trade, ownership, scarcity, and individual choices.

Resources: Food · Wood · Stone · Water · Money · Tools · (other resources as the civilization develops)

```
Farmers     → Food  → Market
Merchants   → Trade → Money
Builders    → Buildings
Fishers     → Food
Lumberjacks → Wood
Miners      → Stone/minerals
Craftsmen   → Tools/items
```

Rich and poor should not be manually assigned. Wealth inequality should emerge from the simulation.

## 12. Seasons and Weather

- **Spring:** favorable rainfall and crop growth.
- **Summer:** possible heat and drought.
- **Autumn:** harvest and preparation.
- **Winter:** reduced production and importance of stored resources.

**Possible events:** Heavy storm · Forest fire · Locust infestation · Flood · Drought · Fish population collapse · New mineral discovery · Disease outbreak · Exceptional harvest

## 13. Village and Civilization Progression

| Stage | Description |
|-------|--------------|
| 0 | Campfire + tents |
| 1 | Primitive houses + small farms + storage + well |
| 2 | Village + roads + market + barn + workshop |
| 3 | School + clinic + blacksmith + larger farms + improved houses |
| 4 | Town + electricity + advanced agriculture + port + bank |
| 5 | Emergent future development determined by the simulation |

The final form of the civilization should not be completely predetermined. The simulation should allow the agents' needs, resources, decisions, and technologies to influence development.

## 14. AI Agent Architecture

The AI layer should not directly control arbitrary world state. The world engine remains authoritative.

```
World State
    ↓
NPC observes needs, economy, weather, relationships, goals
    ↓
AI chooses intention
    ↓
Simulation validates the action
    ↓
Action executes
    ↓
World state changes
    ↓
NPC memory/beliefs update
```

AI can eventually use personality, goals, skills, memories, relationships, prices, weather, resource availability, and future expectations to choose actions.

## 15. Emergent Behavior

- One NPC may hoard food during a drought.
- Another may share food with neighbors.
- Another may speculate on food prices.
- A farmer may become a builder because construction wages increase.
- Workers may move toward professions that are more useful or profitable.
- Economic inequality can naturally develop.
- The population can adapt to shortages and environmental changes.

## 16. Real-Time Public World

Solum should be continuously running on the server. When the website is loaded, visitors enter the current state of the same civilization.

```
                    SERVER
                      │
                WORLD STATE
                      │
          ┌───────────┼───────────┐
          ↓           ↓           ↓
       Browser A   Browser B   Browser C
          ↓           ↓           ↓
       Mumbai       Delhi      London
```

The frontend should receive state changes through WebSockets rather than repeatedly downloading the entire world.

## 17. Frontend Vision

The frontend should feel like a living world rather than a dashboard. It should display the island, village, farms, all 20 NPCs, buildings, weather, resources, and live events.

Island overview · Village close-up · Farm visualization · 20 visible NPCs · NPC movement · Weather effects · Day/night cycle · Zoom and pan · Follow an NPC · Click an NPC to inspect them · Click a farm/building/resource to inspect it · Live event feed · Population and economy statistics · Historical timeline · Experiment results

## 18. NPC Inspection UI

```
MAYA
Age: 27
Health: 94%
Hunger: 21%
Energy: 67%

Occupation: Farmer

Skills:
Farming     ████████░░
Cooking     ████░░░░░░
Building    ███░░░░░░░
Trading     ██████░░░░

Wealth: ₹1,284
House: Small Cottage

Relationships:
Ravi    78
Arun    42
Dev     18

Current goal:
Prepare enough food before winter

Current action:
Harvesting wheat
```

The UI can show system-generated decision explanations such as: "Maya chose to harvest today because food reserves are below her target and winter is approaching." This should explain behavior without exposing private chain-of-thought.

## 19. Camera and World Interaction

Zoom and pan around the island · Follow an NPC · Follow an event · Switch between island, village, and farm views · Smoothly move the camera to an NPC or location · Inspect any visible NPC, building, farm, resource, or important event.

## 20. Real-Time Event Model

The server should send compact changes/deltas instead of the entire world on every update.

```json
{ "type": "npc_moved", "npc_id": 7, "x": 421, "y": 193 }
{ "type": "weather_changed", "weather": "rain" }
```

Other event examples: farm harvested, building completed, NPC bought food, NPC changed job, storm started, resource depleted, or a new technology was unlocked.

## 21. Solum Labs — Real-World Problem Simulation

A future major feature is an experimental environment where users can introduce real-world-inspired problems into the island and observe how the civilization responds.

Drought · Flood · Climate change · Food shortage · Inflation · Wealth inequality · Crop disease · Fertilizer shortage · Infrastructure failure · Population growth · Migration · Technology introduction · Education policy · Water shortage · Power failure

These experiments should be clearly presented as simulations and not as guaranteed real-world predictions.

## 22. Simulation Branching and Rebirth

```
LIVE WORLD
    ↓
Checkpoint
    ↓
Create Experiment
    ↓
Introduce Problem
    ↓
Run Simulation
    ↓
Analyze Result
    ↓
Compare Scenarios
    ↓
Rebirth / Restore Checkpoint
```

If all characters die, the experiment can reach a civilization-extinction state. The system should preserve the pre-experiment checkpoint so the user can restore the civilization and allow it to continue from the same state under the normal server rules.

The main world should continue separately from experimental branches. Experiments should operate on a cloned snapshot or branch rather than destroying the public live world.

## 23. Event Sourcing / State Reconstruction

Rebirth should not require saving a complete database copy every few seconds. The simulation should use snapshots plus events.

```
WORLD STATE
Day 417
    ↓
SNAPSHOT
    ↓
Event 418: Rainfall ↓
Event 419: Farm A harvested
Event 420: Maya bought wheat
Event 421: Storm
Event 422: House damaged
...
    ↓
REBIRTH
    ↓
Load snapshot Day 417
    ↓
Discard experiment events
    ↓
Resume simulation
```

This introduces a real backend/system-design concept: event sourcing or state reconstruction.

## 24. A/B Experimentation

A later version can compare different interventions against the same starting checkpoint.

```
Scenario A: Do nothing
Scenario B: Build irrigation

                    A          B
Population          14         20
Food                83        612
Average wealth    2,130      4,920
Deaths               6          0
Farms                 7         14
```

The platform can report how the simulated outcomes differ and explain which mechanisms caused the difference.

## 25. Main Frontend / Backend Architecture

```
                         SOLUM
                           │
             ┌─────────────┴─────────────┐
             │                           │
        WORLD ENGINE                 AI ENGINE
             │                           │
      ┌──────┼──────┐              ┌─────┼─────┐
      ↓      ↓      ↓              ↓     ↓     ↓
   Time    Weather Economy       Goals Memory Decisions
      │      │      │              │     │     │
      └──────┼──────┘              └─────┼─────┘
             │                           │
             └─────────────┬─────────────┘
                           ↓
                     WORLD STATE
                           │
                    ┌──────┴──────┐
                    ↓             ↓
                PostgreSQL      Redis
                    │             │
                    └──────┬──────┘
                           ↓
                       WebSocket
                           ↓
                    SOLUM FRONTEND
```

## 26. Proposed Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Frontend | Next.js + React + TypeScript | Interactive web application |
| Visualization | Canvas initially; PixiJS or Three.js later | Island and NPC rendering |
| Styling | Tailwind CSS | UI styling |
| Backend | Python + FastAPI | API and WebSocket server |
| Database | PostgreSQL | Persistent world state and history |
| Live state | Redis later | Caching, pub/sub, queues |
| AI | LLM + possible smaller/local models later | Agent decision-making |
| Communication | WebSockets | Real-time world updates |

## 27. Development Strategy

Backend/simulation should come first, but not the entire backend. The first objective is a small, self-contained simulation core.

```
solum/
└── simulation/
    ├── world.py
    ├── npc.py
    ├── jobs.py
    └── main.py
```

Once the simulation produces meaningful state changes, connect a FastAPI backend, then PostgreSQL, then WebSockets, then build the visual frontend.

## 28. Development Milestones

- 20 NPCs exist with names, jobs, stats, and positions.
- NPCs can move around the island.
- NPCs have hunger, energy, and health.
- NPCs work according to their occupations.
- Farmers farm, fishers fish, lumberjacks collect wood, builders construct.
- The world has time, day/night, and seasons.
- Frontend displays the island, village, farm, and all NPCs.
- Real-time WebSocket updates allow everyone to see the same civilization.
- Economy and resource systems become persistent.
- AI agents begin making higher-level decisions.
- Relationships, memories, personality, and goals are added.
- Village upgrades and technology progression are added.
- Weather and disasters become more sophisticated.
- Simulation checkpoints and history are added.
- Solum Labs enables experimental branches.
- Rebirth restores a civilization to a previous checkpoint.
- A/B scenario comparison and analytics are added.

## 29. Time and Difficulty Estimate

| Version | Estimated Time | Scope |
|---------|----------------|-------|
| Visual prototype | ~2 weeks | Island, village, farms, NPC visuals, camera |
| Basic simulation | ~6–8 weeks | NPC needs, jobs, farming, resources, time |
| Real-time online world | ~10–14 weeks | Backend, persistence, WebSockets, shared state |
| AI + economy + weather | ~14–18 weeks | Agents, economy, seasons, weather |
| Experiment/rebirth system | ~18–22 weeks | Snapshots, branching, experiments, restoration |
| Highly polished version | ~5–7 months | Full public-facing Solum with advanced systems |

These are approximate solo-development estimates assuming roughly 15–20 hours per week while learning some of the technologies along the way. A respectable version can be targeted in roughly five months with consistent 2–3 hour daily sessions.

## 30. Why the Project Is Technically Valuable

| Skill | What Solum Demonstrates |
|-------|--------------------------|
| Frontend | Real-time UI, complex visualization, interactive world, state management, camera/navigation |
| Backend | Persistent services, APIs, WebSockets, event-driven architecture |
| Databases | People, relationships, resources, transactions, history, snapshots |
| AI | Autonomous agents, planning, memory, goals, decision-making |
| Algorithms | Pathfinding, scheduling, resource allocation, simulation |
| Distributed systems | Synchronizing one persistent world across many clients |
| Concurrency | Multiple NPCs and events acting simultaneously |
| System design | Separating world engine, AI engine, persistence, and presentation |
| Data engineering | Simulation history, event logs, analytics |
| Visualization | Rendering complex state in an understandable interface |
| Testing | Deterministic simulations and reproducible experiments |

## 31. Project Positioning

Solum should not be presented primarily as an AI game. The stronger framing is:

> "A persistent multi-agent simulation platform for studying emergent behavior in constrained environments."

The island and civilization are the visual interface. Underneath is a serious simulation and distributed application involving AI agents, economic modeling, real-time state synchronization, event sourcing, experimentation, and reproducibility.

## 32. Branding

**SOLUM** — One Island. Twenty Lives. Infinite Outcomes.

- Solum — the living civilization
- Solum Live — real-time public world
- Solum Labs — experimental scenarios
- Solum Archive — civilization history
- Solum Rebirth — restore a previous world state
- Solum Observatory — analytics and civilization statistics

## 33. First Concrete Goal

The first development target is deliberately small:

> "When I open Solum, I see an island containing a village, a farm, and 20 NPCs. The NPCs move around continuously according to their basic needs."

No AI, economy, authentication, or advanced architecture is required for the first milestone. The initial objective is simply to make the world live.

## 34. First Simulation Loop

```
TIME
 ↓
NPC NEEDS
 ↓
NPC ACTIONS
 ↓
RESOURCE CHANGES
 ↓
WORLD UPDATE
```

The simulation should eventually become the foundation on which the backend and frontend are built.