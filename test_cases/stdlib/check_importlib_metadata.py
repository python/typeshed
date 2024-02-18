import sys
from _typeshed import StrPath
from os import PathLike
from pathlib import Path
from typing import Any, Optional
from zipfile import Path as ZipPath

if sys.version_info >= (3, 10):
    from importlib.metadata._meta import SimplePath

    # Simplified version of zipfile.Path
    class MyPath:
        @property
        def parent(self) -> PathLike[str]: ...  # undocumented

        def read_text(self, encoding: Optional[str] = ..., errors: Optional[str] = ...) -> str: ...
        def joinpath(self, *other: StrPath) -> Path: ...
        def __truediv__(self, add: StrPath) -> Path: ...

    if sys.version_info >= (3, 12):

        def takes_simple_path(p: SimplePath[Any]) -> None: ...

    else:

        def takes_simple_path(p: SimplePath) -> None: ...

    takes_simple_path(Path())
    takes_simple_path(ZipPath(""))
    takes_simple_path(MyPath())
    takes_simple_path("some string")  # type: ignore
