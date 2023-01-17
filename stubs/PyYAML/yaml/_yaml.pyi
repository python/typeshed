from _typeshed import Incomplete
from _typeshed import SupportsRead
from collections.abc import Mapping, Sequence
from typing import IO, Any

from .events import Event
from .nodes import Node
from .tokens import Token

def get_version_string() -> str: ...
def get_version() -> tuple[int, int, int]: ...

class Mark:
    name: Any
    index: int
    line: int
    column: int
    buffer: Any
    pointer: Any
    def __init__(self, name, index: int, line: int, column: int, buffer, pointer) -> None: ...
    def get_snippet(self): ...

class CParser:
    def __init__(self, stream: str | bytes | SupportsRead[str | bytes]) -> None: ...
    def dispose(self) -> None: ...
    def get_token(self) -> Token | None: ...
    def peek_token(self) -> Token | None: ...
    def check_token(self, *choices) -> bool: ...
    def get_event(self) -> Event | None: ...
    def peek_event(self) -> Event | None: ...
    def check_event(self, *choices) -> bool: ...
    def check_node(self) -> bool: ...
    def get_node(self) -> Node | None: ...
    def get_single_node(self) -> Node | None: ...
    def raw_parse(self) -> int: ...
    def raw_scan(self) -> int: ...

class CEmitter:
    def __init__(
        self,
        stream: IO[Any],
        canonical: Incomplete | None = ...,
        indent: int | None = ...,
        width: int | None = ...,
        allow_unicode: Incomplete | None = ...,
        line_break: str | None = ...,
        encoding: str | None = ...,
        explicit_start: Incomplete | None = ...,
        explicit_end: Incomplete | None = ...,
        version: Sequence[int] | None = ...,
        tags: Mapping[str, str] | None = ...,
    ) -> None: ...
    def dispose(self) -> None: ...
    def emit(self, event_object) -> None: ...
    def open(self) -> None: ...
    def close(self) -> None: ...
    def serialize(self, node) -> None: ...