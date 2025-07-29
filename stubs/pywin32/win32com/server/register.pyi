from collections.abc import Callable, Mapping
from typing import Literal, Protocol, TypedDict, TypeVar
from typing_extensions import Unpack

from _win32typing import PyHKEY, PyIID, PyIUnknown

_T = TypeVar("_T", PyHKEY, int)

class _RegisterClass(Protocol):
    _reg_clsid_: PyIID

class _RegisterFlag(TypedDict, total=False):
    quiet: bool
    debug: bool
    finalize_register: Callable[[], None]

class _UnregisterFlag(TypedDict, total=False):
    quiet: bool
    finalize_unregister: Callable[[], None]

class _ElevatedFlag(TypedDict, total=False):
    quiet: bool
    unattended: bool
    hwnd: int

class _CommandFlag(_RegisterFlag, _UnregisterFlag, _ElevatedFlag):  # type: ignore[misc]
    ...

CATID_PythonCOMServer: Literal["{B3EF80D0-68E2-11D0-A689-00C04FD658FF}"]

def _set_subkeys(keyName: str, valueDict: Mapping[str | None, str], base: PyHKEY | int = ...) -> None: ...
def _set_string(path: str | None, value: str, base: PyHKEY | int = ...) -> None: ...
def _get_string(path: str | None, base: PyHKEY | int = ...) -> str | None: ...
def _remove_key(path: str | None, base: PyHKEY | int = ...) -> None: ...
def recurse_delete_key(path: str | None, base: PyHKEY | int = ...) -> None: ...
def _cat_registrar() -> PyIUnknown: ...
def _find_localserver_exe(mustfind: bool) -> str | None: ...
def _find_localserver_module() -> str: ...
def RegisterServer(
    clsid: PyIID,
    pythonInstString: str | None = None,
    desc: str | None = None,
    progID: str | None = None,
    verProgID: str | None = None,
    defIcon: str | None = None,
    threadingModel: Literal["apartment", "both", "free", "neutral"] = "both",
    policy: str | None = None,
    catids: list[PyIID] = [],
    other: Mapping[str, str] = {},
    addPyComCat: bool | None = None,
    dispatcher: str | None = None,
    clsctx: int | None = None,
    addnPath: str | None = None,
) -> None: ...
def GetUnregisterServerKeys(
    clsid: PyIID, progID: str | None = None, verProgID: str | None = None, customKeys: tuple[str, _T] | None = None
) -> list[tuple[str, _T | int]]: ...
def UnregisterServer(
    clsid: PyIID, progID: str | None = None, verProgID: str | None = None, customKeys: tuple[str, PyHKEY | int] | None = None
) -> None: ...
def GetRegisteredServerOption(clsid: PyIID, optionName: str) -> str | None: ...
def _get(ob: object, attr: str, default=None): ...
def RegisterClasses(*classes: type[_RegisterClass], **flags: Unpack[_RegisterFlag]) -> None: ...
def UnregisterClasses(*classes: type[_RegisterClass], **flags: Unpack[_UnregisterFlag]) -> None: ...
def UnregisterInfoClasses(*classes: type[_RegisterClass]) -> list[tuple[str, PyHKEY | int]]: ...
def ReExecuteElevated(flags: _ElevatedFlag) -> None: ...
def UseCommandLine(*classes: type[_RegisterClass], **flags: Unpack[_CommandFlag]) -> list[tuple[str, PyHKEY | int]] | None: ...
def RegisterPyComCategory() -> None: ...
