from typing import Any, Generic, Literal, TypedDict, TypeVar, overload, type_check_only
from typing_extensions import Self
from xml.etree.ElementTree import Element

from .bus import Bus
from .generic import bound_signal

_T = TypeVar("_T")
_ST = TypeVar("_ST")  # signal type

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
# Refer to https://github.com/bluez/bluez/blob/master/doc/ for interface details
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
        # Dicts below are always empty because they have no properties. However, the key existence may still be useful
        # for introspection.
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

class ProxyObject(Generic[_T]):
    def __init__(self, bus: Bus[_T], bus_name: str, path: str, object: Self | None = None) -> None: ...
    def __getattr__(self, name: str) -> _T: ...
    def __setattr__(self, name: str, value: _T) -> None: ...

@type_check_only
class _CompositeObject(ProxyObject[_T]):  # Inside CompositeInterface
    def __getitem__(self, iface: str) -> ProxyObject[_T]: ...

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

class ProxyMixin(Generic[_T]):
    @overload
    def get(self, bus_name: Literal[".Notifications"]) -> _OrgFreedesktopNotifications[_T, object]: ...
    @overload
    def get(self, bus_name: Literal["org.freedesktop.Notifications"]) -> _OrgFreedesktopNotifications[_T, object]: ...
    @overload
    def get(self, bus_name: Literal["org.bluez"], object_path: Literal["/"]) -> _OrgBluez[_T]: ...
    @overload
    def get(self, bus_name: str, object_path: str | None = None, *, timeout: int | None = None) -> _CompositeObject[_T]: ...

@type_check_only
class _interface(ProxyObject[_T]):  # inside Interface
    @staticmethod
    def _Introspect() -> None: ...

def Interface(iface: Element) -> _interface[object]: ...
def CompositeInterface(introspection: Element) -> _CompositeObject[object]: ...
