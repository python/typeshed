from collections.abc import Iterator
from typing import Any

class Composable:
    def __init__(self, wrapped) -> None: ...
    def as_string(self, context) -> str: ...
    def __add__(self, other) -> Composed: ...
    def __mul__(self, n) -> Composed: ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...

class Composed(Composable):
    def __init__(self, seq) -> None: ...
    @property
    def seq(self) -> list[Composable]: ...
    def as_string(self, context) -> str: ...
    def __iter__(self) -> Iterator[Composable]: ...
    def __add__(self, other) -> Composed: ...
    def join(self, joiner) -> Composed: ...

class SQL(Composable):
    def __init__(self, string) -> None: ...
    @property
    def string(self) -> str: ...
    def as_string(self, context) -> str: ...
    def format(self, *args, **kwargs) -> Composed: ...
    def join(self, seq) -> Composed: ...

class Identifier(Composable):
    def __init__(self, *strings) -> None: ...
    @property
    def strings(self) -> tuple[str]: ...
    @property
    def string(self) -> str: ...
    def as_string(self, context) -> str: ...

class Literal(Composable):
    @property
    def wrapped(self): ...
    def as_string(self, context) -> str: ...

class Placeholder(Composable):
    def __init__(self, name: Any | None = ...) -> None: ...
    @property
    def name(self) -> str | None: ...
    def as_string(self, context) -> str: ...

NULL: Any
DEFAULT: Any
