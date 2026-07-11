from agent.retrieval_wrapper import RetrievalWrapper
from orchestrator import fleet_stub, ledger_stub

def test_end_to_end_pipeline(tmp_path):
    # Seed retrieval
    rw = RetrievalWrapper(persist_dir=str(tmp_path))
    doc = {"doc_id": "contract_demo", "type": "SLA", "clause": "Delivery within 48h"}
    rw.add_doc(doc)

    # Simulate agent decision
    decision = {
        "action_type": "reroute",
        "target": "truck_12",
        "params": {"new_route": "NH66"},
        "reason": "Predicted delay",
        "rag_refs": ["contract_demo"],
        "evidence_hash": "sha256:demo123",
        "requires_approval": False
    }

    # Orchestrator actions
    fleet_result = fleet_stub.reroute_vehicle(decision["target"], decision["params"]["new_route"])
    ledger_result = ledger_stub.record_action(decision)

    assert fleet_result["status"] == "ok"
    assert ledger_result["status"] == "ok"
