# SOLUM

**One Island. Twenty Lives. Infinite Outcomes.**

Solum is a persistent, AI-driven civilization simulation. A small island begins from ground zero with 20 autonomous NPCs who work, eat, sleep, trade, build, form relationships, respond to weather and seasons, and collectively develop their village — running continuously on a server and observable in real time by anyone who opens the website.

> "A persistent multi-agent simulation platform for studying emergent behavior in constrained environments."

📄 **Full design specification:** [`docs/DESIGN.md`](docs/DESIGN.md) — data models, world systems, economy, AI architecture, real-time protocol, Solum Labs (experiment branching + rebirth), tech stack, and roadmap.

---

## Current Status

🚧 Early simulation core. See [First Concrete Goal](docs/DESIGN.md#33-first-concrete-goal):

> "When I open Solum, I see an island containing a village, a farm, and 20 NPCs. The NPCs move around continuously according to their basic needs."

No AI, economy, authentication, or advanced architecture yet — this stage is purely about making the world *live*.

## Project Structure

```
Solum/
├── backend/
│   ├── README.md
│   ├── requirements.txt
│   ├── docs/
│   │   └── DESIGN.md          # full specification
│   └── solum/
│       ├── __init__.py
│       ├── simulation/         # pure Python simulation core, no web deps
│       │   ├── __init__.py
│       │   ├── npc.py          # NPC data model + behavior
│       │   ├── jobs.py         # occupation definitions
│       │   ├── world.py        # world state, tick loop, resources
│       │   └── main.py         # CLI entry point (standalone runs)
│       └── api/                # FastAPI layer wrapping the simulation
│           ├── __init__.py
│           ├── server.py       # app, background tick loop, REST + WebSocket routes
│           ├── connection_manager.py  # WebSocket broadcast manager
│           └── schemas.py      # dataclass -> JSON serialization
└── frontend/                   # (sibling folder, not covered here)
```

## Getting Started

Requires Python 3.10+.

```bash
cd backend
pip install -r requirements.txt
```

### Run the simulation as a standalone script (no server)

```bash
python -m solum.simulation.main --ticks 50
```

This starts the world with the 20 founding NPCs, ticks time forward, and prints world/NPC events to the console.

### Run the live API server

```bash
uvicorn solum.api.server:app --reload --port 8000
```

This runs the same simulation core inside a FastAPI process: the world ticks forward continuously in real time in the background, and clients connect over REST or WebSocket to observe it — matching DESIGN.md §16 ("the world should continue running even when nobody is viewing it").

| Endpoint | Description |
|----------|-------------|
| `GET /api/health` | server status + connected client count |
| `GET /api/world` | full world snapshot (day/hour, resources, all NPCs) |
| `GET /api/npcs` | list of all NPCs |
| `GET /api/npcs/{id}` | single NPC detail |
| `WS /ws/world` | live event stream — sends a full snapshot on connect, then event deltas (`npc_moved`, `npc_worked`, `day_changed`, etc.) as they happen |

Interactive API docs are available at `http://localhost:8000/docs` once the server is running.

Config via environment variables:

| Variable | Default | Purpose |
|----------|---------|---------|
| `SOLUM_TICK_INTERVAL` | `2.0` | seconds of real time per simulated hour |
| `SOLUM_SEED` | unset (random) | seed for reproducible runs |
| `SOLUM_CORS_ORIGINS` | localhost:3000, localhost:5173 | allowed frontend origins |

### Run for a fixed number of ticks (CLI only)

```bash
python -m solum.simulation.main --ticks 50
```

### Quieter output (state summary only, not per-event logs)

```bash
python -m solum.simulation.main --ticks 200 --quiet
```

## Roadmap

Backend/simulation comes first. Once the simulation core produces meaningful state changes, the plan is: FastAPI backend → PostgreSQL → WebSockets → visual frontend (Next.js + Canvas/PixiJS).

See the full [Development Milestones](docs/DESIGN.md#28-development-milestones) and [Time Estimate](docs/DESIGN.md#29-time-and-difficulty-estimate) in the design doc.

## Tech Stack (Planned)

| Layer | Technology |
|-------|-----------|
| Frontend | Next.js + React + TypeScript, Tailwind CSS |
| Visualization | Canvas → PixiJS/Three.js |
| Backend | Python + FastAPI |
| Database | PostgreSQL (+ Redis later) |
| Realtime | WebSockets |
| AI | LLM-driven agent decisions |

Details in [`docs/DESIGN.md` § 26](docs/DESIGN.md#26-proposed-technology-stack).

---

*Solum — one island, twenty lives, infinite outcomes.*