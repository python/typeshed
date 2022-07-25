from collections.abc import Callable, Sequence
from io import TextIOWrapper
from re import Pattern
from typing import Any

HELP: str
RUNNER_PATTERN: Pattern[Any]

def match(obj_name: str) -> tuple[str, str]: ...
def resolve(module_name: str, object_name: str) -> Any: ...
def show_help(stream: TextIOWrapper, name: str, error: str | None = ...) -> None: ...
def show_exception(stream: TextIOWrapper) -> None: ...
def run(argv: Sequence[str] = ..., _serve: Callable[..., Any] = ...) -> None: ...
