# Stubs for importlib (Python 3.4)

from ._bootstrap import __import__ as __import__

from typing import Optional
from types import ModuleType

def invalidate_caches() -> None: ...
def import_module(name: str, package: Optional[str] = ...) -> ModuleType: ...
def reload(module: ModuleType) -> ModuleType: ...
