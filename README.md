# Smart Ticketing System 🚀

An intelligent LLM-powered support ticket system that automatically:
- Classifies tickets
- Routes to departments
- Calculates confidence score
- Escalates to human agents when needed

Built using **LangGraph**, **Ollama**, and **Streamlit**.

---

## 🔧 Tech Stack
- Python
- LangGraph
- LangChain
- Ollama (Local LLM)
- Streamlit
- Docker

---

## 🧠 Features
- Multi-category intent classification
- Confidence-based escalation logic
- Automated vs Human review decision
- Modular agent-based architecture
- Local LLM inference using Ollama

---

## 📂 Project Structure


# Smart Ticketing System 🚀

An intelligent LLM-powered support ticket system that automatically:
- Classifies tickets
- Routes to departments
- Calculates confidence score
- Escalates to human agents when needed

Built using **LangGraph**, **Ollama**, and **Streamlit**.

---

## 🔧 Tech Stack
- Python
- LangGraph
- LangChain
- Ollama (Local LLM)
- Streamlit
- Docker

---

## 🧠 Features
- Multi-category intent classification
- Confidence-based escalation logic
- Automated vs Human review decision
- Modular agent-based architecture
- Local LLM inference using Ollama

---

## 📂 Project Structure

smart-ticketing-system/
│
├── agents/
│ ├── intent.py
│ ├── confidence.py
│ ├── escalation.py
│ ├── response.py
│
├── graph.py
├── app.py
├── Dockerfile
├── requirements.txt
└── README.md



---

## 🚀 How to Run Locally

### 1️⃣ Install Ollama
https://ollama.com

### 2️⃣ Pull model
```bash
ollama pull llama3.2:3b
ollama serve


docker build -t smart-ticketing-system .
docker run -p 8501:8501 smart-ticketing-system


http://localhost:8501

This project uses local LLM inference via Ollama, so Ollama must be running on the system.
