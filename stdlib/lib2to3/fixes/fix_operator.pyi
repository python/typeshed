from lib2to3 import fixer_base
from typing import ClassVar
from typing_extensions import Literal, LiteralString

def invocation(s): ...

class FixOperator(fixer_base.BaseFix):
    BM_compatible: ClassVar[Literal[True]]
    order: ClassVar[Literal["pre"]]
    methods: str
    obj: str
    PATTERN: ClassVar[LiteralString]
    def transform(self, node, results): ...
