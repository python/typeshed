from _typeshed import Incomplete

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
    def __init__(self, name, index: int, line: int, column: int) -> None: ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...

class FileMark(StreamMark): ...

class StringMark(StreamMark):
    buffer: Incomplete
    pointer: Incomplete
    def __init__(self, name, index: int, line: int, column: int, buffer, pointer) -> None: ...
    def get_snippet(self, indent: int = 4, max_length: int = 75): ...

class CommentMark:
    column: Incomplete
    def __init__(self, column) -> None: ...

class YAMLError(Exception): ...

class MarkedYAMLError(YAMLError):
    context: Incomplete
    context_mark: Incomplete
    problem: Incomplete
    problem_mark: Incomplete
    note: Incomplete
    def __init__(
        self,
        context: Incomplete | None = None,
        context_mark: Incomplete | None = None,
        problem: Incomplete | None = None,
        problem_mark: Incomplete | None = None,
        note: Incomplete | None = None,
        warn: Incomplete | None = None,
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
        context: Incomplete | None = None,
        context_mark: Incomplete | None = None,
        problem: Incomplete | None = None,
        problem_mark: Incomplete | None = None,
        note: Incomplete | None = None,
        warn: Incomplete | None = None,
    ) -> None: ...
    def check_append(self, lines: list[str], val: str | None) -> None: ...

class ReusedAnchorWarning(YAMLWarning): ...

class UnsafeLoaderWarning(YAMLWarning):
    text: str

class MantissaNoDotYAML1_1Warning(YAMLWarning):
    node: Incomplete
    flt: Incomplete
    def __init__(self, node, flt_str) -> None: ...

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
        context: Incomplete | None = None,
        context_mark: Incomplete | None = None,
        problem: Incomplete | None = None,
        problem_mark: Incomplete | None = None,
        note: Incomplete | None = None,
        warn: Incomplete | None = None,
    ) -> None: ...
    def check_append(self, lines: list[str], val: str | None) -> None: ...
