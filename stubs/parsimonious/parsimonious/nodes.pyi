from collections.abc import Callable, Iterator, Sequence
from re import Match
from typing import Any, NoReturn, TypeVar

from parsimonious.exceptions import VisitationError as VisitationError
from parsimonious.expressions import Expression
from parsimonious.grammar import Grammar

class Node:
    expr: Expression
    full_text: str
    start: int
    end: int
    children: Sequence[Node]
    def __init__(self, expr: Expression, full_text: str, start: int, end: int, children: Sequence[Node] | None = ...) -> None: ...
    @property
    def expr_name(self) -> str: ...
    def __iter__(self) -> Iterator[Node]: ...
    @property
    def text(self) -> str: ...
    def prettily(self, error: Node | None = ...) -> str: ...
    def __repr__(self, top_level: bool = ...) -> str: ...

class RegexNode(Node):
    match: Match[str]

class RuleDecoratorMeta(type): ...

_VisitorResultT = TypeVar("_VisitorResultT")

class NodeVisitor(metaclass=RuleDecoratorMeta):
    grammar: Grammar | Any
    unwrapped_exceptions: tuple[type[BaseException], ...]
    def visit(self, node: Node) -> _VisitorResultT: ...
    def generic_visit(self, node: Node, visited_children: Sequence[Any]) -> NoReturn: ...
    def parse(self, text: str, pos: int = ...) -> _VisitorResultT: ...
    def match(self, text: str, pos: int = ...) -> _VisitorResultT: ...
    def lift_child(self, node: Node, children: Sequence[Any]) -> Any: ...

_CallableT = TypeVar("_CallableT", bound=Callable[..., Any])

def rule(rule_string: str) -> Callable[[_CallableT], _CallableT]: ...
