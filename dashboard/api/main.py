from fastapi import FastAPI

app = FastAPI()

@app.get("/telemetry")
def get_telemetry():
    return {"vehicle_id": "truck_12", "speed_kmh": 58, "gps": {"lat": 19.076, "lon": 72.877}}

@app.get("/decisions")
def get_decisions():
    return [{
        "action_type": "reroute",
        "target": "truck_12",
        "params": {"new_route": "NH66"},
        "reason": "Predicted delay due to NH48 closure",
        "rag_refs": ["contract_1", "incident_1"],
        "evidence_hash": "sha256:abcd1234",
        "requires_approval": False
    }]

@app.get("/ledger")
def get_ledger():
    return [{"timestamp": 1720720000, "hash": "sha256:abcd1234"}]
