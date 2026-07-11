# Demo Scenario: Security Quarantine

**Telemetry Input**  
- Warehouse `WH_Mumbai` DPI flags suspicious outbound flow.  

**RAG Retrieval**  
- `policy_2`: Suspicious flows must be quarantined immediately.  

**Agent Decision**  
```json
{
  "action_type": "quarantine",
  "target": "flow_99",
  "params": {"rule": "block outbound"},
  "reason": "Suspicious flow detected by DPI",
  "rag_refs": ["policy_2"],
  "evidence_hash": "sha256:ijkl9012",
  "requires_approval": false
}
