from typing import Final, NamedTuple, TypeVar

_T = TypeVar("_T")

MOBILE_DEVICE_FAMILIES: Final[tuple[str, ...]]
PC_OS_FAMILIES: Final[tuple[str, ...]]
MOBILE_OS_FAMILIES: Final[tuple[str, ...]]
MOBILE_BROWSER_FAMILIES: Final[tuple[str, ...]]
TABLET_DEVICE_FAMILIES: Final[tuple[str, ...]]
TOUCH_CAPABLE_OS_FAMILIES: Final[tuple[str, ...]]
TOUCH_CAPABLE_DEVICE_FAMILIES: Final[tuple[str, ...]]
EMAIL_PROGRAM_FAMILIES: Final[set[str]]

def verify_attribute(attribute: _T) -> _T | int: ...
def parse_version(
    major: str | None = None, minor: str | None = None, patch: str | None = None, patch_minor: str | None = None
) -> tuple[int | str, ...]: ...

class Browser(NamedTuple):
    family: str
    version: tuple[int | str, ...]
    version_string: str

def parse_browser(
    family: str, major: str | None = None, minor: str | None = None, patch: str | None = None, patch_minor: str | None = None
) -> Browser: ...

class OperatingSystem(NamedTuple):
    family: str
    version: tuple[int | str, ...]
    version_string: str

def parse_operating_system(
    family: str, major: str | None = None, minor: str | None = None, patch: str | None = None, patch_minor: str | None = None
) -> OperatingSystem: ...

class Device(NamedTuple):
    family: str
    brand: str | None
    model: str | None

def parse_device(family: str, brand: str | None, model: str | None) -> Device: ...

class UserAgent:
    ua_string: str
    os: OperatingSystem
    browser: Browser
    device: Device
    def __init__(self, user_agent_string: str) -> None: ...
    def get_device(self) -> str: ...
    def get_os(self) -> str: ...
    def get_browser(self) -> str: ...
    @property
    def is_tablet(self) -> bool: ...
    @property
    def is_mobile(self) -> bool: ...
    @property
    def is_touch_capable(self) -> bool: ...
    @property
    def is_pc(self) -> bool: ...
    @property
    def is_bot(self) -> bool: ...
    @property
    def is_email_client(self) -> bool: ...

def parse(user_agent_string: str) -> UserAgent: ...
