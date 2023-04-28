from _typeshed import StrPath
from lib2to3.pytree import Node
from typing import ClassVar
from typing_extensions import Literal

from .. import fixer_base

bind_warning: str

class FixNext(fixer_base.BaseFix):
    BM_compatible: ClassVar[Literal[True]]
    PATTERN: ClassVar[str]
    order: ClassVar[Literal["pre"]]
    shadowed_next: bool
    def start_tree(self, tree: Node, filename: StrPath) -> None: ...
    def transform(self, node, results) -> None: ...

def is_assign_target(node): ...
def find_assign(node): ...
def is_subtree(root, node): ...
