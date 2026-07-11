from orchestrator import fleet_stub, ledger_stub, quarantine_stub

def test_fleet_reroute():
    result = fleet_stub.reroute_vehicle("truck_1", "NH66")
    assert result["status"] == "ok"

def test_ledger_record():
    action = {"action_type": "reroute", "target": "truck_1"}
    result = ledger_stub.record_action(action)
    assert "entry" in result

def test_quarantine_flow():
    result = quarantine_stub.quarantine_flow("flow_99", "Suspicious DPI flag")
    assert result["status"] == "ok"

