from typing import Dict
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2:3b",
    base_url="http://host.docker.internal:11434",
    temperature=0
)

def generate_response(state: Dict) -> Dict:
    prompt = f"""
You are a smart SaaS support assistant.

Ticket:
Subject: {state['subject']}
Description: {state['description']}

Detected Intent: {state.get('intent', 'general')}

Write a clear, professional, and helpful response.
"""

    response = llm.invoke(prompt)
    state["draft_response"] = response.content
    return state
