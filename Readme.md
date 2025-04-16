# ☕ BaristaBot – AI-Powered Cafe Assistant

BaristaBot is an interactive AI cafe assistant built using LangGraph, LangChain, and Google Gemini. It enables users to place, modify, confirm, and submit cafe orders through natural conversation.

Designed with clean stateful architecture and tool-driven logic, BaristaBot simulates a real-world ordering experience while showcasing the capabilities of modern LLMs in a web-based chatbot interface.

---

## 📦 Features

- 🔄 **Session-Based Order Tracking**
Track user-specific orders across conversations using persistent UUID-based session IDs.

- 📜 **Menu Navigation & Modifier Handling**
Users can explore the menu and customize drinks with validated modifiers (milk type, caffeine level, etc.).

- 📡 **LLM-Powered Intelligence**
Uses Google Gemini 2.0 Flash to understand user intent, handle corrections, and respond fluidly in conversation.

- 📋 **Order Confirmation & ETA Generation**
Orders are summarized and confirmed before being submitted with a simulated kitchen ETA.

- 🧠 **LangGraph-Powered State Management**
Finite state machine architecture manages tool invocation, memory, routing, and conversational flow.

- 🌈 **Streamlit Chat UI**
Clean chat interface with st.chat_input() for live user interaction and real-time responses.

- 🧾 **PDF Receipt Generation**
Automatically generates a receipt with itemized order and estimated pickup time.

- 📊 **Analytics Logging**
Session data is logged locally in structured JSON for usage tracking and analysis.

- 🐳 **Docker-Ready**
Containerized environment for local development and production deployment.

---

## 🧠 Concepts Used
BaristaBot demonstrates several foundational AI system design concepts:

- 🧩 **Modular Tool Architecture**
Each functional unit (add item, clear order, confirm, etc.) is a callable LangChain tool. This follows the command pattern and decouples intent from execution.

- 🧠 **Stateful Agent Design via LangGraph**
LangGraph allows LLMs to act like agents in a finite-state machine, managing both the conversation and order logic with conditional transitions.

- 🧾 **Structured Memory via TypedDict**
A shared state dictionary (TypedDict) stores and passes structured data (messages, order, finished, session_id) across nodes and tools.

- 🔗 **Language Model with Tool Integration**
The Gemini model is bound to external tools, giving it real-world capabilities like interacting with orders and responding with context-aware actions.

- 🧪 **Session Persistence with UUID**
Each user interaction is isolated via unique session IDs, ensuring independent and stateful order tracking even across reruns or threads.

- 🖼️ **UI-State Sync with Streamlit**
The app uses Streamlit's session_state to sync chat input/output and trigger reruns — mimicking client-server reactivity.

- 📑 **PDF Generation via FPDF**
A simple PDF generation module turns order data into receipts, highlighting structured output generation from dynamic user input.

- 🧾 **Logging & Audit Trail**
Every session is recorded as a .json file, enabling analytics, bug tracking, and potential order playback or future training datasets.

---

## 📁 Project Structure

baristabot/ 
├── app.py # Streamlit UI 
├── tools.py # All tool functions (get_menu, add_to_order, etc.) 
├── graph.py # LangGraph logic, state machine definition 
├── requirements.txt # Python dependencies 
├── Dockerfile # Docker setup 
├── .dockerignore └── README.md

---

## 🚀 Quick Start

### 🔧 1. Clone the Repo
```bash
git clone https://github.com/yourusername/baristabot.git
cd baristabot
```

### 🧪 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 🔑 3. Set API Key
You need a Google Gemini API Key
Add this to your environment:
```bash
export GOOGLE_API_KEY=your_key_here
```

### ▶️ 4. Run Streamlit Locally
```bash
streamlit run app.py
```
Now open http://localhost:8501 in your browser.

## 🐳 Docker Deployment
### 📦 Build
```bash
docker build -t baristabot .
```

### 🚀 Run
```bash
docker run -p 8501:8501 -e GOOGLE_API_KEY=your_key_here baristabot
```
Visit http://localhost:8501 in browser.


## ☁️ Deploy on Streamlit Cloud
1. Push code to GitHub

2. Go to streamlit.io/cloud

3. Connect your repo

4. Set GOOGLE_API_KEY in Secrets Manager

5. Deploy!

## 🧠 Powered By
LangGraph

LangChain

Google Gemini API

Streamlit

Docker

## 💡 Future Enhancements
✅ Dropdown-based UI for drinks & modifiers

✅ Admin dashboard to view & manage orders

✅ Persistent database storage (e.g., Redis or SQLite)

✅ Multimodal order input (image of chalkboard menu)

## 🤝 Contributing
Pull requests welcome. For major changes, please open an issue first.


