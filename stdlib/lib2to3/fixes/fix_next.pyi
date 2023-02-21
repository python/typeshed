from typing import ClassVar
from typing_extensions import Literal, LiteralString

from .. import fixer_base

bind_warning: str

class FixNext(fixer_base.BaseFix):
    BM_compatible: ClassVar[Literal[True]]
    PATTERN: ClassVar[LiteralString]
    order: ClassVar[Literal["pre"]]
    shadowed_next: bool
    def start_tree(self, tree, filename) -> None: ...
    def transform(self, node, results) -> None: ...

def is_assign_target(node): ...
def find_assign(node): ...
def is_subtree(root, node): ...
