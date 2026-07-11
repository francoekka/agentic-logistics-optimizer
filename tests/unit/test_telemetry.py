import json
import jsonschema
from pathlib import Path

def test_vehicle_schema_valid():
    schema = json.load(open("telemetry-simulator/data_schemas/vehicle_schema.json"))
    sample = {
        "vehicle_id": "truck_12",
        "timestamp": "2026-07-11T20:38:00",
        "gps": {"lat": 19.076, "lon": 72.877},
        "speed_kmh": 58
    }
    jsonschema.validate(sample, schema)

def test_warehouse_schema_valid():
    schema = json.load(open("telemetry-simulator/data_schemas/warehouse_schema.json"))
    sample = {
        "warehouse_id": "WH_Mumbai",
        "timestamp": "2026-07-11T20:38:00",
        "dock_status": "occupied"
    }
    jsonschema.validate(sample, schema)
