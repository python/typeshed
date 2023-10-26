# On py311+, things are actually defined here
# and re-exported from importlib.readers,
# but doing it this way leads to less code duplication for us

from collections.abc import Iterable, Iterator
from importlib.readers import *
from typing import TypeVar

_T = TypeVar("_T")

def remove_duplicates(items: Iterable[_T]) -> Iterator[_T]: ...
