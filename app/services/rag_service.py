from sqlalchemy.orm import Session

from app.services.llm_service import generate_answer
from app.services.redis_service import get_messages, save_message
from app.services.search_service import search_similar_chunks


def build_context(
    question: str,
    db: Session,
    top_k: int = 3,
) -> str:
    results = search_similar_chunks(
        query=question,
        db=db,
        top_k=top_k,
    )

    context_parts = []

    for result in results:
        chunk_text = result.payload.get("chunk_text")

        if chunk_text:
            context_parts.append(chunk_text)

    return "\n\n".join(context_parts)


def answer_question(
    question: str,
    db: Session,
    conversation_id: str,
    top_k: int = 3,
) -> str:
    history = get_messages(conversation_id)

    context = build_context(
        question=question,
        db=db,
        top_k=top_k,
    )

    history_text = "\n".join(history)

    prompt = f"""
You are a document question-answering assistant.

Use the provided document context to answer the user's question.

You may also use the conversation history to understand
references such as "it", "that", "those", or "the previous answer".

Do not invent information.

If the answer cannot be found in the provided documents,
say:
"I couldn't find that information in the provided documents."

Conversation history:
{history_text}

Document context:
{context}

Current question:
{question}
"""

    answer = generate_answer(prompt)

    save_message(
        conversation_id,
        "user",
        question,
    )

    save_message(
        conversation_id,
        "assistant",
        answer,
    )

    return answer
