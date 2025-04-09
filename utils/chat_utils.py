import streamlit as st

def init_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

def clear_chat_history():
    if st.session_state.get("messages"):
        st.session_state.chat_history.append({
            "title": f"Chat {len(st.session_state.chat_history) + 1}",
            "message": st.session_state.messages
        })
    st.session_state.messages = []

def load_chat_history(index):
    st.session_state.messages = st.session_state.chat_history[index]["message"]
