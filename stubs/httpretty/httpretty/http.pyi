from collections.abc import Sequence
from typing_extensions import TypeVar

_T = TypeVar("_T", str, bytes)

STATUSES: dict[int, str]

class HttpBaseClass:
    GET: Final = "GET"
    PUT: Final = "PUT"
    POST: Final = "POST"
    DELETE: Final = "DELETE"
    HEAD: Final = "HEAD"
    PATCH: Final = "PATCH"
    OPTIONS: Final = "OPTIONS"
    CONNECT: Final = "CONNECT"
    METHODS: tuple[_HTTPMethod, ...]

def parse_requestline(s: str) -> tuple[str, str, str]: ...
def last_requestline(sent_data: Sequence[_T]) -> _T | None: ...
