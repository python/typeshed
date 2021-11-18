from typing import Any

class Document:
    id: Any
    payload: Any
    def __init__(self, id, payload: Any | None = ..., **fields) -> None: ...
