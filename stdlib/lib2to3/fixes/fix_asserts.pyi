from typing import ClassVar
from typing_extensions import Literal, LiteralString

from ..fixer_base import BaseFix

NAMES: dict[str, str]

class FixAsserts(BaseFix):
    BM_compatible: ClassVar[Literal[False]]
    PATTERN: ClassVar[LiteralString]
    def transform(self, node, results) -> None: ...
