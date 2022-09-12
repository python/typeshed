from parsimonious.expressions import Expression
from parsimonious.grammar import LazyReference
from parsimonious.nodes import Node
from parsimonious.utils import StrAndRepr

class ParseError(StrAndRepr, Exception):
    text: str
    pos: int
    expr: Expression | None

    def __init__(self, text: str, pos: int = ..., expr: Expression | None = ...) -> None: ...
    def line(self) -> int: ...
    def column(self) -> int: ...

class LeftRecursionError(ParseError): ...
class IncompleteParseError(ParseError): ...

class VisitationError(Exception):
    original_class: type[BaseException]
    def __init__(self, exc: BaseException, exc_class: type[BaseException], node: Node) -> None: ...

class BadGrammar(StrAndRepr, Exception): ...

class UndefinedLabel(BadGrammar):
    label: LazyReference

    def __init__(self, label: LazyReference) -> None: ...
