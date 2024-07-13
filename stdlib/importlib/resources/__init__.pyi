import os
import sys
from _typeshed import StrPath
from collections.abc import Iterator
from contextlib import AbstractContextManager
from io import TextIOWrapper
from pathlib import Path
from types import ModuleType
from typing import Any, BinaryIO, TextIO, overload
from typing_extensions import TypeAlias, Unpack

if sys.version_info >= (3, 11):
    from importlib.resources._common import Package
else:
    Package: TypeAlias = str | ModuleType

if sys.version_info >= (3, 9):
    from importlib.abc import Traversable

__all__ = ["Package", "contents", "is_resource", "open_binary", "open_text", "path", "read_binary", "read_text"]

if sys.version_info >= (3, 9):
    __all__ += ["as_file", "files"]

if sys.version_info >= (3, 10):
    __all__ += ["ResourceReader"]

if sys.version_info < (3, 13):
    __all__ += ["Resource"]

if sys.version_info < (3, 11):
    Resource: TypeAlias = str | os.PathLike[Any]
elif sys.version_info < (3, 13):
    Resource: TypeAlias = str

if sys.version_info >= (3, 13):
    from importlib.resources._common import Anchor

    __all__ += ["Anchor"]

    from importlib.resources._functional import contents, is_resource, open_binary, open_text, path, read_binary, read_text

else:
    def open_binary(package: Package, resource: Resource) -> BinaryIO: ...
    def open_text(package: Package, resource: Resource, encoding: str = "utf-8", errors: str = "strict") -> TextIO: ...
    def read_binary(package: Package, resource: Resource) -> bytes: ...
    def read_text(package: Package, resource: Resource, encoding: str = "utf-8", errors: str = "strict") -> str: ...
    def path(package: Package, resource: Resource) -> AbstractContextManager[Path]: ...
    def is_resource(package: Package, name: str) -> bool: ...
    def contents(package: Package) -> Iterator[str]: ...

if sys.version_info >= (3, 11):
    from importlib.resources._common import as_file
elif sys.version_info >= (3, 9):
    def as_file(path: Traversable) -> AbstractContextManager[Path]: ...

if sys.version_info >= (3, 11):
    from importlib.resources._common import files

elif sys.version_info >= (3, 9):
    def files(package: Package) -> Traversable: ...

if sys.version_info >= (3, 10):
    from importlib.abc import ResourceReader as ResourceReader
