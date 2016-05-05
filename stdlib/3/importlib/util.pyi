# Stubs for importlib.util (Python 3.4)

from ._bootstrap import MAGIC_NUMBER as MAGIC_NUMBER
from ._bootstrap import cache_from_source as cache_from_source
from ._bootstrap import decode_source as decode_source
from ._bootstrap import source_from_cache as source_from_cache
from ._bootstrap import spec_from_loader as spec_from_loader
from ._bootstrap import spec_from_file_location as spec_from_file_location

from typing import Optional, Callable
from ._bootstrap import ModuleSpec
from types import ModuleType

def resolve_name(name: str, package: Optional[str]) -> str: ...
def find_spec(name: str, package: Optional[str] = ...) -> Optional[ModuleSpec]: ...
def set_package(fxn: Callable[..., ModuleType]) -> Callable[..., ModuleType]: ...
def set_loader(fxn: Callable[..., ModuleType]) -> Callable[..., ModuleType]: ...
def module_for_loader(fxn: Callable[..., ModuleType]) \
                      -> Callable[..., ModuleType]: ...
