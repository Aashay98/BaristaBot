import streamlit as st
from langgraph.graph import StateGraph
from barista_bot import graph_with_order_tools  # import your compiled graph
from langchain_core.messages import HumanMessage
import uuid

st.set_page_config(page_title="BaristaBot ☕", layout="centered")

# Session ID
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

st.title("BaristaBot ☕")
st.caption("Welcome to your AI-powered coffee assistant!")

# Message history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat input
user_input = st.chat_input("Place your order or ask about the menu...")

# Display message history
for msg in st.session_state.messages:
    role = "👤 You" if msg.role == "user" else "🤖 BaristaBot"
    st.markdown(f"**{role}:** {msg.content}")

if user_input:
    st.session_state.messages.append(HumanMessage(content=user_input))
    with st.spinner("Thinking..."):
        state = graph_with_order_tools.invoke({
            "messages": st.session_state.messages,
            "order": [],
            "finished": False,
            "session_id": st.session_state.session_id,
        })
        st.session_state.messages.extend(state["messages"])
        st.rerun()
