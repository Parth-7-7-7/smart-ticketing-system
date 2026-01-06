def decide_action(state):
    confidence = state.get("confidence", 0)
    priority = state.get("priority", "P3")
    tier = state.get("customer_tier", "Free")

    # 🚦 STRICT ESCALATION RULES
    if (
        confidence < 0.6
        or priority in ["P0", "P1"]
        or tier == "Paid"
    ):
        state["final_action"] = "HUMAN_REVIEW"
    else:
        state["final_action"] = "AUTO_REPLY"

    return state
