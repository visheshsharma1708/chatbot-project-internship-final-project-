from langgraph.graph import StateGraph, END
from utils.model_loader import get_llm
from Agents.tech_agent import handle_tech_question
from Agents.nontech_agent import handle_nontech_question
from Agents.general_agent import handle_general_question
from langchain_core.runnables import RunnableLambda

llm = get_llm()

class ChatState(dict):
    question: str
    response: str
    intent: str

def classify_intent(state: ChatState) -> ChatState:
    q = state["question"].lower()
    if any(word in q for word in ["python", "code", "ai", "ml", "data", "programming"]):
        state["intent"] = "tech"
    elif any(word in q for word in ["movie", "travel", "news", "food"]):
        state["intent"] = "general"
    else:
        state["intent"] = "nontech"
    return state

def tech_node(state: ChatState) -> dict:
    return {"response": handle_tech_question(state["question"], llm)}

def nontech_node(state: ChatState) -> dict:
    return {"response": handle_nontech_question(state["question"], llm)}

def general_node(state: ChatState) -> dict:
    return {"response": handle_general_question(state["question"], llm)}

builder = StateGraph(ChatState)
builder.add_node("classifier", RunnableLambda(classify_intent))
builder.add_node("tech_node", RunnableLambda(tech_node))
builder.add_node("nontech_node", RunnableLambda(nontech_node))
builder.add_node("general_node", RunnableLambda(general_node))

builder.set_entry_point("classifier")
builder.add_conditional_edges(
    "classifier",
    lambda state: state["intent"],
    {
        "tech": "tech_node",
        "nontech": "nontech_node",
        "general": "general_node"
    }
)

builder.add_edge("tech_node", END)
builder.add_edge("nontech_node", END)
builder.add_edge("general_node", END)

graph = builder.compile()

def get_bot_response(user_input: str) -> str:
    """
    This function is called from the Streamlit UI (app.py)
    It sends the user input through the graph and returns the bot's response.
    """
    try:
        result = graph.invoke({"question": user_input})
        return result.get("response", "Sorry, I couldn't generate a response.")
    except Exception as e:
        return f" Error: {str(e)}"


if __name__ == "__main__":
    input_question = "tell me about Jeff Bezos and his company"
    print("Bot Response:", get_bot_response(input_question))
