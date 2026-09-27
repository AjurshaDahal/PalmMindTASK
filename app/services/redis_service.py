import redis


redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True,
)


def save_message(
    conversation_id: str,
    role: str,
    content: str,
) -> None:
    key = f"chat:{conversation_id}"

    redis_client.rpush(
        key,
        f"{role}:{content}",
    )


def get_messages(
    conversation_id: str,
) -> list[str]:
    key = f"chat:{conversation_id}"

    return redis_client.lrange(
        key,
        0,
        -1,
    )

import json


def save_booking_state(
    conversation_id: str,
    details: dict,
) -> None:
    key = f"booking:{conversation_id}"

    redis_client.set(
        key,
        json.dumps(details),
    )


def get_booking_state(
    conversation_id: str,
) -> dict:
    key = f"booking:{conversation_id}"

    data = redis_client.get(key)

    if not data:
        return {}

    return json.loads(data)


def clear_booking_state(
    conversation_id: str,
) -> None:
    key = f"booking:{conversation_id}"

    redis_client.delete(key)