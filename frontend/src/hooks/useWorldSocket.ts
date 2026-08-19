import type { useEffect, useRef, useState } from "react";
import type { WorldState } from "../types/world";

export type ConnectionStatus = "connecting" | "connected" | "disconnected";

const RECONNECT_DELAY_MS = 2000;

/**
 * Connects to the Solum backend's WebSocket (backend/simulation/main.py's
 * `/ws` endpoint) and keeps `world` in sync with every broadcast. The
 * backend sends a full snapshot on every tick, so this hook just replaces
 * state wholesale on each message — no client-side diffing needed.
 *
 * Auto-reconnects on drop, same behavior as the original vanilla JS version.
 */
export function useWorldSocket(url: string) {
  const [world, setWorld] = useState<WorldState | null>(null);
  const [status, setStatus] = useState<ConnectionStatus>("connecting");
  const socketRef = useRef<WebSocket | null>(null);
  const reconnectTimer = useRef<ReturnType<typeof setTimeout> | null>(null);

  useEffect(() => {
    let cancelled = false;

    function connect() {
      const ws = new WebSocket(url);
      socketRef.current = ws;

      ws.onopen = () => {
        if (!cancelled) setStatus("connected");
      };

      ws.onmessage = (event) => {
        if (cancelled) return;
        try {
          const data = JSON.parse(event.data) as WorldState;
          setWorld(data);
        } catch (err) {
          console.error("Failed to parse world state:", err);
        }
      };

      ws.onclose = () => {
        if (cancelled) return;
        setStatus("disconnected");
        reconnectTimer.current = setTimeout(connect, RECONNECT_DELAY_MS);
      };

      ws.onerror = () => {
        ws.close();
      };
    }

    connect();

    return () => {
      cancelled = true;
      if (reconnectTimer.current) clearTimeout(reconnectTimer.current);
      socketRef.current?.close();
    };
  }, [url]);

  return { world, status };
}
