from typing import Optional

class Mark:
    name: str
    index: int
    line: int
    column: int
    buffer: Optional[str]
    pointer: int
    def __init__(self, name: str, index: int, line: int, column: int, buffer: Optional[str], pointer: int) -> None: ...
    def get_snippet(self, indent: int = ..., max_length: int = ...) -> Optional[str]: ...

class YAMLError(Exception): ...

class MarkedYAMLError(YAMLError):
    context: Optional[str]
    context_mark: Optional[Mark]
    problem: Optional[str]
    problem_mark: Optional[Mark]
    note: Optional[str]
    def __init__(
        self,
        context: Optional[str] = ...,
        context_mark: Optional[Mark] = ...,
        problem: Optional[str] = ...,
        problem_mark: Optional[Mark] = ...,
        note: Optional[str] = ...,
    ) -> None: ...
