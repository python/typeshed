from typing import IO, Any, Dict, Tuple

def pformat(object: object, indent: int = ..., width: int = ..., depth: int | None = ...) -> str: ...
def pprint(
    object: object, stream: IO[str] | None = ..., indent: int = ..., width: int = ..., depth: int | None = ...
) -> None: ...
def isreadable(object: object) -> bool: ...
def isrecursive(object: object) -> bool: ...
def saferepr(object: object) -> str: ...

class PrettyPrinter:
    def __init__(self, indent: int = ..., width: int = ..., depth: int | None = ..., stream: IO[str] | None = ...) -> None: ...
    def pformat(self, object: object) -> str: ...
    def pprint(self, object: object) -> None: ...
    def isreadable(self, object: object) -> bool: ...
    def isrecursive(self, object: object) -> bool: ...
    def format(self, object: object, context: Dict[int, Any], maxlevels: int, level: int) -> Tuple[str, bool, bool]: ...
