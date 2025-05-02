from collections.abc import Callable

from gi.repository import Gio
from gi.repository.GLib import Variant

from .exitable import Exitable

class Subscription(Exitable):
    Flags: Gio.DBusSignalFlags

    def __init__(
        self,
        con: Gio.DBusConnection,
        sender: str,
        iface: str,
        member: str | None,
        object: str | None,
        arg0: str | None,
        flags: Gio.DBusSignalFlags,
        callback: Callable[[str, str, str, str, Variant], None] | None,
    ) -> None: ...
    def unsubscribe(self) -> None: ...  # added by ExitableWithAliases('unsubscribe')
    def disconnect(self) -> None: ...  # added by ExitableWithAliases('disconnect')

class SubscriptionMixin:
    SubscriptionFlags: Gio.DBusSignalFlags

    def subscribe(
        self,
        sender: str | None = None,
        iface: str | None = None,
        signal: str | None = None,
        object: str | None = None,
        arg0: str | None = None,
        flags: Gio.DBusSignalFlags = ...,
        signal_fired: Callable[[str, str, str, str, Variant], None] | None = None,
    ) -> Subscription: ...
