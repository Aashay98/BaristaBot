# ☕ BaristaBot – AI-Powered Cafe Assistant

BaristaBot is an interactive AI assistant built using LangGraph, LangChain, and Google Gemini. It takes customer orders, modifies them, confirms, and sends them to a virtual cafe. The app runs on a conversational Streamlit frontend and supports session-based order tracking via a unique session ID. Perfect for virtual cafes, chatbot showcases, or applied LLM demonstrations.

---

## 🌐 Live Demo (Streamlit Cloud)
> [Click to try the demo](https://your-streamlit-link.streamlit.app)  
*(Update this with your deployed URL)*

---

## 📦 Features

- 🔄 **Session-based order tracking**
- 📜 **Menu navigation and modifier handling**
- 📡 **Google Gemini 2.0 Flash LLM integration**
- 📋 **Order confirmation and ETA estimation**
- 🧠 **LangGraph-powered logic for memory & tools**
- 🌈 **Streamlit frontend for live interaction**
- 🐳 **Dockerized for easy deployment**

---

## 📁 Project Structure

baristabot/ ├── app.py # Streamlit UI ├── tools.py # All tool functions (get_menu, add_to_order, etc.) ├── graph.py # LangGraph logic, state machine definition ├── requirements.txt # Python dependencies ├── Dockerfile # Docker setup ├── .dockerignore └── README.md

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