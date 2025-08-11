import streamlit as st
from langgraph_module import get_bot_response
st.set_page_config(page_title="NeoMind AI", page_icon="🤖", layout="wide")
st.title("🤖 NeoMind AI")
st.write("Ask me anything — tech, general, or creative!")
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []  
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**NeoMind:** {msg['content']}")

st.divider()


user_input = st.chat_input("Type your message and press Enter...")

if user_input:

    st.session_state["messages"].append({"role": "user", "content": user_input})
    with st.spinner("Thinking..."):
        bot_reply = get_bot_response(user_input)
    st.session_state["messages"].append({"role": "assistant", "content": bot_reply})
    st.rerun()
