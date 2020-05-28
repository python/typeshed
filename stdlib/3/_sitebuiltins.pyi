
import sys
from typing import Optional, NoReturn, ClassVar, Sequence

if sys.version_info >= (3, 8)
    from typing import Literal
else:
    from typing_extensions import Literal

class Quitter:
    def __init__(self, name: str, eof: str) -> None: ...
    def __call__(self, code: Optional[int] = ...) -> NoReturn: ...

class _Printer:
    MAXLINES: ClassVar[Literal[23]]

    def __init__(self, name: str, data: str, files: Sequence[str] = ..., dirs: Sequence[str] = ...) -> None: ...
    def __call__(self) -> None: ...

class _Helper:
    def __call__(self, request: object) -> None: ...
