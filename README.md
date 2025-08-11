🤖 NeoMind AI — Intelligent Chatbot with LangChain, LangGraph & Streamlit
Author: Vishesh Sharma

📌 Overview
NeoMind AI is an intelligent chatbot built using LangChain, LangGraph, and Streamlit.
It can answer technical, non-technical, and general questions by automatically detecting the user’s intent and routing the query to the right agent.

The chatbot uses Ollama’s LLaMA 3 model for generating responses, and a state graph (via LangGraph) to manage the conversation flow.

🚀 Features
✅ Multi-Intent Understanding — Classifies questions into Tech, Non-Tech, or General automatically.
✅ Agent-Based Architecture — Each type of query is handled by a dedicated AI agent.
✅ LLM Powered — Uses LLaMA 3 through Ollama for high-quality answers.
✅ Interactive UI — Built with Streamlit for a smooth chat interface.
✅ Extensible — Easily add more agents or modify intent classification rules.

🛠 Tech Stack
Python 3.10+

LangChain — LLM orchestration

LangGraph — Graph-based flow control

Ollama — Local LLaMA 3 model

Streamlit — Web UI

Custom Agents — For intent-specific responses

📂 Project Structure
graphql
Copy
Edit
NeoMind_AI/
│
├── utils/
│   └── model_loader.py         # Loads the LLaMA 3 model
│
├── Agents/
│   ├── tech_agent.py           # Handles technical questions
│   ├── nontech_agent.py        # Handles non-technical questions
│   └── general_agent.py        # Handles general queries
│
├── langgraph_module.py         # Manages chatbot flow using LangGraph
│
├── app.py                      # Streamlit UI for the chatbot
│
├── README.md                   # Project documentation
└── requirements.txt            # Dependencies
⚙️ How It Works
1️⃣ Model Loader (utils/model_loader.py)
Loads the Ollama LLaMA 3 model with a specific temperature setting for balanced creativity and accuracy.

2️⃣ Agents (Agents/)
Tech Agent — Answers programming, AI, ML, and data-related queries.

Non-Tech Agent — Handles everyday questions in simple language.

General Agent — Responds to casual, friendly, and general topics.

3️⃣ LangGraph Pipeline (langgraph_module.py)
Classifier Node — Detects user intent based on keywords.

Routing — Directs question to the correct agent node.

Response Node — Generates and returns the AI's answer.

4️⃣ Streamlit UI (app.py)
Displays a chat interface where the user can interact with the bot.

Maintains chat history for the current session.

📦 Installation & Setup
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/visheshsharma1708/chatbot-project-internship-final-project-
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Install & Run Ollama (for LLaMA 3)
Follow Ollama's installation guide: https://ollama.ai
Then, pull the LLaMA 3 model:

bash
Copy
Edit
ollama pull llama3
4. Run the App
bash
Copy
Edit
streamlit run app.py
💡 Example Interaction
You: "Explain Python decorators"
NeoMind: "A Python decorator is a function that modifies another function without changing its code..."

You: "What's the latest news about space exploration?"
NeoMind: "Recently, NASA announced plans for a new mission to..."

📚 Future Improvements
 Add database support to store chat history permanently.

 Integrate APIs for real-time information (e.g., news, weather).

 Implement voice-based input/output.

 Enhance intent classification using NLP models instead of keyword matching.

👨‍💻 Author
Vishesh Sharma
AI/ML Developer | Python Enthusiast | Problem Solver

📧 svishesh1708@gmail.com

📜 License
This project is licensed under the MIT License — feel free to use and modify with attribution.

