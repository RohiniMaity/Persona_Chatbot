import streamlit as st
from utils.chat_utils import clear_chat_history, load_chat_history

def show_sidebar():
    with st.sidebar:
        st.header("🧠 Persona Controls")

        persona = st.selectbox("Select a persona", ["Harry Potter", "Shrek", "Star Wars", "Batman", "Custom Persona"], index=0)
        persona_description, chat_sample = "", ""
        if persona == "Custom Persona":
            persona = st.text_input("Enter a custom persona")
            persona_description = st.text_area("Enter a description for the custom persona")
            chat_sample = st.text_area("Enter a chat sample for the custom persona")

        if st.button("➕ New Chat"):
            clear_chat_history()

        temperature = st.slider("Temperature", 0.0, 1.0, 0.8, 0.1)
        max_tokens = st.slider("Max Tokens", 1024, 4096, 2048, 1024)
        model_name = st.selectbox("Model", ["llama3-8b-8192", "deepseek-r1-distill-qwen-32b", "gemma2-9b-it", "llama3-70b-8192", "whisper-large-v3"])
        
        st.write(f"You are talking to **{persona}**")

        if 'chat_history' in st.session_state and len(st.session_state['chat_history']) > 0:
            st.markdown("### 📜 Previous Chats")
            for i, chat in enumerate(st.session_state['chat_history']):
                if st.button(chat['title'], key=f"chat_{i}"):
                    load_chat_history(i)

    return {
        "temperature": temperature,
        "max_tokens": max_tokens,
        "model_name": model_name,
        "persona": persona,
        "persona_description": persona_description,
        "chat_sample": chat_sample
    }
