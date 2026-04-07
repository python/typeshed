from collections.abc import Iterable
from typing import Literal

class Node:
    __slots__ = str | Iterable[str]
    source_line: int
    source_column: int
    type: str

    def __init__(self, source_line: int, source_column: int) -> None: ...
    def serialize(self) -> str: ...

class ParseError(Node):
    __slots__ = str | Iterable[str]
    type: Literal["error"]
    kind: str
    message: str
    def __init__(self, line: int, column: int, kind: str, message: str) -> None: ...

class Comment(Node):
    __slots__ = str | Iterable[str]
    type: Literal["comment"]
    value: str
    def __init__(self, line: int, column: int, value: str) -> None: ...

class WhitespaceToken(Node):
    __slots__ = str | Iterable[str]
    type: Literal["whitespace"]
    value: str
    def __init__(self, line: int, column: int, value: str) -> None: ...

class LiteralToken(Node):
    __slots__ = str | Iterable[str]
    type: Literal["literal"]
    value: str
    def __init__(self, line: int, column: int, value: str) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

class IdentToken(Node):
    __slots__ = str | Iterable[str]
    type: Literal["ident"]
    value: str
    lower_value: str
    def __init__(self, line: int, column: int, value: str) -> None: ...

class AtKeywordToken(Node):
    __slots__ = str | Iterable[str]
    type: Literal["at-keyword"]
    value: str
    lower_value: str
    def __init__(self, line: int, column: int, value: str) -> None: ...

class HashToken(Node):
    __slots__ = str | Iterable[str]
    type: Literal["hash"]
    value: str
    is_identifier: bool
    def __init__(self, line: int, column: int, value: str, is_identifier: bool) -> None: ...

class StringToken(Node):
    __slots__ = str | Iterable[str]
    type: Literal["string"]
    value: str
    representation: str
    def __init__(self, line: int, column: int, value: str, representation: str) -> None: ...

class URLToken(Node):
    __slots__ = str | Iterable[str]
    type: Literal["url"]
    value: str
    representation: str
    def __init__(self, line: int, column: int, value: str, representation: str) -> None: ...

class UnicodeRangeToken(Node):
    __slots__ = str | Iterable[str]
    type: Literal["unicode-range"]
    start: int
    end: int
    def __init__(self, line: int, column: int, start: int, end: int) -> None: ...

class NumberToken(Node):
    __slots__ = str | Iterable[str]
    type: Literal["number"]
    value: float
    int_value: int | None
    is_integer: bool
    representation: str
    def __init__(self, line: int, column: int, value: float, int_value: int | None, representation: str) -> None: ...

class PercentageToken(Node):
    __slots__ = str | Iterable[str]
    type: Literal["percentage"]
    value: float
    int_value: int | None
    is_integer: bool
    representation: str
    def __init__(self, line: int, column: int, value: float, int_value: int | None, representation: str) -> None: ...

class DimensionToken(Node):
    __slots__ = str | Iterable[str]
    type: Literal["dimension"]
    value: float
    int_value: int | None
    is_integer: bool
    representation: str
    unit: str
    lower_unit: str
    def __init__(self, line: int, column: int, value: float, int_value: int | None, representation: str, unit: str) -> None: ...

class ParenthesesBlock(Node):
    __slots__ = str | Iterable[str]
    type: Literal["()"]
    content: list[Node]
    def __init__(self, line: int, column: int, content: list[Node]) -> None: ...

class SquareBracketsBlock(Node):
    __slots__ = str | Iterable[str]
    type: Literal["[]"]
    content: list[Node]
    def __init__(self, line: int, column: int, content: list[Node]) -> None: ...

class CurlyBracketsBlock(Node):
    __slots__ = str | Iterable[str]
    type: Literal["{}"]
    content: list[Node]
    def __init__(self, line: int, column: int, content: list[Node]) -> None: ...

class FunctionBlock(Node):
    __slots__ = str | Iterable[str]
    type: Literal["function"]
    name: str
    lower_name: str
    arguments: list[Node]
    def __init__(self, line: int, column: int, name: str, arguments: list[Node]) -> None: ...

class Declaration(Node):
    __slots__ = str | Iterable[str]
    type: Literal["declaration"]
    name: str
    lower_name: str
    value: list[Node]
    important: bool
    def __init__(self, line: int, column: int, name: str, lower_name: str, value: list[Node], important: bool) -> None: ...

class QualifiedRule(Node):
    __slots__ = str | Iterable[str]
    type: Literal["qualified-rule"]
    prelude: list[Node]
    content: list[Node]
    def __init__(self, line: int, column: int, prelude: list[Node], content: list[Node]) -> None: ...

class AtRule(Node):
    __slots__ = str | Iterable[str]
    type: Literal["at-rule"]
    at_keyword: str
    lower_at_keyword: str
    prelude: list[Node]
    content: list[Node] | None
    def __init__(
        self, line: int, column: int, at_keyword: str, lower_at_keyword: str, prelude: list[Node], content: list[Node] | None
    ) -> None: ...
