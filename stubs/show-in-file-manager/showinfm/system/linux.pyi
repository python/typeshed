import typing as t
from _typeshed import Incomplete
from enum import Enum

from ..constants import FileManagerType

# must be replaced by packaging.version.Version after implementing of https://github.com/python/typeshed/issues/5768
_packaging_Version = Incomplete

def stock_linux_file_manager() -> str: ...
def user_linux_file_manager() -> str: ...
def valid_linux_file_manager() -> str: ...
def known_linux_file_managers() -> tuple[str]: ...
def linux_file_manager_type(file_manager: str) -> FileManagerType: ...
def caja_version() -> _packaging_Version | None: ...
def caja_supports_select() -> bool: ...
def translate_wsl_path(path: str, from_windows_to_wsl: bool) -> str: ...
def wsl_path_is_for_windows(path_or_uri: str) -> bool: ...

class WSLTransformPathURI(t.NamedTuple):
    is_win_location: bool
    win_uri: str
    win_path: str
    linux_path: str
    is_dir: bool
    exists: bool

def wsl_transform_path_uri(path_or_uri: str, generate_win_path: bool) -> WSLTransformPathURI: ...
def wsl_path_to_uri_for_windows_explorer(path: str) -> str: ...

class LinuxDesktop(Enum):
    gnome: int
    unity: int
    cinnamon: int
    kde: int
    xfce: int
    mate: int
    lxde: int
    lxqt: int
    ubuntugnome: int
    popgnome: int
    deepin: int
    zorin: int
    ukui: int
    pantheon: int
    enlightenment: int
    wsl: int
    wsl2: int
    cutefish: int
    lumina: int
    unknown: int

LinuxDesktopHumanize: dict[str, str]
LinuxDesktopFamily: dict[str, str]
StandardLinuxFileManager: dict[str, str]
LinuxFileManagerBehavior: dict[str, FileManagerType]

def wsl_version() -> LinuxDesktop | None: ...
def detect_wsl() -> bool: ...
def linux_desktop() -> LinuxDesktop: ...
def linux_desktop_humanize(desktop: LinuxDesktop) -> str: ...
