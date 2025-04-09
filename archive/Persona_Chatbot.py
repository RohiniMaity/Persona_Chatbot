import streamlit as st
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="Persona Bot", layout="wide")  # Added page config for better layout

st.title("Persona Bot")
st.info("This is a chatbot that can talk to different personas. You can select the persona from the sidebar.")

chat_history = []
history = ""
persona = "Harry Potter"
persona_description = ""
chat_sample = ""

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = chat_history

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

if 'current_chat' not in st.session_state:
    st.session_state['current_chat'] = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


def get_prompt():
    template = '''
    You are {persona}. You will respond to the user based on how your persona will in reality.

    Your Description:
    {persona_description}

    chat sample:
    {chat_sample}

    Here is a history of the chat
    {chat_history}

    User: {query}
    {persona}: 
    '''
    prompt = PromptTemplate.from_template(
        template=template
    )
    return prompt

def get_llm():
    llm = ChatGroq(
        temperature=temperature,
        groq_api_key=os.environ.get('GROQ_API_KEY'),
        model_name=model_name,
        max_tokens=max_tokens
    )
    return llm

def get_parser():
    outputparser = StrOutputParser()
    return outputparser

def invoke(query):
    global history
    global chat_history
    history = ""
    if len(chat_history) != 0:
        for hist in chat_history:
            for key, value in hist.items():
                history += f"{key}: {value}\n"
    response = chain.invoke({
        "persona": persona,
        "query": query,
        "persona_description": persona_description,
        "chat_sample": chat_sample,
        "chat_history": history
    })
    chat_history.append({"User": query, persona: response})
    return response
    
# Save old chat and clear messages
def clear_chat():
    if st.session_state.get("messages"):
        st.session_state['chat_history'].append({
            'title': f"Chat {len(st.session_state['chat_history']) + 1}",
            'message': st.session_state['messages']
        })
    st.session_state['messages'] = []  # Clear current messages

# Load an old chat by index
def load_chat(index):
    st.session_state['messages'] = st.session_state['chat_history'][index]['message']

# SIDEBAR
with st.sidebar:
    st.header("🧠 Persona Controls")
    persona = st.selectbox("Select a persona", ["Harry Potter", "Shrek", "Star Wars", "Batman", "Custom Persona"], index=0)

    st.button("➕ New Chat", on_click=lambda: clear_chat())
    temperature = st.slider("Temperature", 0.0, 1.0, 0.8, 0.1)
    max_tokens = st.slider("Max Tokens", 1024, 4096, 2048, 1024)
    model_name = st.selectbox("Model", [
        "llama3-8b-8192",
        "deepseek-r1-distill-qwen-32b",
        "gemma2-9b-it",
        "llama3-70b-8192",
        "whisper-large-v3"
    ])
    
    if persona == "Custom Persona":
        persona = st.text_input("Enter a custom persona")
        persona_description = st.text_area("Enter a description for the custom persona")
        chat_sample = st.text_area("Enter a chat sample for the custom persona")

    st.write(f"You are talking to {persona}")

    # Display chat history list
    if 'chat_history' in st.session_state and len(st.session_state['chat_history']) > 0:
        st.markdown("### 📜 Previous Chats")
        for i, chat in enumerate(st.session_state['chat_history']):
            if st.button(chat['title'], key=f"chat_{i}"):
                load_chat(i)


# React to user input
if prompt := st.chat_input("What is up?"):
    #Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    #Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    chain = get_prompt() | get_llm() | get_parser()
    response = invoke(query=prompt)

    #Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    #Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})