import sys
from _typeshed import StrPath
from collections.abc import Sequence
from typing import IO, overload
from typing_extensions import Self
from zipfile import ZipFile

if sys.version_info >= (3, 12):
    class InitializedState:
        def __init__(self, *args: object, **kwargs: object) -> None: ...
        def __getstate__(self) -> tuple[list[object], dict[object, object]]: ...
        def __setstate__(self, state: Sequence[tuple[list[object], dict[object, object]]]) -> None: ...

    class CompleteDirs(InitializedState, ZipFile):
        def resolve_dir(self, name: str) -> str: ...
        @overload
        @classmethod
        def make(cls, source: ZipFile) -> CompleteDirs: ...
        @overload
        @classmethod
        def make(cls, source: StrPath | IO[bytes]) -> Self: ...
