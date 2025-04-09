import streamlit as st

def display_messages(messages):
    for message in messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
