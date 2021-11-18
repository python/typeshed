from ._util import to_string as to_string
from typing import Any

class Suggestion:
    string: Any
    payload: Any
    score: Any
    def __init__(self, string, score: float = ..., payload: Any | None = ...) -> None: ...

class SuggestionParser:
    with_scores: Any
    with_payloads: Any
    sugsize: int
    def __init__(self, with_scores, with_payloads, ret) -> None: ...
    def __iter__(self): ...
