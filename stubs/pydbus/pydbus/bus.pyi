import types
from typing import Any, Generic, Literal, TypedDict, TypeVar, overload, type_check_only
from typing_extensions import Self

from gi.repository import Gio

from .bus_names import OwnMixin, WatchMixin
from .generic import bound_signal
from .proxy import ProxyMixin, _CompositeObject
from .publication import PublicationMixin
from .registration import RegistrationMixin
from .request_name import RequestNameMixin
from .subscription import SubscriptionMixin

_T = TypeVar("_T")
_ST = TypeVar("_ST")  # signal type

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

@type_check_only
class OrgBluezAdapter1Dict(TypedDict, total=False):
    Address: str
    AddressType: Literal["public", "random"]
    Alias: str
    Class: int
    Connectable: bool
    Discoverable: bool
    DiscoverableTimeout: int
    Discovering: bool
    Manufacturer: int
    Modalias: str
    Name: str
    Pairable: bool
    PairableTimeout: int
    Powered: bool
    Roles: list[str]
    UUIDs: list[str]
    Version: int

@type_check_only
class OrgBluezDevice1Dict(TypedDict, total=False):
    Adapter: str
    Address: str
    AddressType: Literal["public", "random"]
    Alias: str
    Appearance: int
    Blocked: bool
    Bonded: bool
    Class: int
    Connected: bool
    Icon: str
    LegacyPairing: bool
    Modalias: str
    Name: str
    Paired: bool
    ServicesResolved: bool
    Trusted: bool
    UUIDs: list[str]
    WakeAllowed: bool

@type_check_only
class OrgBluezInput1Dict(TypedDict, total=False):
    ReconnectMode: str

@type_check_only
class OrgBluezMedia1Dict(TypedDict, total=False):
    SupportedUUIDs: list[str]

@type_check_only
class OrgBluezMediaControl1Dict(TypedDict, total=False):
    Connected: bool

@type_check_only
class OrgBluezBattery1Dict(TypedDict, total=False):
    Percentage: int
    Source: str

@type_check_only
class OrgBluezGattService1Dict(TypedDict, total=False):
    Device: str
    Handle: int
    Includes: list[str]
    Primary: bool
    UUID: str

@type_check_only
class OrgBluezGattCharacteristic1Dict(TypedDict, total=False):
    Flags: list[str]
    Handle: int
    MTU: int
    Service: str
    UUID: str
    Value: list[int]

@type_check_only
class OrgBluezGattDescriptor1Dict(TypedDict, total=False):
    Characteristic: str
    Handle: int
    UUID: str
    Value: list[int]

@type_check_only
class OrgBluezLEAdvertisingManager1Dict(TypedDict, total=False):
    ActiveInstances: int
    SupportedCapabilities: dict[str, int]  # e.g. MaxTxPower: 7
    SupportedFeatures: list[str]
    SupportedIncludes: list[str]
    SupportedInstances: int
    SupportedSecondaryChannels: list[str]

@type_check_only
class OrgBluezNetwork1Dict(TypedDict, total=False):
    Connected: bool
    Interface: str
    UUID: str

# This is for keys under /org/bluez/hci0/*
_OrgBluezDict = TypedDict(
    "_OrgBluezDict",
    {
        "org.bluez.Adapter1": OrgBluezAdapter1Dict,
        "org.bluez.Battery1": OrgBluezBattery1Dict,
        "org.bluez.Device1": OrgBluezDevice1Dict,
        "org.bluez.GattCharacteristic1": OrgBluezGattCharacteristic1Dict,
        "org.bluez.GattDescriptor1": OrgBluezGattDescriptor1Dict,
        "org.bluez.GattService1": OrgBluezGattService1Dict,
        "org.bluez.Input1": OrgBluezInput1Dict,
        "org.bluez.LEAdvertisingManager1": OrgBluezLEAdvertisingManager1Dict,
        "org.bluez.Media1": OrgBluezMedia1Dict,
        "org.bluez.Network1": OrgBluezNetwork1Dict,
        "org.bluez.MediaControl1": OrgBluezMediaControl1Dict,
        # The following always appear as empty dictionaries on my system.
        "org.bluez.AgentManager1": dict[str, Any],
        "org.bluez.BatteryProviderManager1": dict[str, Any],
        "org.bluez.NetworkServer1": dict[str, Any],
        "org.bluez.ProfileManager1": dict[str, Any],
        "org.freedesktop.DBus.Introspectable": dict[str, Any],
        "org.freedesktop.DBus.Properties": dict[str, Any],
    },
    total=False,
)

@type_check_only
class _OrgFreedesktopDBusObjectManager:
    @staticmethod
    def GetManagedObjects() -> dict[str, _OrgBluezDict]: ...

@type_check_only
class _OrgBluez(_CompositeObject[_T]):
    def __getitem__(  # type: ignore[override]
        self, key: Literal["org.freedesktop.DBus.ObjectManager"]
    ) -> _OrgFreedesktopDBusObjectManager: ...

@type_check_only
class _OrgFreedesktopNotifications(_CompositeObject[_T], Generic[_T, _ST]):
    Inhibited: bool
    ActivationToken: bound_signal[_ST]
    ActionInvoked: bound_signal[_ST]
    NotificationClosed: bound_signal[_ST]

    def CloseNotification(self, id: int) -> None: ...
    def GetCapabilities(self) -> list[str]: ...  # We could use Literal[] here but KDE also returns its own not in the spec.
    def GetServerInformation(self) -> tuple[str, str, str, str]: ...
    def Inhibit(self, name: str, reason: str, hints: dict[str, bool | bytes | int | str]) -> int | None: ...
    def Notify(
        self,
        app_name: str,
        replaces_id: int,
        app_icon: str,
        summary: str,
        body: str,
        actions: list[str],
        hints: dict[str, bool | bytes | int | str],  # See https://specifications.freedesktop.org/notification-spec/1.3/hints.html
        expire_timeout: int,
    ) -> int: ...
    def UnInhibit(self, key: int) -> int | None: ...

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
    @overload  # type: ignore[override]
    def get(self, bus_name: Literal[".Notifications"]) -> _OrgFreedesktopNotifications[_T, object]: ...
    @overload
    def get(self, bus_name: Literal["org.freedesktop.Notifications"]) -> _OrgFreedesktopNotifications[_T, object]: ...
    @overload
    def get(self, bus_name: Literal["org.bluez"], object_path: Literal["/"]) -> _OrgBluez[_T]: ...
    @overload
    def get(self, bus_name: str, object_path: str) -> Any: ...

def SystemBus() -> Bus[object]: ...
def SessionBus() -> Bus[object]: ...
