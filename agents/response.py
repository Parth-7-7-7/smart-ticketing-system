from typing import Dict
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2:3b",
    base_url="http://host.docker.internal:11434",
    temperature=0
)

def generate_response(state: Dict) -> Dict:
    knowledge = "\n".join(state.get("knowledge", []))

    prompt = f"""
You are a smart SaaS support assistant.

Use the following knowledge base if relevant:
{knowledge}

Ticket:
Subject: {state['subject']}
Description: {state['description']}

Detected Intent: {state.get('intent', 'general')}

Rules:
- If knowledge is relevant, use it
- If not, respond normally
- Be clear and professional
"""

    response = llm.invoke(prompt)
    state["draft_response"] = response.content
    return state
