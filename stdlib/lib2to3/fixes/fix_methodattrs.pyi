from typing import Final
from typing import ClassVar, Literal

from .. import fixer_base

MAP: Final[dict[str, str]]

class FixMethodattrs(fixer_base.BaseFix):
    BM_compatible: ClassVar[Literal[True]]
    PATTERN: ClassVar[str]
    def transform(self, node, results) -> None: ...
