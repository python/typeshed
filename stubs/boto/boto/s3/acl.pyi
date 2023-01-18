from _typeshed import Incomplete
from typing import Any

from .connection import S3Connection
from .user import User

CannedACLStrings: list[str]

class Policy:
    parent: Any
    namespace: Any
    acl: ACL
    def __init__(self, parent: Incomplete | None = ...) -> None: ...
    owner: User
    def startElement(self, name: str, attrs: dict[str, Any], connection: S3Connection) -> None | User | ACL: ...
    def endElement(self, name: str, value: Any, connection: S3Connection) -> None: ...
    def to_xml(self) -> str: ...

class ACL:
    policy: Policy
    grants: list[Grant]
    def __init__(self, policy: Policy | None = ...) -> None: ...
    def add_grant(self, grant: Grant) -> None: ...
    def add_email_grant(self, permission: str, email_address: str) -> None: ...
    def add_user_grant(self, permission: str, user_id: str, display_name: str | None = ...) -> None: ...
    def startElement(self, name, attrs, connection): ...
    def endElement(self, name: str, value: Any, connection: S3Connection) -> None: ...
    def to_xml(self) -> str: ...

class Grant:
    NameSpace: str
    permission: str
    id: str
    display_name: str
    uri: str
    email_address: str
    type: str
    def __init__(
        self,
        permission: str | None = ...,
        type: str | None = ...,
        id: str | None = ...,
        display_name: str | None = ...,
        uri: str | None = ...,
        email_address: str | None = ...,
    ) -> None: ...
    def startElement(self, name, attrs, connection): ...
    def endElement(self, name: str, value: Any, connection: S3Connection) -> None: ...
    def to_xml(self) -> str: ...
