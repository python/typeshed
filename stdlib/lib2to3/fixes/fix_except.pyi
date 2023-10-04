from collections.abc import Generator, Iterable
from typing import ClassVar, TypeVar
from typing_extensions import Literal

from .. import fixer_base
from ..pytree import Base

_N = TypeVar("_N", bound=Base)

def find_excepts(nodes: Iterable[_N]) -> Generator[tuple[_N, _N], None, None]: ...

class FixExcept(fixer_base.BaseFix):
    BM_compatible: ClassVar[Literal[True]]
    PATTERN: ClassVar[str]
    def transform(self, node, results): ...
