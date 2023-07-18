import sys
from collections.abc import Callable
from typing import Any

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

_Writer: TypeAlias = Callable[[str], None]
_Processor: TypeAlias = Callable[[tuple[str, ...], tuple[Any, ...]], None]

class TagTracer:
    indent: int
    def __init__(self) -> None: ...
    def get(self, name: str) -> TagTracerSub: ...
    def setwriter(self, writer: _Writer) -> None: ...
    def setprocessor(self, tags: str | tuple[str, ...], processor: _Processor) -> None: ...

class TagTracerSub:
    root: TagTracer
    tags: tuple[str, ...]
    def __init__(self, root: TagTracer, tags: tuple[str, ...]) -> None: ...
    def __call__(self, *args: object) -> None: ...
    def get(self, name: str) -> TagTracerSub: ...
