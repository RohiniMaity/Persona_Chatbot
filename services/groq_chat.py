import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from services.prompt import get_prompt
from dotenv import load_dotenv

load_dotenv()

def get_llm(model_name, temperature, max_tokens):
    return ChatGroq(
        temperature=temperature,
        groq_api_key=os.environ.get('GROQ_API_KEY'),
        model_name=model_name,
        max_tokens=max_tokens
    )
    return llm

def get_parser():
    outputparser = StrOutputParser()
    return outputparser


def invoke_model(query, params):
    # Compile history string
    history = ""
    for pair in st.session_state.get("messages", []):
        history += f"{pair['role'].capitalize()}: {pair['content']}\n"

    chain = get_prompt() | get_llm(model_name=params['model_name'],temperature=params['temperature'],max_tokens=params['max_tokens']) | get_parser()

    return chain.invoke({
        "persona": params['persona'],
        "query": query,
        "persona_description": params['persona_description'],
        "chat_sample": params['chat_sample'],
        "chat_history": history
    })
