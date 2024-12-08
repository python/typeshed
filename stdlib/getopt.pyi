from collections.abc import Iterable, Sequence
from typing import TypeVar

_StrSequenceT = TypeVar("_StrSequenceT", bound=Sequence[str])

__all__ = ["GetoptError", "error", "getopt", "gnu_getopt"]

def getopt(
    args: _StrSequenceT, shortopts: str, longopts: Iterable[str] | str = []
) -> tuple[list[tuple[str, str]], _StrSequenceT]: ...
def gnu_getopt(
    args: Sequence[str], shortopts: str, longopts: Iterable[str] | str = []
) -> tuple[list[tuple[str, str]], list[str]]: ...

class GetoptError(Exception):
    msg: str
    opt: str
    def __init__(self, msg: str, opt: str = "") -> None: ...

error = GetoptError
