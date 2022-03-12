from re import Match
from typing import Any, Callable, Iterator, NoReturn, TypeVar
from typing_extensions import Self

from parsimonious.exceptions import UndefinedLabel, VisitationError
from parsimonious.expressions import Expression
from parsimonious.grammar import Grammar

class Node:
    expr: Expression
    full_text: str
    start: int
    end: int
    children: list[Node]
    def __init__(self, expr: Expression, full_text: str, start: int, end: int, children: list[Node] | None = ...) -> None: ...
    @property
    def expr_name(self) -> str: ...
    def __iter__(self) -> Iterator[Node]: ...
    @property
    def text(self) -> str: ...
    def prettily(self, error: Node | None = ...) -> str: ...

class RegexNode(Node):
    match: Match[str]

class RuleDecoratorMeta(type):
    def __new__(metaclass: type[Self], name: str, bases: tuple[type, ...], namespace: dict[str, Any]) -> Self: ...

class NodeVisitor(type):
    grammar: Grammar | Any
    unwrapped_exceptions: tuple[Exception]
    def visit(self, node: Node) -> Any: ...
    def generic_visit(self, node: Node, visited_children: list[Any]) -> NoReturn: ...
    def parse(self, text: str, pos: int = ...) -> Node: ...
    def match(self, text: str, pos: int = ...) -> Node: ...
    def lift_child(self, node: Node, children: list[Any]) -> Any: ...

_T = TypeVar("_T")

def rule(rule_string: str) -> Callable[[Callable[..., _T]], Callable[..., _T]]: ...
