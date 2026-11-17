import types
from typing import TypeVar, type_check_only
from typing_extensions import Self

from gi.repository import Gio

from .bus_names import OwnMixin, WatchMixin
from .proxy import ProxyMixin
from .publication import PublicationMixin
from .registration import RegistrationMixin
from .request_name import RequestNameMixin
from .subscription import SubscriptionMixin

_T = TypeVar("_T")

def bus_get(type: Gio.BusType) -> Bus[object]: ...
def connect(address: str) -> Bus[object]: ...
@type_check_only
class _DBusOrgFreedesktopDBus:
    # Incomplete interface to org.freedesktop.DBus
    Features: list[str]

    def GetId(self) -> str: ...

@type_check_only
class _DBusOrgFreedesktopPolicyKit1Authority:
    # Incomplete interface to org.freedesktop.PolicyKit1.Authority
    BackendFeatures: int  # flags
    BackendName: str
    BackendVersion: str

class Bus(ProxyMixin[_T], RequestNameMixin[_T], OwnMixin, WatchMixin, SubscriptionMixin, RegistrationMixin[_T], PublicationMixin):
    Type: type[Gio.BusType] = ...
    autoclose: bool
    con: Gio.DBusConnection

    def __init__(self, gio_con: Gio.DBusConnection) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None
    ) -> None: ...
    @property
    def dbus(self) -> _DBusOrgFreedesktopDBus: ...
    @property
    def polkit_authority(self) -> _DBusOrgFreedesktopPolicyKit1Authority: ...

def SystemBus() -> Bus[object]: ...
def SessionBus() -> Bus[object]: ...
