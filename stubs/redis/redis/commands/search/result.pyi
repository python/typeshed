from ._util import to_string as to_string
from .document import Document as Document
from typing import Any

class Result:
    total: Any
    duration: Any
    docs: Any
    def __init__(self, res, hascontent, duration: int = ..., has_payload: bool = ..., with_scores: bool = ...) -> None: ...
