from ollama import chat


MODEL_NAME = "llama3.2:3b"


def generate_answer(
    prompt: str,
) -> str:
    response = chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response.message.content


def generate_json(
    prompt: str,
) -> str:
    response = chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        format="json",
    )

    return response.message.content
