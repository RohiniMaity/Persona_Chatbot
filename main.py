import streamlit as st
from components.sidebar import show_sidebar
from components.chat_display import display_messages
from services.groq_chat import invoke_model
from utils.chat_utils import init_session_state, clear_chat_history

# Load session state vars
init_session_state()

# Set Streamlit UI
st.set_page_config(page_title="Persona Bot", layout="wide")
st.title("Persona Bot")
st.info("This is a chatbot that can talk to different personas. You can select the persona from the sidebar.")

# Render sidebar and get parameters
params = show_sidebar()

# Display existing messages
display_messages(st.session_state.messages)

# Handle user input
if prompt := st.chat_input("What is up?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = invoke_model(prompt, params)
    st.chat_message("assistant").markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
