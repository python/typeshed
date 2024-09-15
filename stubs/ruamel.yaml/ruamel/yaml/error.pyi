from typing import ClassVar, Self, TypeAlias

from _ruamel_yaml import Mark

from .nodes import ScalarNode

__all__ = [
    "FileMark",
    "StringMark",
    "CommentMark",
    "YAMLError",
    "MarkedYAMLError",
    "ReusedAnchorWarning",
    "UnsafeLoaderWarning",
    "MarkedYAMLWarning",
    "MarkedYAMLFutureWarning",
]

_Mark: TypeAlias = Mark | StreamMark

class StreamMark:
    name: str | None
    index: int
    line: int
    column: int
    def __init__(self, name: str | None, index: int, line: int, column: int) -> None: ...
    def __eq__(self, other: Self, /) -> bool: ...
    def __ne__(self, other: Self, /) -> bool: ...

class FileMark(StreamMark): ...

class StringMark(StreamMark):
    buffer: str
    pointer: int
    def __init__(self, name: str | None, index: int, line: int, column: int, buffer: str, pointer: int) -> None: ...
    def get_snippet(self, indent: int = 4, max_length: int = 75) -> str: ...

class CommentMark:
    column: int
    def __init__(self, column: int) -> None: ...

class YAMLError(Exception): ...

class MarkedYAMLError(YAMLError):
    context: str | None
    context_mark: _Mark | None
    problem: str | None
    problem_mark: _Mark | None
    note: str | None
    def __init__(
        self,
        context: str | None = None,
        context_mark: _Mark | None = None,
        problem: str | None = None,
        problem_mark: _Mark | None = None,
        note: str | None = None,
        warn: str | None = None,
    ) -> None: ...
    def check_append(self, lines: list[str], val: str | None) -> None: ...

class YAMLStreamError(Exception): ...
class YAMLWarning(Warning): ...

class MarkedYAMLWarning(YAMLWarning):
    context: str | None
    context_mark: _Mark | None
    problem: str | None
    problem_mark: _Mark | None
    note: str | None
    warn: str | None
    def __init__(
        self,
        context: str | None = None,
        context_mark: _Mark | None = None,
        problem: str | None = None,
        problem_mark: _Mark | None = None,
        note: str | None = None,
        warn: str | None = None,
    ) -> None: ...
    def check_append(self, lines: list[str], val: str | None) -> None: ...

class ReusedAnchorWarning(YAMLWarning): ...

class UnsafeLoaderWarning(YAMLWarning):
    text: ClassVar[str]

class MantissaNoDotYAML1_1Warning(YAMLWarning):
    node: ScalarNode
    flt: str
    def __init__(self, node: ScalarNode, flt_str: str) -> None: ...

class YAMLFutureWarning(Warning): ...

class MarkedYAMLFutureWarning(YAMLFutureWarning):
    context: str | None
    context_mark: _Mark | None
    problem: str | None
    problem_mark: _Mark | None
    note: str | None
    warn: str | None
    def __init__(
        self,
        context: str | None = None,
        context_mark: _Mark | None = None,
        problem: str | None = None,
        problem_mark: _Mark | None = None,
        note: str | None = None,
        warn: str | None = None,
    ) -> None: ...
    def check_append(self, lines: list[str], val: str | None) -> None: ...
