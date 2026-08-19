import WorldCanvas from "./components/WorldCanvas";
import StatusBanner from "./components/StatusBanner";
import { useWorldSocket } from "./hooks/useWorldSocket";

const WS_URL = import.meta.env.VITE_WS_URL ?? "ws://localhost:8000/ws";

export default function App() {
  const { world, status } = useWorldSocket(WS_URL);

  return (
    <div className="app">
      <header>
        <h1>SOLUM</h1>
        <p>One Island. Twenty Lives. Infinite Outcomes.</p>
      </header>

      <WorldCanvas world={world} />
      <StatusBanner status={status} url={WS_URL} />
    </div>
  );
}