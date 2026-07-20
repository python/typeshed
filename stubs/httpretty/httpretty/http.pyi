from collections.abc import Sequence
from typing import Literal
from typing_extensions import TypeVar

_T = TypeVar("_T", str, bytes)

STATUSES: dict[int, str]

class HttpBaseClass:
    GET: Literal["GET"]
    PUT: Literal["PUT"]
    POST: Literal["POST"]
    DELETE: Literal["DELETE"]
    HEAD: Literal["HEAD"]
    PATCH: Literal["PATCH"]
    OPTIONS: Literal["OPTIONS"]
    CONNECT: Literal["CONNECT"]
    METHODS: tuple[Literal["GET", "PUT", "POST", "DELETE", "HEAD", "PATCH", "OPTIONS", "CONNECT"], ...]

def parse_requestline(s: str) -> tuple[str, str, str]: ...
def last_requestline(sent_data: Sequence[_T]) -> _T | None: ...
