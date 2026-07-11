import time
from agent.retrieval_wrapper import RetrievalWrapper
from orchestrator import fleet_stub, ledger_stub, quarantine_stub

def main():
    print("=== Agentic Logistics Optimizer Demo ===")

    # Step 1: Telemetry input (simulated)
    telemetry = {
        "vehicle_id": "truck_12",
        "speed_kmh": 58,
        "gps": {"lat": 19.076, "lon": 72.877}
    }
    print("\nTelemetry:", telemetry)

    # Step 2: Retrieval
    rw = RetrievalWrapper(persist_dir="demo_index")
    doc = {"doc_id": "contract_demo", "type": "SLA", "clause": "Delivery within 48h"}
    rw.add_doc(doc)
    hits = rw.query("delivery")
    print("\nRetrieved docs:", hits)

    # Step 3: Agent decision (simplified)
    decision = {
        "action_type": "reroute",
        "target": telemetry["vehicle_id"],
        "params": {"new_route": "NH66"},
        "reason": "Predicted delay near NH48",
        "rag_refs": [doc["doc_id"]],
        "evidence_hash": "sha256:demo123",
        "requires_approval": False
    }
    print("\nAgent decision:", decision)

    # Step 4: Orchestrator actions
    fleet_result = fleet_stub.reroute_vehicle(decision["target"], decision["params"]["new_route"])
    ledger_result = ledger_stub.record_action(decision)

    print("\nFleet result:", fleet_result)
    print("Ledger result:", ledger_result)

    # Step 5: Dashboard stub output
    print("\n=== Dashboard View ===")
    print("Map: reroute truck_12 → NH66")
    print("Timeline: decision logged with citations")
    print("Ledger entry:", ledger_result)

if __name__ == "__main__":
    main()
