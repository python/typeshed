from collections.abc import Callable, Mapping
from typing import Literal, Protocol, TypedDict, TypeVar
from typing_extensions import Unpack

from _win32typing import PyHKEY, PyIID, PyIUnknown
from win32con import HKEY_CLASSES_ROOT

T = TypeVar("T", PyHKEY, int)

class RegisterClass(Protocol):
    _reg_clsid_: PyIID

class RegisterFlag(TypedDict, total=False):
    quiet: bool
    debug: bool
    finalize_register: Callable[[], None]

class UnregisterFlag(TypedDict, total=False):
    quiet: bool
    finalize_unregister: Callable[[], None]

class ElevatedFlag(TypedDict, total=False):
    quiet: bool
    unattended: bool
    hwnd: int

class CommandFlag(RegisterFlag, UnregisterFlag, ElevatedFlag):  # type: ignore[misc]
    ...

CATID_PythonCOMServer = "{B3EF80D0-68E2-11D0-A689-00C04FD658FF}"

def _set_subkeys(keyName: str, valueDict: Mapping[str | None, str], base: PyHKEY | int = HKEY_CLASSES_ROOT) -> None: ...
def _set_string(path: str | None, value: str, base: PyHKEY | int = HKEY_CLASSES_ROOT) -> None: ...
def _get_string(path: str | None, base: PyHKEY | int = HKEY_CLASSES_ROOT) -> str | None: ...
def _remove_key(path: str | None, base: PyHKEY | int = HKEY_CLASSES_ROOT) -> None: ...
def recurse_delete_key(path: str | None, base: PyHKEY | int = HKEY_CLASSES_ROOT) -> None: ...
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
    clsid: PyIID, progID: str | None = None, verProgID: str | None = None, customKeys: tuple[str, T] | None = None
) -> list[tuple[str, T | int]]: ...
def UnregisterServer(
    clsid: PyIID, progID: str | None = None, verProgID: str | None = None, customKeys: tuple[str, PyHKEY | int] | None = None
) -> None: ...
def GetRegisteredServerOption(clsid: PyIID, optionName: str) -> str | None: ...
def _get(ob: object, attr: str, default=None): ...
def RegisterClasses(*classes: type[RegisterClass], **flags: Unpack[RegisterFlag]) -> None: ...
def UnregisterClasses(*classes: type[RegisterClass], **flags: Unpack[UnregisterFlag]) -> None: ...
def UnregisterInfoClasses(*classes: type[RegisterClass]) -> list[tuple[str, PyHKEY | int]]: ...
def ReExecuteElevated(flags: ElevatedFlag) -> None: ...
def UseCommandLine(*classes: type[RegisterClass], **flags: Unpack[CommandFlag]) -> list[tuple[str, PyHKEY | int]] | None: ...
def RegisterPyComCategory() -> None: ...
