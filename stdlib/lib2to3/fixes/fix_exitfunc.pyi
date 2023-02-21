from _typeshed import Incomplete
from lib2to3 import fixer_base
from typing import ClassVar
from typing_extensions import Literal, LiteralString

class FixExitfunc(fixer_base.BaseFix):
    BM_compatible: ClassVar[Literal[True]]
    PATTERN: ClassVar[LiteralString]
    def __init__(self, *args) -> None: ...
    sys_import: Incomplete | None
    def start_tree(self, tree, filename) -> None: ...
    def transform(self, node, results) -> None: ...
