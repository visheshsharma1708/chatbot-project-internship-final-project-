def handle_tech_question(question: str, llm) -> str:
    prompt = f"You are a tech assistant. Answer the following technical question:\n{question}"
    return llm.invoke(prompt)
