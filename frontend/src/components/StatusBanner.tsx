import type { ConnectionStatus } from "../hooks/useWorldSocket";

interface Props {
  status: ConnectionStatus;
  url: string;
}

const LABELS: Record<ConnectionStatus, string> = {
  connecting: "connecting…",
  connected: "connected",
  disconnected: "disconnected — retrying…",
};

export default function StatusBanner({ status, url }: Props) {
  return (
    <div className="status">
      {LABELS[status]}
      {status === "connected" ? ` — ${url}` : ""}
    </div>
  );
}
