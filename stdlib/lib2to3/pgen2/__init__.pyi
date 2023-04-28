from collections.abc import Callable
from typing import Any
from typing_extensions import TypeAlias

from .pgen2.grammar import Grammar
from .pytree import _RawNode

# This is imported in several lib2to3/pgen2 submodules
_Convert: TypeAlias = Callable[[Grammar, _RawNode], Any]  # noqa: Y047
