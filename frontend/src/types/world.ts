/**
 * These mirror World.to_dict() and NPC.to_dict() in
 * backend/simulation/world.py and npc.py exactly. If you add a field
 * on the Python side, add it here too — this is the single place the
 * frontend and backend contract is defined.
 */

export interface WorldNpc {
  id: number;
  name: string;
  occupation: string;
  age: number;
  x: number;
  y: number;
  health: number;
  hunger: number;
  energy: number;
  money: number;
  action: string;
  skills: Record<string, number>;
}

export interface WorldState {
  day: number;
  hour: number;
  minute: number;
  weather: string;
  resources: Record<string, number>;
  population: number;
  npcs: WorldNpc[];
  events: string[];
}
