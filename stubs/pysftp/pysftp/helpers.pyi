from collections.abc import Callable, Iterator
from contextlib import AbstractContextManager
from typing_extensions import TypeAlias

def known_hosts() -> str: ...
def st_mode_to_int(val: int) -> int: ...

class WTCallbacks:
    def __init__(self) -> None: ...
    def file_cb(self, pathname: str) -> None: ...
    def dir_cb(self, pathname: str) -> None: ...
    def unk_cb(self, pathname: str) -> None: ...
    @property
    def flist(self) -> list[str]: ...
    @flist.setter
    def flist(self, val: list[str]) -> None: ...
    @property
    def dlist(self) -> list[str]: ...
    @dlist.setter
    def dlist(self, val: list[str]) -> None: ...
    @property
    def ulist(self) -> list[str]: ...
    @ulist.setter
    def ulist(self, val: list[str]) -> None: ...

def path_advance(thepath: str, sep: str = ...) -> Iterator[str]: ...
def path_retreat(thepath: str, sep: str = ...) -> Iterator[str]: ...
def reparent(newparent: str, oldpath: str) -> str: ...

_PathCallback: TypeAlias = Callable[[str], object]

def walktree(
    localpath: str, fcallback: _PathCallback, dcallback: _PathCallback, ucallback: _PathCallback, recurse: bool = True
) -> None: ...
def cd(localpath: str | None = None) -> AbstractContextManager[None]: ...
