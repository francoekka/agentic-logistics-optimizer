import React from "react";
import MapView from "./components/MapView";
import DecisionTimeline from "./components/DecisionTimeline";
import RAGCitations from "./components/RAGCitations";
import LedgerViewer from "./components/LedgerViewer";

function App() {
  return (
    <div>
      <h1>Agentic Logistics Optimizer Dashboard</h1>
      <MapView />
      <DecisionTimeline />
      <RAGCitations />
      <LedgerViewer />
    </div>
  );
}

export default App;
