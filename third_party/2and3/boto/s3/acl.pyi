from .connection import S3Connection
from .user import User
from typing import Any, Dict, Optional, List, Text, Union

CannedACLStrings = ...  # type: List[str]

class Policy:
    parent = ...  # type: Any
    namespace = ...  # type: Any
    acl = ...  # type: ACL
    def __init__(self, parent: Optional[Any] = ...) -> None: ...
    owner = ...  # type: User
    def startElement(self, name: Text, attrs: Dict[str, Any], connection: S3Connection) -> Union[None, User, ACL]: ...
    def endElement(self, name: Text, value: Any, connection: S3Connection) -> None: ...
    def to_xml(self) -> str: ...

class ACL:
    policy = ...  # type: Policy
    grants = ...  # type: List[Grant]
    def __init__(self, policy: Optional[Policy] = ...) -> None: ...
    def add_grant(self, grant: Grant) -> None: ...
    def add_email_grant(self, permission: Text, email_address: Text) -> None: ...
    def add_user_grant(self, permission: Text, user_id: Text, display_name: Optional[Text] = ...) -> None: ...
    def startElement(self, name, attrs, connection): ...
    def endElement(self, name: Text, value: Any, connection: S3Connection) -> None: ...
    def to_xml(self) -> str: ...

class Grant:
    NameSpace = ...  # type: Text
    permission = ...  # type: Text
    id = ...  # type: Text
    display_name = ...  # type: Text
    uri = ...  # type: Text
    email_address = ...  # type: Text
    type = ...  # type: Text
    def __init__(self, permission: Optional[Text] = ..., type: Optional[Text] = ..., id: Optional[Text] = ..., display_name: Optional[Text] = ..., uri: Optional[Text] = ..., email_address: Optional[Text] = ...) -> None: ...
    def startElement(self, name, attrs, connection): ...
    def endElement(self, name: Text, value: Any, connection: S3Connection) -> None: ...
    def to_xml(self) -> str: ...
