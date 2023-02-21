from collections.abc import Generator
from typing import ClassVar
from typing_extensions import Literal, LiteralString

from .. import fixer_base

def traverse_imports(names) -> Generator[str, None, None]: ...

class FixImport(fixer_base.BaseFix):
    BM_compatible: ClassVar[Literal[True]]
    PATTERN: ClassVar[LiteralString]
    skip: bool
    def start_tree(self, tree, name) -> None: ...
    def transform(self, node, results): ...
    def probably_a_local_import(self, imp_name): ...
