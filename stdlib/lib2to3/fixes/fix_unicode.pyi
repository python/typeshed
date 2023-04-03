from _typeshed import StrPath
from lib2to3.pytree import Node
from typing import ClassVar
from typing_extensions import Literal

from .. import fixer_base

class FixUnicode(fixer_base.BaseFix):
    BM_compatible: ClassVar[Literal[True]]
    PATTERN: ClassVar[Literal["STRING | 'unicode' | 'unichr'"]]  # type: ignore[name-defined]  # Name "STRING" is not defined
    unicode_literals: bool
    def start_tree(self, tree: Node, filename: StrPath) -> None: ...
    def transform(self, node, results): ...
