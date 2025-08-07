def handle_nontech_question(question: str, llm) -> str:
    prompt = f"You are a non-tech assistant. Answer in simple words:\n{question}"
    return llm.invoke(prompt)
