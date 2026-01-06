from typing import Dict
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
import re

llm = ChatOllama(
    model="llama3.2:3b",
    base_url="http://host.docker.internal:11434",
    temperature=0
)


def is_ambiguous(text: str) -> bool:
    text = text.lower().strip()

    ambiguous_phrases = [
        "something is wrong",
        "need help",
        "problem",
        "issue",
        "not sure",
        "help me",
        "question"
    ]

    if len(text.split()) < 6:
        return True

    for phrase in ambiguous_phrases:
        if phrase in text:
            return True

    return False


def classify_intent(state: Dict) -> Dict:
    combined_text = f"{state['subject']} {state['description']}"

    # 🚨 HARD GUARD FOR AMBIGUITY
    if is_ambiguous(combined_text):
        state["intent"] = "general"
        state["confidence"] = 0.45
        state["reason"] = "Ambiguous or insufficient information"
        return state

    prompt = ChatPromptTemplate.from_template("""
You are a support ticket classifier.

Categories:
- account
- billing
- technical
- refund
- general

Return response strictly in this format:
Category: <category>
Confidence: <number between 0 and 1>

Ticket:
{text}
""")

    response = llm.invoke(
        prompt.format(text=combined_text)
    ).content

    category_match = re.search(r"Category:\s*(\w+)", response, re.IGNORECASE)
    confidence_match = re.search(r"Confidence:\s*([0-9.]+)", response)

    state["intent"] = category_match.group(1).lower() if category_match else "general"
    state["confidence"] = float(confidence_match.group(1)) if confidence_match else 0.5
    state["reason"] = "LLM classified intent"

    return state
