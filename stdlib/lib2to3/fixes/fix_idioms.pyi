from typing import ClassVar
from typing_extensions import Literal, LiteralString

from .. import fixer_base

CMP: str
TYPE: str

class FixIdioms(fixer_base.BaseFix):
    BM_compatible: ClassVar[Literal[False]]
    explicit: bool
    PATTERN: ClassVar[LiteralString]
    def match(self, node): ...
    def transform(self, node, results): ...
    def transform_isinstance(self, node, results): ...
    def transform_while(self, node, results) -> None: ...
    def transform_sort(self, node, results) -> None: ...
