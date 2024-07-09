import os
import sys
from _typeshed import StrPath
from collections.abc import Iterator
from contextlib import AbstractContextManager
from pathlib import Path
from types import ModuleType
from typing import Any, BinaryIO, TextIO
from typing_extensions import TypeAlias

if sys.version_info >= (3, 9):
    from importlib.abc import Traversable

__all__ = ["Package", "contents", "is_resource", "open_binary", "open_text", "path", "read_binary", "read_text"]

if sys.version_info >= (3, 9):
    __all__ += ["as_file", "files"]

if sys.version_info >= (3, 10):
    __all__ += ["ResourceReader"]

if sys.version_info >= (3, 13):
    __all__ += ["Anchor"]
else:
    __all__ += ["Resource"]

Package: TypeAlias = str | ModuleType

if sys.version_info >= (3, 13):
    Anchor: TypeAlias = Package

if sys.version_info < (3, 13):
    Resource: TypeAlias = str
elif sys.version_info < (3, 11):
    Resource: TypeAlias = str | os.PathLike[Any]

if sys.version_info >= (3, 13):
    def open_binary(anchor: Anchor, *path_names: StrPath) -> BinaryIO: ...
    def open_text(anchor: Anchor, *path_names: StrPath, encoding: str = ..., errors: str = "strict") -> TextIO: ...
    def read_binary(anchor: Anchor, *path_names: StrPath) -> bytes: ...
    def read_text(anchor: Anchor, *path_names: StrPath, encoding: str = ..., errors: str = "strict") -> str: ...
    def path(anchor: Anchor, *path_names: StrPath) -> AbstractContextManager[Path]: ...
    def is_resource(anchor: Anchor, *path_names: StrPath) -> bool: ...
    def contents(anchor: Anchor, *path_names: StrPath) -> Iterator[str]: ...

else:
    def open_binary(package: Package, resource: Resource) -> BinaryIO: ...
    def open_text(package: Package, resource: Resource, encoding: str = "utf-8", errors: str = "strict") -> TextIO: ...
    def read_binary(package: Package, resource: Resource) -> bytes: ...
    def read_text(package: Package, resource: Resource, encoding: str = "utf-8", errors: str = "strict") -> str: ...
    def path(package: Package, resource: Resource) -> AbstractContextManager[Path]: ...
    def is_resource(package: Package, name: str) -> bool: ...
    def contents(package: Package) -> Iterator[str]: ...

if sys.version_info >= (3, 9):
    def as_file(path: Traversable) -> AbstractContextManager[Path]: ...

if sys.version_info >= (3, 12):
    def files(anchor: Package | None = ...) -> Traversable: ...

elif sys.version_info >= (3, 9):
    def files(package: Package) -> Traversable: ...

if sys.version_info >= (3, 10):
    from importlib.abc import ResourceReader as ResourceReader
