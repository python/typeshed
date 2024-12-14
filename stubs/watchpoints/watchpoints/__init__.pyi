from collections.abc import Callable
from typing import Final, Literal
from typing_extensions import LiteralString, Unpack

from .watch import Watch

__version__: Final[LiteralString]

all: Final[list[Literal["watch", "unwatch"]]]
watch: Watch
unwatch: Final[Callable[[Unpack[tuple[object, ...]]], None]]
