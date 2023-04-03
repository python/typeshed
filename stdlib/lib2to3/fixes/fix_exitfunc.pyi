from _typeshed import Incomplete, StrPath
from lib2to3 import fixer_base
from lib2to3.pytree import Node
from typing import ClassVar
from typing_extensions import Literal, LiteralString

class FixExitfunc(fixer_base.BaseFix):
    BM_compatible: ClassVar[Literal[True]]
    PATTERN: ClassVar[LiteralString]
    def __init__(self, *args) -> None: ...
    sys_import: Incomplete | None
    def start_tree(self, tree: Node, filename: StrPath) -> None: ...
    def transform(self, node, results) -> None: ...
