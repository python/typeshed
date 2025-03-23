import sys
from _typeshed import StrPath
from typing import Final

if sys.platform == "win32":
    from ctypes import windll as windll

__version__: Final[str]
__version_info__: Final[tuple[int, int, int]]
unicode = str
system: Final[str]

def user_data_dir(
    appname: StrPath | None = None, appauthor: StrPath | None = None, version: StrPath | None = None, roaming: bool = False
) -> StrPath: ...
def site_data_dir(
    appname: StrPath | None = None, appauthor: StrPath | None = None, version: StrPath | None = None, roaming: bool = False
) -> StrPath: ...
def user_config_dir(
    appname: StrPath | None = None, appauthor: StrPath | None = None, version: StrPath | None = None, roaming: bool = False
) -> StrPath: ...
def site_config_dir(
    appname: StrPath | None = None, appauthor: StrPath | None = None, version: StrPath | None = None, roaming: bool = False
) -> StrPath: ...
def user_cache_dir(
    appname: StrPath | None = None, appauthor: StrPath | None = None, version: StrPath | None = None, roaming: bool = False
) -> StrPath: ...
def user_state_dir(
    appname: StrPath | None = None, appauthor: StrPath | None = None, version: StrPath | None = None, roaming: bool = False
) -> StrPath: ...
def user_log_dir(
    appname: StrPath | None = None, appauthor: StrPath | None = None, version: StrPath | None = None, roaming: bool = False
) -> StrPath: ...

class AppDirs:
    appname: StrPath | None
    appauthor: StrPath | None
    version: StrPath | None
    roaming: bool
    multipath: bool
    def __init__(
        self,
        appname: StrPath | None = None,
        appauthor: StrPath | None = None,
        version: StrPath | None = None,
        roaming: bool = False,
        multipath: bool = False,
    ) -> None: ...
    @property
    def user_data_dir(self) -> StrPath: ...
    @property
    def site_data_dir(self) -> StrPath: ...
    @property
    def user_config_dir(self) -> StrPath: ...
    @property
    def site_config_dir(self) -> StrPath: ...
    @property
    def user_cache_dir(self) -> StrPath: ...
    @property
    def user_state_dir(self) -> StrPath: ...
    @property
    def user_log_dir(self) -> StrPath: ...
