import sys
from ctypes import _CArgObject, _PointerLike
from typing import Any
from typing_extensions import TypeAlias

if sys.platform == "win32":
    # Description, Source, HelpFile, HelpContext, scode
    _COMError_Details: TypeAlias = tuple[str | None, str | None, str | None, int | None, int | None]

    class COMError(Exception):
        hresult: int
        text: str | None
        details: _COMError_Details

        def __init__(self, hresult: int, text: str | None, details: _COMError_Details) -> None: ...

    def CopyComPointer(src: _PointerLike, dst: _PointerLike | _CArgObject) -> int: ...

def __getattr__(name: str) -> Any: ...  # incomplete
