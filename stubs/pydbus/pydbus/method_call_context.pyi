from typing import Generic, NamedTuple, TypeVar

from gi.repository import Gio

from .bus import Bus

_T = TypeVar("_T")

class AuthorizationResult(NamedTuple):
    is_authorized: bool
    is_challenge: bool
    details: dict[str, str]

class MethodCallContext(Generic[_T]):
    def __init__(self, gdbus_method_invocation: Gio.DBusMethodInvocation) -> None: ...
    @property
    def bus(self) -> Bus[_T]: ...
    @property
    def sender(self) -> str: ...
    @property
    def object_path(self) -> str: ...
    @property
    def interface_name(self) -> str: ...
    @property
    def method_name(self) -> str: ...
    def check_authorization(self, action_id: str, details: dict[str, str], interactive: bool = False) -> AuthorizationResult: ...
    def is_authorized(self, action_id: str, details: dict[str, str], interactive: bool = False) -> bool: ...
