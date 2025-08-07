def handle_general_question(question: str, llm) -> str:
    prompt = f"You are a friendly chatbot. Answer the general question:\n{question}"
    return llm.invoke(prompt)
