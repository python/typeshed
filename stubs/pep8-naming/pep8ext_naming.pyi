from typing import Any, FrozenSet
import ast
from argparse import Namespace

__version__: str

PYTHON_VERSION: tuple[int, int, int]
PY2: bool
CLASS_METHODS: FrozenSet[str]
METACLASS_BASES: FrozenSet[str]
METHOD_CONTAINER_NODES: set[ast.AST]
FUNC_NODES: tuple[ast.AST]

class NamingChecker:
    name: str
    version: str
    visitors: Any
    decorator_to_type: Any
    ignore_names: FrozenSet[str]
    parents: Any
    def __init__(self, tree: ast.AST, filename: str) -> None: ...
    @classmethod
    def add_options(cls, parser: Any) -> None: ...
    @classmethod
    def parse_options(cls, option: Namespace) -> None: ...
    def run(self): ...
    def __getattr__(self, name: str) -> Any: ...  # incomplete (other attributes are normally not accessed)

def __getattr__(name: str) -> Any: ...  # incomplete (other attributes are normally not accessed)
