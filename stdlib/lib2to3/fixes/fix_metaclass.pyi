from collections.abc import Generator
from typing import ClassVar, Literal

from .. import fixer_base
from ..pytree import Base

def has_metaclass(parent): ...
def fixup_parse_tree(cls_node) -> None: ...
def fixup_simple_stmt(parent, i, stmt_node) -> None: ...
def remove_trailing_newline(node) -> None: ...
def find_metas(cls_node) -> Generator[tuple[Base, int, Base], None, None]: ...
def fixup_indent(suite) -> None: ...

class FixMetaclass(fixer_base.BaseFix):
    BM_compatible: ClassVar[Literal[True]]
    PATTERN: ClassVar[str]
    def transform(self, node, results) -> None: ...
