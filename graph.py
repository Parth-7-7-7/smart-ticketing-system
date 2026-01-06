from typing import TypedDict, List
from langgraph.graph import StateGraph
from utils.logger import log_ticket
from agents.intake import ticket_intake
from agents.classifier import classify_intent
from agents.priority import assign_priority
from agents.knowledge import retrieve_knowledge
from agents.response import generate_response
from agents.escalation import decide_action



# STATE DEFINITION

class TicketState(TypedDict):
    subject: str
    description: str
    customer_tier: str
    intent: str
    confidence: float
    priority: str
    sla_hours: int
    knowledge: List[str]
    draft_response: str
    final_action: str



# SAFE RESPONSE NODE

def response_node(state: TicketState) -> TicketState:
    return generate_response(state)

def logging_node(state: TicketState) -> TicketState:
    log_ticket(state)
    return state


# LANGGRAPH BUILD

builder = StateGraph(TicketState)

builder.add_node("intake", ticket_intake)
builder.add_node("classify", classify_intent)
builder.add_node("priority", assign_priority)
builder.add_node("knowledge", retrieve_knowledge)
builder.add_node("response", response_node)
builder.add_node("escalation", decide_action)
builder.add_node("logging", logging_node)


builder.set_entry_point("intake")

builder.add_edge("intake", "classify")
builder.add_edge("classify", "priority")
builder.add_edge("priority", "knowledge")
builder.add_edge("knowledge", "response")
builder.add_edge("response", "escalation")
builder.add_edge("escalation", "logging")


graph_app = builder.compile()



# GRAPH RUNNER

def run_graph(ticket_data: dict) -> dict:
    initial_state: TicketState = {
        "subject": ticket_data["subject"],
        "description": ticket_data["description"],
        "customer_tier": ticket_data["customer_tier"],

        # AI-generated fields
        "intent": "",
        "confidence": 0.0,
        "priority": "",
        "sla_hours": 0,
        "knowledge": [],
        "draft_response": "",
        "final_action": ""
    }

    return graph_app.invoke(initial_state)
