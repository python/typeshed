import sys
from _typeshed import SupportsRead
from _typeshed.importlib import LoaderProtocol, MetaPathFinderProtocol, PathEntryFinderProtocol
from collections.abc import Callable, Iterable, Iterator
from typing import IO, Any, NamedTuple, TypeVar
from typing_extensions import deprecated

__all__ = [
    "get_importer",
    "iter_importers",
    "get_loader",
    "find_loader",
    "walk_packages",
    "iter_modules",
    "get_data",
    "read_code",
    "extend_path",
    "ModuleInfo",
]
if sys.version_info < (3, 12):
    __all__ += ["ImpImporter", "ImpLoader"]

_PathT = TypeVar("_PathT", bound=Iterable[str])

class ModuleInfo(NamedTuple):
    module_finder: MetaPathFinderProtocol | PathEntryFinderProtocol
    name: str
    ispkg: bool

def extend_path(path: _PathT, name: str) -> _PathT: ...

if sys.version_info < (3, 12):
    class ImpImporter:
        def __init__(self, path: str | None = None) -> None: ...

    class ImpLoader:
        def __init__(self, fullname: str, file: IO[str], filename: str, etc: tuple[str, str, int]) -> None: ...

@deprecated("Use importlib.util.find_spec() instead. Will be removed in Python 3.14.")
def find_loader(fullname: str) -> LoaderProtocol | None: ...
def get_importer(path_item: str) -> MetaPathFinderProtocol | PathEntryFinderProtocol | None: ...
@deprecated("Use importlib.util.find_spec() instead. Will be removed in Python 3.14.")
def get_loader(module_or_name: str) -> LoaderProtocol | None: ...
def iter_importers(fullname: str = "") -> Iterator[MetaPathFinderProtocol | PathEntryFinderProtocol]: ...
def iter_modules(path: Iterable[str] | None = None, prefix: str = "") -> Iterator[ModuleInfo]: ...
def read_code(stream: SupportsRead[bytes]) -> Any: ...  # undocumented
def walk_packages(
    path: Iterable[str] | None = None, prefix: str = "", onerror: Callable[[str], object] | None = None
) -> Iterator[ModuleInfo]: ...
def get_data(package: str, resource: str) -> bytes | None: ...

if sys.version_info >= (3, 9):
    def resolve_name(name: str) -> Any: ...
