from _typeshed import StrPath
from collections.abc import Generator
from lib2to3.pytree import Node
from typing import ClassVar
from typing_extensions import Literal

from .. import fixer_base

def traverse_imports(names) -> Generator[str, None, None]: ...

class FixImport(fixer_base.BaseFix):
    BM_compatible: ClassVar[Literal[True]]
    PATTERN: ClassVar[str]
    skip: bool
    def start_tree(self, tree: Node, name: StrPath) -> None: ...
    def transform(self, node, results): ...
    def probably_a_local_import(self, imp_name): ...
