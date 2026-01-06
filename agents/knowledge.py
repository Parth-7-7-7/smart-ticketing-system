def retrieve_knowledge(state):
    try:
        with open("data/knowledge_base.txt", encoding="utf-8") as f:
            kb = f.read()
        state["knowledge"] = [kb[:500]]
    except FileNotFoundError:
        state["knowledge"] = []
    return state
