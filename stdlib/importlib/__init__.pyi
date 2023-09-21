import sys
from collections.abc import Mapping, Sequence
from importlib import abc as abc, machinery as machinery, util as util
from importlib.abc import Loader
from types import ModuleType

__all__ = ["__import__", "import_module", "invalidate_caches", "reload"]

# Signature of `builtins.__import__` should be kept identical to `importlib.__import__`
def __import__(
    name: str,
    globals: Mapping[str, object] | None = None,
    locals: Mapping[str, object] | None = None,
    fromlist: Sequence[str] = (),
    level: int = 0,
) -> ModuleType: ...

# `importlib.import_module` return type should be kept the same as `builtins.__import__`
def import_module(name: str, package: str | None = None) -> ModuleType: ...

if sys.version_info < (3, 12):
    def find_loader(name: str, path: str | None = None) -> Loader | None: ...

def invalidate_caches() -> None: ...
def reload(module: ModuleType) -> ModuleType: ...
