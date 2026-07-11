def quarantine_flow(flow_id: str, reason: str) -> dict:
    """
    Simulate quarantining a suspicious network flow.
    In production, this would push firewall/DPI rules.
    """
    print(f"[Quarantine] Flow {flow_id} quarantined. Reason: {reason}")
    return {
        "status": "ok",
        "flow_id": flow_id,
        "reason": reason
    }
