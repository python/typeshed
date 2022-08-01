from _typeshed import Incomplete
import sys
from collections.abc import Mapping
from typing import Any, ClassVar

if sys.version_info >= (3, 9):
    __all__ = ["Dialog"]

class Dialog:
    command: ClassVar[str | None]
    master: Incomplete | None
    options: Mapping[str, Incomplete]
    def __init__(self, master: Incomplete | None = ..., **options) -> None: ...
    def show(self, **options) -> Incomplete: ...
