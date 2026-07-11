# Demo Scenario: Predictive Reroute

**Telemetry Input**  
- Vehicle `truck_12` speed drops near NH48.  
- GPS shows proximity to known closure zone.  

**RAG Retrieval**  
- `contract_1`: SLA requires delivery within 48 hours.  
- `incident_1`: NH48 closure caused 6‑hour delay in 2024.  

**Agent Decision**  
```json
{
  "action_type": "reroute",
  "target": "truck_12",
  "params": {"new_route": "NH66"},
  "reason": "Predicted delay due to NH48 closure",
  "rag_refs": ["contract_1", "incident_1"],
  "evidence_hash": "sha256:abcd1234",
  "requires_approval": false
}
