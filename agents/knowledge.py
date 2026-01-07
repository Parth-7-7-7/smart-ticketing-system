from typing import Dict

def retrieve_knowledge(state: Dict) -> Dict:
    try:
        with open("data/knowledge_base.txt", encoding="utf-8") as f:
            kb = f.read()

        # Simple keyword-based relevance
        text = f"{state['subject']} {state['description']}".lower()

        relevant_chunks = []

        for block in kb.split("\n\n"):
            if any(word in block.lower() for word in text.split()):
                relevant_chunks.append(block)

        # Fallback
        if not relevant_chunks:
            relevant_chunks.append(kb[:500])

        state["knowledge"] = relevant_chunks[:2]

    except Exception:
        state["knowledge"] = []

    return state
