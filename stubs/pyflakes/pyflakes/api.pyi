from collections.abc import Iterator, Sequence
from typing import Any, Pattern

from pyflakes.reporter import Reporter

__all__ = ['check', 'checkPath', 'checkRecursive', 'iterSourceCode', 'main']

PYTHON_SHEBANG_REGEX: Pattern[bytes]

def check(codeString: str, filename: str, reporter: Reporter | None = ...) -> int: ...
def checkPath(filename, reporter: Reporter | None = ...) -> int: ...
def isPythonFile(filename) -> bool: ...
def iterSourceCode(paths: Sequence[Any]) -> Iterator[Any]: ...
def checkRecursive(paths: Sequence[Any], reporter: Reporter) -> int: ...
def main(prog: str | None = ..., args: Sequence[Any] | None = ...) -> None: ...
