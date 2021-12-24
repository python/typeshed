from collections.abc import Generator
import ast
from typing import Any, ClassVar, Type

class Plugin:
    name: ClassVar[str]
    version: ClassVar[str]
    def __init__(self, tree: ast.AST) -> None: ...
    def run(self) -> Generator[tuple[int, int, str, Type[Any]], None, None]: ...
