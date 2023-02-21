from collections.abc import Generator, Iterable
from lib2to3.pytree import Base
from typing import ClassVar, TypeVar
from typing_extensions import Literal, LiteralString

from .. import fixer_base

_N = TypeVar("_N", bound=Base)

def find_excepts(nodes: Iterable[_N]) -> Generator[tuple[_N, _N], None, None]: ...

class FixExcept(fixer_base.BaseFix):
    BM_compatible: ClassVar[Literal[True]]
    PATTERN: ClassVar[LiteralString]
    def transform(self, node, results): ...
