from langchain_core.prompts import PromptTemplate

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
    return PromptTemplate.from_template(template)
