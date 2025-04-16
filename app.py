import os
from reciept import generate_pdf
import streamlit as st
from agent import graph_with_order_tools
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
    if role == "👤 You":
        st.chat_message("user").markdown(msg.content)
    elif role == "🤖 BaristaBot":
        st.chat_message("assistant").markdown(msg.content)
    else:  # Tool
        with st.expander("🛠 Tool Response"):
            st.markdown(msg.content)

if user_input:
    st.session_state.messages.append(HumanMessage(content=user_input))
    with st.spinner("Thinking..."):
        state = graph_with_order_tools.invoke(
            {
                "messages": st.session_state.messages,
                "order": [],
                "finished": False,
                "session_id": st.session_state.session_id,
            }
        )
        if state.get("finished", False):
            st.success("✅ Order placed! Your order is being prepared.")

            order_items = state.get("order", [])
            eta = next((msg.content for msg in state["messages"] if "ETA" in str(msg.content)), "N/A")

            pdf_path = generate_pdf(order_items, eta, st.session_state.session_id)

            with open(pdf_path, "rb") as f:
                st.download_button(
                    label="📄 Download Receipt (PDF)",
                    data=f,
                    file_name=os.path.basename(pdf_path),
                    mime="application/pdf"
                )

            if st.button("Start New Order"):
                st.session_state.messages = []
                st.session_state.session_id = str(uuid.uuid4())
                st.rerun()
        st.session_state.messages.extend(state["messages"])
        st.rerun()
