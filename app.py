import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from graph import run_graph

st.title("🎫 Smart Ticketing System")

subject = st.text_input("Subject")
description = st.text_area("Description")
customer_tier = st.selectbox("Customer Tier", ["Free", "Paid"])

if st.button("Submit Ticket"):
    if not subject or not description:
        st.warning("Please fill in subject and description.")
    else:
        ticket_data = {
            "subject": subject,
            "description": description,
            "customer_tier": customer_tier
        }

        result = run_graph(ticket_data)

        st.subheader("🧠 AI Decision Summary")

        st.write(f"**Category:** {result.get('intent', 'N/A')}")
        st.write(f"**Priority:** {result.get('priority', 'N/A')}")
        st.write(f"**SLA (hours):** {result.get('sla_hours', 'N/A')}")

        confidence = result.get("confidence", 0)

        if confidence >= 0.7:
            st.success(f"Confidence: {round(confidence * 100, 2)}%")
        elif confidence >= 0.5:
            st.warning(f"Confidence: {round(confidence * 100, 2)}%")
        else:
            st.error(f"Confidence: {round(confidence * 100, 2)}%")

        st.subheader("💬 Suggested Response")
        st.write(result.get("draft_response", ""))

        st.subheader("🚦 Final Action")

        if result.get("final_action") == "AUTO_REPLY":
            st.success("✅ Auto Reply Sent")
            st.info("📄 Ticket logged successfully")
        else:
            st.error("🧑 Escalated to Human Support")
            st.info("📄 Ticket logged successfully")



