import json
from datetime import datetime
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "tickets.log"


def log_ticket(state: dict):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "subject": state.get("subject"),
        "description": state.get("description"),
        "intent": state.get("intent"),
        "confidence": state.get("confidence"),
        "priority": state.get("priority"),
        "sla_hours": state.get("sla_hours"),
        "final_action": state.get("final_action"),
        "draft_response": state.get("draft_response"),
        "customer_tier": state.get("customer_tier"),
    }

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry) + "\n")
