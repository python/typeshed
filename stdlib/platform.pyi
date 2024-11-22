import sys
from typing import NamedTuple, type_check_only

def libc_ver(executable: str | None = None, lib: str = "", version: str = "", chunksize: int = 16384) -> tuple[str, str]: ...
def win32_ver(release: str = "", version: str = "", csd: str = "", ptype: str = "") -> tuple[str, str, str, str]: ...
def win32_edition() -> str: ...
def win32_is_iot() -> bool: ...
def mac_ver(
    release: str = "", versioninfo: tuple[str, str, str] = ("", "", ""), machine: str = ""
) -> tuple[str, tuple[str, str, str], str]: ...
def java_ver(
    release: str = "", vendor: str = "", vminfo: tuple[str, str, str] = ("", "", ""), osinfo: tuple[str, str, str] = ("", "", "")
) -> tuple[str, str, tuple[str, str, str], tuple[str, str, str]]: ...
def system_alias(system: str, release: str, version: str) -> tuple[str, str, str]: ...
def architecture(executable: str = sys.executable, bits: str = "", linkage: str = "") -> tuple[str, str]: ...

if sys.version_info >= (3, 9):
    @type_check_only
    class _uname_result_base(NamedTuple):
        system: str
        node: str
        release: str
        version: str
        machine: str

    class uname_result(_uname_result_base, tuple[str, str, str, str, str, str]):  # type: ignore[misc]
        @property
        def processor(self) -> str: ...

else:
    class uname_result(NamedTuple):
        system: str
        node: str
        release: str
        version: str
        machine: str
        processor: str

def uname() -> uname_result: ...
def system() -> str: ...
def node() -> str: ...
def release() -> str: ...
def version() -> str: ...
def machine() -> str: ...
def processor() -> str: ...
def python_implementation() -> str: ...
def python_version() -> str: ...
def python_version_tuple() -> tuple[str, str, str]: ...
def python_branch() -> str: ...
def python_revision() -> str: ...
def python_build() -> tuple[str, str]: ...
def python_compiler() -> str: ...
def platform(aliased: bool = ..., terse: bool = ...) -> str: ...

if sys.version_info >= (3, 10):
    def freedesktop_os_release() -> dict[str, str]: ...

if sys.version_info >= (3, 13):
    class AndroidVer(NamedTuple):
        release: str
        api_level: int
        manufacturer: str
        model: str
        device: str
        is_emulator: bool

    class IOSVersionInfo(NamedTuple):
        system: str
        release: str
        model: str
        is_simulator: bool

    def android_ver(
        release: str = "",
        api_level: int = 0,
        manufacturer: str = "",
        model: str = "",
        device: str = "",
        is_emulator: bool = False,
    ) -> AndroidVer: ...
    def ios_ver(system: str = "", release: str = "", model: str = "", is_simulator: bool = False) -> IOSVersionInfo: ...
