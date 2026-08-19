import { useEffect, useRef, useState } from "react";
import type { WorldNpc, WorldState } from "../types/world";

const ISLAND_WIDTH = 100;
const ISLAND_HEIGHT = 100;
const PADDING = 30;
const CANVAS_SIZE = 700;

interface Props {
  world: WorldState | null;
}

function toScreen(x: number, y: number): [number, number] {
  const scaleX = (CANVAS_SIZE - PADDING * 2) / ISLAND_WIDTH;
  const scaleY = (CANVAS_SIZE - PADDING * 2) / ISLAND_HEIGHT;
  return [PADDING + x * scaleX, PADDING + y * scaleY];
}

function roundRect(
  ctx: CanvasRenderingContext2D,
  x: number,
  y: number,
  w: number,
  h: number,
  r: number
) {
  ctx.beginPath();
  ctx.moveTo(x + r, y);
  ctx.arcTo(x + w, y, x + w, y + h, r);
  ctx.arcTo(x + w, y + h, x, y + h, r);
  ctx.arcTo(x, y + h, x, y, r);
  ctx.arcTo(x, y, x + w, y, r);
  ctx.closePath();
}

export default function WorldCanvas({ world }: Props) {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const [hoveredNpc, setHoveredNpc] = useState<WorldNpc | null>(null);
  const [tooltipPos, setTooltipPos] = useState<{ x: number; y: number } | null>(null);

  // redraw whenever the world state or hover target changes
  useEffect(() => {
    const canvas = canvasRef.current;
    const ctx = canvas?.getContext("2d");
    if (!canvas || !ctx) return;

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    const rootStyles = getComputedStyle(document.documentElement);
    ctx.fillStyle = rootStyles.getPropertyValue("--island");
    const [ix, iy] = toScreen(0, 0);
    roundRect(ctx, ix, iy, CANVAS_SIZE - PADDING * 2, CANVAS_SIZE - PADDING * 2, 24);
    ctx.fill();

    if (!world) return;

    for (const npc of world.npcs) {
      const [sx, sy] = toScreen(npc.x, npc.y);
      const isHovered = hoveredNpc?.id === npc.id;

      ctx.beginPath();
      ctx.arc(sx, sy, isHovered ? 7 : 5, 0, Math.PI * 2);
      ctx.fillStyle = rootStyles.getPropertyValue("--npc");
      ctx.fill();

      if (isHovered) {
        ctx.strokeStyle = "#fff";
        ctx.lineWidth = 1.5;
        ctx.stroke();
      }
    }
  }, [world, hoveredNpc]);

  function handleMouseMove(e: React.MouseEvent<HTMLCanvasElement>) {
    if (!world) return;
    const rect = e.currentTarget.getBoundingClientRect();
    const mx = e.clientX - rect.left;
    const my = e.clientY - rect.top;

    let found: WorldNpc | null = null;
    for (const npc of world.npcs) {
      const [sx, sy] = toScreen(npc.x, npc.y);
      if (Math.hypot(sx - mx, sy - my) < 8) {
        found = npc;
        break;
      }
    }

    setHoveredNpc(found);
    setTooltipPos(found ? { x: e.clientX, y: e.clientY } : null);
  }

  function handleMouseLeave() {
    setHoveredNpc(null);
    setTooltipPos(null);
  }

  return (
    <div className="stage-wrap">
      <canvas
        ref={canvasRef}
        width={CANVAS_SIZE}
        height={CANVAS_SIZE}
        onMouseMove={handleMouseMove}
        onMouseLeave={handleMouseLeave}
      />

      {world && (
        <div className="hud">
          Day {world.day} — {String(world.hour).padStart(2, "0")}:
          {String(world.minute).padStart(2, "0")}
          <br />
          Weather: {world.weather}
          <br />
          Population: {world.population}
          <br />
          Food {world.resources.food?.toFixed(0)} · Wood{" "}
          {world.resources.wood?.toFixed(0)} · Stone{" "}
          {world.resources.stone?.toFixed(0)}
        </div>
      )}

      {hoveredNpc && tooltipPos && (
        <div
          className="tooltip"
          style={{ left: tooltipPos.x + 14, top: tooltipPos.y + 10 }}
        >
          <strong>{hoveredNpc.name}</strong> ({hoveredNpc.occupation})
          <br />
          {hoveredNpc.action} · health {hoveredNpc.health}% · hunger{" "}
          {hoveredNpc.hunger}% · energy {hoveredNpc.energy}%
        </div>
      )}
    </div>
  );
}