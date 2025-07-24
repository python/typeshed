from collections.abc import Iterable
from typing import Any

from _win32typing import PyIClassFactory, PyIID

def RegisterClassFactories(
    clsids: Iterable[PyIID], flags: int | None = None, clsctx: int | None = None
) -> list[tuple[PyIClassFactory, Any]]: ...
def RevokeClassFactories(infos: Iterable[tuple[Any, Any]]) -> None: ...
