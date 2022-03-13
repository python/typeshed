import typing
from typing import Any, Callable, Pattern

from parsimonious.exceptions import ParseError
from parsimonious.grammar import Grammar
from parsimonious.nodes import Node
from parsimonious.utils import StrAndRepr

MARKER: Any

def is_callable(value: Any) -> bool: ...

_CALLABLE_RETURN_TYPE = int | tuple[int, list[Node]] | Node | None
_CALLABLE_TYPE = (
    Callable[[str, int], _CALLABLE_RETURN_TYPE]
    | Callable[[str, int, dict[tuple[int, int], Node], ParseError, Grammar], _CALLABLE_RETURN_TYPE]
    | Callable[[Any, str, int], _CALLABLE_RETURN_TYPE]
    | Callable[[Any, str, int, dict[tuple[int, int], Node], ParseError, Grammar], _CALLABLE_RETURN_TYPE]
)

def expression(callable: _CALLABLE_TYPE, rule_name: str, grammar: Grammar) -> Expression: ...

class Expression(StrAndRepr):
    name: str
    identity_tuple: tuple[str]
    def __init__(self, name: str = ...) -> None: ...
    def parse(self, text: str, pos: int = ...) -> Node: ...
    def match(self, text: str, pos: int = ...) -> Node: ...
    def match_core(self, text: str, pos: int, cache: dict[tuple[int, int], Node], error: ParseError) -> Node: ...
    def as_rule(self) -> str: ...

class Literal(Expression):
    literal: str
    identity_tuple: tuple[str, str]
    def __init__(self, literal: str, name: str = ...) -> None: ...

class TokenMatcher(Literal): ...

class Regex(Expression):
    re: Pattern[str]
    identity_tuple: tuple[str, Pattern[str]]
    def __init__(
        self,
        pattern: str,
        name: str = ...,
        ignore_case: bool = ...,
        locale: bool = ...,
        multiline: bool = ...,
        dot_all: bool = ...,
        unicode: bool = ...,
        verbose: bool = ...,
        ascii: bool = ...,
    ) -> None: ...

class Compound(Expression):
    members: typing.Sequence[Expression]
    def __init__(self, *members: typing.Sequence[Expression], **kwargs: Any) -> None: ...

class Sequence(Compound): ...
class OneOf(Compound): ...
class Lookahead(Compound): ...
class Not(Compound): ...
class Optional(Compound): ...
class ZeroOrMore(Compound): ...

class OneOrMore(Compound):
    min: int
    def __init__(self, member: Expression, name: str = ..., min: int = ...) -> None: ...
