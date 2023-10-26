# On py311+, things are actually defined in importlib.resources.readers,
# and re-exported here,
# but doing it this way leads to less code duplication for us

import pathlib
import sys
from _typeshed import Incomplete, StrPath
from collections.abc import Iterable, Iterator
from io import BufferedReader
from typing import NoReturn, TypeVar
from typing_extensions import Literal, Never, Self

if sys.version_info >= (3, 11):
    import importlib.resources.abc as abc
else:
    import importlib.abc as abc

if sys.version_info >= (3, 10):
    if sys.version_info >= (3, 11):
        __all__ = ["FileReader", "ZipReader", "MultiplexedPath", "NamespaceReader"]
    if sys.version_info < (3, 11):
        _T = TypeVar("_T")

        def remove_duplicates(items: Iterable[_T]) -> Iterator[_T]: ...

    class FileReader(abc.TraversableResources):
        path: pathlib.Path
        def __init__(self, loader) -> None: ...
        def resource_path(self, resource: StrPath) -> str: ...
        def files(self) -> pathlib.Path: ...

    class ZipReader(abc.TraversableResources):
        prefix: str
        archive: Incomplete
        def __init__(self, loader, module: str) -> None: ...
        def open_resource(self, resource: str) -> BufferedReader: ...
        def is_resource(self, path: StrPath) -> bool: ...
        def files(self): ...

    class MultiplexedPath(abc.Traversable):
        def __init__(self, *paths: abc.Traversable) -> None: ...
        def iterdir(self) -> Iterator[abc.Traversable]: ...
        def read_bytes(self) -> NoReturn: ...
        def read_text(self, *args: Never, **kwargs: Never) -> NoReturn: ...  # type: ignore[override]
        def is_dir(self) -> Literal[True]: ...
        def is_file(self) -> Literal[False]: ...
        if sys.version_info >= (3, 12):
            def joinpath(self, *descendants: str) -> abc.Traversable: ...
        else:
            def joinpath(self, child: str) -> abc.Traversable: ...  # type: ignore[override]
            __truediv__ = joinpath
        def open(self, *args: Never, **kwargs: Never) -> NoReturn: ...  # type: ignore[override]
        @property
        def name(self) -> str: ...

    class NamespaceReader(abc.TraversableResources):
        path: MultiplexedPath
        def __init__(self, namespace_path) -> None: ...
        def resource_path(self, resource: str) -> str: ...
        def files(self) -> MultiplexedPath: ...
