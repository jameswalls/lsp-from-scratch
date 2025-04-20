import json

def encode_message(msg: object) -> bytes:
    content = json.dumps(msg, separators=(',', ':'))

    len_content = len(content)
    return f"Content-Length: {len_content}\r\n\r\n{content}".encode("utf-8")

class BaseMessage:
    def __init__(self, method: str):
        self.Method = method

def base_message_hook(obj: dict) -> BaseMessage:
    return BaseMessage(obj["method"])

def decode_message(msg: bytes) -> tuple[str, bytes]:
    header, content = msg.split(b"\r\n\r\n")

    content_length_bytes = header[len(b"Content-Length: "):]
    content_length = int(content_length_bytes)

    base_messge: BaseMessage = json.loads(
        content[:content_length],
        object_hook=base_message_hook
    )

    return base_messge.Method, content[:content_length]
