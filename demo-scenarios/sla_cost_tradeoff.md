# Demo Scenario: SLA Cost Tradeoff

**Telemetry Input**  
- Vehicle `truck_7` delayed 3 hours due to congestion.  

**RAG Retrieval**  
- `contract_1`: $500 per hour penalty beyond SLA.  

**Agent Decision**  
```json
{
  "action_type": "reroute",
  "target": "truck_7",
  "params": {"new_route": "Expressway"},
  "reason": "Reroute avoids 5‑hour penalty but adds $2000 cost",
  "rag_refs": ["contract_1"],
  "evidence_hash": "sha256:efgh5678",
  "requires_approval": true
}
