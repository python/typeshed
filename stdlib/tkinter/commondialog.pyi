from collections.abc import Mapping
from tkinter import Misc
from typing import Any, ClassVar

__all__ = ["Dialog"]

class Dialog:
    command: ClassVar[str | None]
    master: Misc | None
    options: Mapping[str, Any]
    def __init__(self, master: Misc = None, **options: Any) -> None: ...
    def show(self, **options: Any): ...
