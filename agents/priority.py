def assign_priority(state):
    if state["intent"] == "Security":
        state["priority"] = "P0"
        state["sla_hours"] = 2
    elif state["intent"]=="technical":
        state["priority"] = "P1"
        state["sla_hours"] = 8
    elif state["intent"]=="refund":
        state["priority"] = "P2"
        state["sla_hours"] = 24    
    elif state["customer_tier"] == "Enterprise" and state["intent"] == "Bug":
        state["priority"] = "P0"
        state["sla_hours"] = 2
    elif state["intent"] == "account":
        state["priority"] = "P1"
        state["sla_hours"] = 8
    elif state["intent"] == "Billing":
        state["priority"] = "P2"
        state["sla_hours"] = 24
    else:
        state["priority"] = "P3"
        state["sla_hours"] = 72
    return state
