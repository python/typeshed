from _typeshed import SupportsRead
from typing import IO, Any, Callable, Iterable, Iterator, List, Optional, Tuple, Union

Loader = Any
MetaPathFinder = Any
PathEntryFinder = Any

_ModuleInfoLike = Tuple[MetaPathFinder | PathEntryFinder, str, bool]

def extend_path(path: List[str], name: str) -> List[str]: ...

class ImpImporter:
    def __init__(self, path: Optional[str] = ...) -> None: ...

class ImpLoader:
    def __init__(self, fullname: str, file: IO[str], filename: str, etc: Tuple[str, str, int]) -> None: ...

def find_loader(fullname: str) -> Optional[Loader]: ...
def get_importer(path_item: str) -> Optional[PathEntryFinder]: ...
def get_loader(module_or_name: str) -> Loader: ...
def iter_importers(fullname: str = ...) -> Iterator[MetaPathFinder | PathEntryFinder]: ...
def iter_modules(path: Optional[Iterable[str]] = ..., prefix: str = ...) -> Iterator[_ModuleInfoLike]: ...
def read_code(stream: SupportsRead[bytes]) -> Any: ...  # undocumented
def walk_packages(
    path: Optional[Iterable[str]] = ..., prefix: str = ..., onerror: Optional[Callable[[str], None]] = ...
) -> Iterator[_ModuleInfoLike]: ...
def get_data(package: str, resource: str) -> Optional[bytes]: ...
