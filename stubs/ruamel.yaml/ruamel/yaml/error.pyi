from _typeshed import Incomplete
from typing import Any

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

class StreamMark:
    name: Incomplete
    index: Incomplete
    line: Incomplete
    column: Incomplete
    def __init__(self, name: Any, index: int, line: int, column: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

class FileMark(StreamMark): ...

class StringMark(StreamMark):
    buffer: Incomplete
    pointer: Incomplete
    def __init__(self, name: Any, index: int, line: int, column: int, buffer: Any, pointer: Any) -> None: ...
    def get_snippet(self, indent: int = 4, max_length: int = 75) -> Any: ...

class CommentMark:
    column: Incomplete
    def __init__(self, column: Any) -> None: ...

class YAMLError(Exception): ...

class MarkedYAMLError(YAMLError):
    context: Incomplete
    context_mark: Incomplete
    problem: Incomplete
    problem_mark: Incomplete
    note: Incomplete
    def __init__(
        self,
        context: Any = None,
        context_mark: Any = None,
        problem: Any = None,
        problem_mark: Any = None,
        note: Any = None,
        warn: Any = None,
    ) -> None: ...
    def check_append(self, lines: list[str], val: str | None) -> None: ...

class YAMLStreamError(Exception): ...
class YAMLWarning(Warning): ...

class MarkedYAMLWarning(YAMLWarning):
    context: Incomplete
    context_mark: Incomplete
    problem: Incomplete
    problem_mark: Incomplete
    note: Incomplete
    warn: Incomplete
    def __init__(
        self,
        context: Any = None,
        context_mark: Any = None,
        problem: Any = None,
        problem_mark: Any = None,
        note: Any = None,
        warn: Any = None,
    ) -> None: ...
    def check_append(self, lines: list[str], val: str | None) -> None: ...

class ReusedAnchorWarning(YAMLWarning): ...

class UnsafeLoaderWarning(YAMLWarning):
    text: str

class MantissaNoDotYAML1_1Warning(YAMLWarning):
    node: Incomplete
    flt: Incomplete
    def __init__(self, node: Any, flt_str: Any) -> None: ...

class YAMLFutureWarning(Warning): ...

class MarkedYAMLFutureWarning(YAMLFutureWarning):
    context: Incomplete
    context_mark: Incomplete
    problem: Incomplete
    problem_mark: Incomplete
    note: Incomplete
    warn: Incomplete
    def __init__(
        self,
        context: Any = None,
        context_mark: Any = None,
        problem: Any = None,
        problem_mark: Any = None,
        note: Any = None,
        warn: Any = None,
    ) -> None: ...
    def check_append(self, lines: list[str], val: str | None) -> None: ...
