from logging import Logger
from typing import ClassVar, Protocol

from .spec import Connection

class _Credentials(Protocol):
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def response_for(self, start: Connection.Start) -> tuple[str | None, bytes | None]: ...
    def erase_credentials(self) -> None: ...

LOGGER: Logger

class PlainCredentials(_Credentials):
    TYPE: ClassVar[str]
    erase_on_connect: bool
    username: str
    password: str
    def __init__(self, username: str, password: str, erase_on_connect: bool = False) -> None: ...

class ExternalCredentials(_Credentials):
    TYPE: ClassVar[str]
    erase_on_connect: bool
    def __init__(self) -> None: ...

VALID_TYPES: list[_Credentials]
