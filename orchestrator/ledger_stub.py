import hashlib
import json
import time

def record_action(action_json: dict) -> dict:
    """
    Simulate immutable ledger recording.
    In production, this would write to blockchain or append-only log.
    """
    # Create a hash of the action for immutability
    evidence_str = json.dumps(action_json, sort_keys=True)
    evidence_hash = hashlib.sha256(evidence_str.encode()).hexdigest()

    entry = {
        "timestamp": time.time(),
        "action": action_json,
        "evidence_hash": evidence_hash
    }

    print(f"[Ledger] Recorded action with hash {evidence_hash}")
    return {"status": "ok", "entry": entry}
