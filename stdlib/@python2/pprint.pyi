import sys
from typing import IO, Any, Dict, Optional, Tuple

def pformat(object: object, indent: int = ..., width: int = ..., depth: Optional[int] = ...) -> str: ...
def pprint(
    object: object, stream: Optional[IO[str]] = ..., indent: int = ..., width: int = ..., depth: Optional[int] = ...
) -> None: ...
def isreadable(object: object) -> bool: ...
def isrecursive(object: object) -> bool: ...
def saferepr(object: object) -> str: ...

class PrettyPrinter:
    def __init__(
        self, indent: int = ..., width: int = ..., depth: Optional[int] = ..., stream: Optional[IO[str]] = ...
    ) -> None: ...
    def pformat(self, object: object) -> str: ...
    def pprint(self, object: object) -> None: ...
    def isreadable(self, object: object) -> bool: ...
    def isrecursive(self, object: object) -> bool: ...
    def format(self, object: object, context: Dict[int, Any], maxlevels: int, level: int) -> Tuple[str, bool, bool]: ...
