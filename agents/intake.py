def ticket_intake(state):
    state["subject"] = state["subject"].strip()
    state["description"] = state["description"].strip()
    return state
