import threading
from collections.abc import Iterable, Set as AbstractSet
from re import Pattern
from typing import Callable, TypedDict, override, type_check_only

try:
    from inotify.adapters import Inotify
    from inotify.constants import IN_CREATE, IN_DELETE, IN_DELETE_SELF, IN_MODIFY, IN_MOVE_SELF, IN_MOVED_FROM, IN_MOVED_TO
except ImportError:
    Inotify = object

COMPILED_EXT_RE: Pattern[str]


class Reloader(threading.Thread):
    daemon: bool

    def __init__(
        self,
        extra_files: Iterable[str] | None = None,
        interval: int = 1,
        callback: Callable[[str], None] | None = None,
    ) -> None: ...
    def add_extra_file(self, filename: str) -> None: ...
    def get_files(self) -> list[str]: ...
    @override
    def run(self) -> None: ...


has_inotify: bool

EventMask = int


class InotifyReloader(threading.Thread):
    event_mask: EventMask
    daemon: bool

    def __init__(
        self,
        extra_files: Iterable[str] | None = None,
        callback: Callable[[str], None] | None = None,
    ) -> None: ...
    def add_extra_file(self, filename: str) -> None: ...
    def get_dirs(self) -> AbstractSet[str]: ...
    @override
    def run(self) -> None: ...


type PreferredReloaderType = type[InotifyReloader | Reloader]


@type_check_only
class _ReloadedEngines(TypedDict):
    auto: PreferredReloaderType
    pool: type[Reloader]
    inotify: type[InotifyReloader]


preferred_reloader: PreferredReloaderType
reloader_engines: _ReloadedEngines
