import base64


def encode_verify_slug(user_id: int, token: str) -> str:
    payload = f"{int(user_id)}:{token}".encode("utf-8")
    return base64.urlsafe_b64encode(payload).decode("utf-8").rstrip("=")



def decode_verify_slug(slug: str):
    try:
        padded = slug + "=" * (-len(slug) % 4)
        decoded = base64.urlsafe_b64decode(padded.encode("utf-8")).decode("utf-8")
        user_id, token = decoded.split(":", 1)
        return int(user_id), token
    except Exception:
        return None, None
