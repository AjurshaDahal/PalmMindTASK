from app.services.llm_service import generate_answer


prompt = "Explain Python in two simple sentences."

answer = generate_answer(prompt)

print("=== LLM RESPONSE ===")
print(answer)
