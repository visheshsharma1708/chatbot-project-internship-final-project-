# app.py
import streamlit as st
from langgraph_module import get_bot_response

# Page config
st.set_page_config(page_title="NeoMind AI", page_icon="🤖", layout="wide")

# Header
st.title("🤖 NeoMind AI")
st.write("Ask me anything — tech, general, or creative!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []  # Each message: {"role": "user"/"assistant", "content": str}

# Display previous messages
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**NeoMind:** {msg['content']}")

st.divider()

# Chat input — sends automatically when pressing Enter
user_input = st.chat_input("Type your message and press Enter...")

if user_input:
    # Add user message
    st.session_state["messages"].append({"role": "user", "content": user_input})

    # Show processing indicator while bot responds
    with st.spinner("Thinking..."):
        bot_reply = get_bot_response(user_input)

    # Add bot reply
    st.session_state["messages"].append({"role": "assistant", "content": bot_reply})

    # Refresh to show new messages
    st.rerun()
