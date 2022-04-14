import sys
from typing import Any, Protocol

if sys.version_info >= (3, 9):
    __all__ = ["getline", "clearcache", "checkcache", "lazycache"]
else:
    __all__ = ["getline", "clearcache", "checkcache"]

_ModuleGlobals = dict[str, Any]
_ModuleMetadata = tuple[int, float | None, list[str], str]

class _SourceLoader(Protocol):
    def __call__(self) -> str | None: ...

cache: dict[str, _SourceLoader | _ModuleMetadata]  # undocumented

def getline(filename: str, lineno: int, module_globals: _ModuleGlobals | None = ...) -> str: ...
def clearcache() -> None: ...
def getlines(filename: str, module_globals: _ModuleGlobals | None = ...) -> list[str]: ...
def checkcache(filename: str | None = ...) -> None: ...
def updatecache(filename: str, module_globals: _ModuleGlobals | None = ...) -> list[str]: ...
def lazycache(filename: str, module_globals: _ModuleGlobals) -> bool: ...
