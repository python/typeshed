from collections.abc import Generator
from typing import ClassVar
from typing_extensions import Literal

from .. import fixer_base

MAPPING: dict[str, str]

def alternates(members): ...
def build_pattern(mapping=...) -> Generator[str, None, None]: ...

class FixImports(fixer_base.BaseFix):
    BM_compatible: ClassVar[Literal[True]]
    mapping = MAPPING  # noqa: F821
    def build_pattern(self): ...
    def compile_pattern(self) -> None: ...
    def match(self, node): ...
    replace: dict[str, str]
    def start_tree(self, tree, filename) -> None: ...
    def transform(self, node, results) -> None: ...
