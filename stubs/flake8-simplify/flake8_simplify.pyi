import ast
from typing import Any, Generator, Tuple, Type

class Plugin:
    name: str
    version: str
    def __init__(self, tree: ast.AST) -> None: ...
    def run(self) -> Generator[Tuple[int, int, str, Type[Any]], None, None]: ...
