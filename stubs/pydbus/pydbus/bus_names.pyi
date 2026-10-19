from collections.abc import Callable

from gi.repository import Gio

from .exitable import Exitable

class NameOwner(Exitable):
    Flags: Gio.BusNameOwnerFlags

    def __init__(
        self,
        con: Gio.DBusConnection,
        name: str,
        flags: Gio.BusNameOwnerFlags,
        name_aquired_handler: Callable[[str], object],
        name_lost_handler: Callable[[str], object],
    ) -> None: ...
    def unown(self) -> None: ...  # added by ExitableWithAliases('unown')

class NameWatcher(Exitable):
    Flags: Gio.BusNameWatcherFlags

    def __init__(
        self,
        con: Gio.DBusConnection,
        name: str,
        flags: Gio.BusNameWatcherFlags,
        name_appeared_handler: Callable[[str], object],
        name_vanished_handler: Callable[[str], object],
    ) -> None: ...
    def unwatch(self) -> None: ...  # added by ExitableWithAliases('unwatch')

class OwnMixin:
    NameOwnerFlags: Gio.BusNameOwnerFlags

    def own_name(
        self,
        name: str,
        flags: Gio.BusNameOwnerFlags = ...,
        name_aquired: Callable[[str], object] | None = ...,
        name_lost: Callable[[str], object] | None = ...,
    ) -> NameOwner: ...

class WatchMixin:
    NameWatcherFlags: Gio.BusNameWatcherFlags

    def watch_name(
        self,
        name: str,
        flags: Gio.BusNameWatcherFlags = ...,
        name_appeared: Callable[[str], object] | None = ...,
        name_vanished: Callable[[str], object] | None = ...,
    ) -> NameWatcher: ...
