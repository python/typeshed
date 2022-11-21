from _typeshed import Incomplete
from logging import Logger
from typing import ClassVar

from .spec import Connection

LOGGER: Logger

class PlainCredentials:
    TYPE: ClassVar[str]
    username: str
    password: str
    erase_on_connect: bool
    def __init__(self, username: str, password: str, erase_on_connect: bool = ...) -> None: ...
    def __eq__(self, other: PlainCredentials) -> bool: ...  # type: ignore[override]
    def __ne__(self, other: PlainCredentials) -> bool: ...  # type: ignore[override]
    def response_for(self, start: Connection.Start) -> tuple[str | None, bytes | None]: ...
    def erase_credentials(self) -> None: ...

class ExternalCredentials:
    TYPE: ClassVar[str]
    erase_on_connect: bool
    def __init__(self) -> None: ...
    def __eq__(self, other: ExternalCredentials) -> bool: ...  # type: ignore[override]
    def __ne__(self, other: ExternalCredentials) -> bool: ...  # type: ignore[override]
    def response_for(self, start: Connection.Start) -> tuple[str | None, bytes | None]: ...
    def erase_credentials(self) -> None: ...

VALID_TYPES: Incomplete
