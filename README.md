
# 🤖 Persona Chatbot

**Persona Chatbot** is an interactive Streamlit-based application that allows users to chat with different fictional or custom personas. It uses the **Groq API** to provide fast, powerful language model completions, and **LangChain** to build prompt pipelines and structure the chat logic.

---

## 🧠 Features

- 🔥 Chat with popular fictional characters like **Harry Potter**, **Shrek**, **Batman**, and more.
- 🧩 Create your own **Custom Persona** with a description and sample dialog.
- 🧾 View and load **chat history** from previous conversations.
- ⚙️ Customize the **model**, **temperature**, and **max tokens** for response generation.
- ⚡ Built with **LangChain** prompt chaining and Groq’s blazing-fast LLMs.

---

## 📁 Project Structure

```
persona_bot/
├── main.py                 # Main Streamlit app
├── components/
│   ├── sidebar.py          # UI for sidebar with persona options and settings
│   ├── chat_display.py     # Renders messages in the chat interface
├── services/
│   ├── groq_chat.py        # Handles LLM invocation using Groq API
│   ├── prompt.py           # Defines the persona-specific prompt template
├── utils/
│   ├── chat_utils.py       # Utilities to manage session state and chat history
├── .env                    # Stores API keys securely
├── requirements.txt        # Python dependencies
└── README.md               # Documentation
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/persona-chatbot.git
cd persona-chatbot
```

### 2. Create and Activate a Virtual Environment

```bash
conda create -n langchain-RAG python=3.10
conda activate langchain-RAG
```

Or with `venv`:

```bash
python -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> This will install `streamlit`, `langchain`, `langchain-groq`, `python-dotenv`, etc.

---

### 4. Add Your API Key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your-groq-api-key-here
```

You can get a free API key from [groq.com](https://console.groq.com/).

---

### 5. Run the Application

```bash
streamlit run main.py
```

This will open the chatbot interface in your browser at `http://localhost:8501`.

---

## 🧩 How It Works

### Prompt Template

The core of the persona interaction is a dynamic **prompt template** that includes:

- Persona name
- Persona description
- Sample conversation style
- Chat history
- User query

This prompt ensures that the response aligns with the chosen persona’s behavior and tone.

```jinja2
You are {persona}. You will respond to the user based on how your persona will in reality.

Your Description:
{persona_description}

Chat Sample:
{chat_sample}

Here is a history of the chat
{chat_history}

User: {query}
{persona}:
```

---

### Chat History

- Each new conversation is stored in `st.session_state['chat_history']`.
- Chats can be saved, named, and reloaded from the sidebar.
- Only session-based persistence is currently implemented.

---

## 🧰 Customization Tips

- Want persistent history across sessions? Add file/database storage in `chat_utils.py`.
- Want to change LLM models? Modify the `model_name` dropdown in `sidebar.py`.
- Want better prompt control? Tune the structure in `prompt.py`.

---

## 🔐 Security Note

Never commit your `.env` file to version control. You can add this line to your `.gitignore`:

```bash
.env
```

---

## 💡 Future Improvements

- ✅ Export chat logs to markdown or PDF
- ⏳ Add memory support with LangChain Agents
- 🧠 Connect to external knowledge bases using RAG
- 🌍 Multi-language support for personas

---

## 🙋‍♀️ Author

**Rohini Maity**  
Built with ❤️ using Python, LangChain, and Streamlit.

---

## 📝 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
