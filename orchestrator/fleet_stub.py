def reroute_vehicle(vehicle_id: str, new_route: str) -> dict:
    """
    Simulate rerouting a vehicle.
    In production, this would call the carrier/fleet API.
    """
    print(f"[Fleet] Rerouting {vehicle_id} via {new_route}")
    return {
        "status": "ok",
        "vehicle_id": vehicle_id,
        "new_route": new_route
    }
