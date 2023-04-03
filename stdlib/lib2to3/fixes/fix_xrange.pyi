from _typeshed import Incomplete, StrPath
from lib2to3.pytree import Node
from typing import ClassVar
from typing_extensions import Literal, LiteralString

from .. import fixer_base

class FixXrange(fixer_base.BaseFix):
    BM_compatible: ClassVar[Literal[True]]
    PATTERN: ClassVar[LiteralString]
    transformed_xranges: set[Incomplete] | None
    def start_tree(self, tree: Node, filename: StrPath) -> None: ...
    def finish_tree(self, tree: Node, filename: StrPath) -> None: ...
    def transform(self, node, results): ...
    def transform_xrange(self, node, results) -> None: ...
    def transform_range(self, node, results): ...
    P1: ClassVar[LiteralString]
    p1: ClassVar[Incomplete]
    P2: ClassVar[LiteralString]
    p2: ClassVar[Incomplete]
    def in_special_context(self, node): ...
