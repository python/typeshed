from _typeshed import Incomplete

from ldap3.protocol.novell import NmasSetUniversalPasswordResponseValue

from ...extend.operation import ExtendedOperation

class NmasSetUniversalPassword(ExtendedOperation):
    request_name: str
    response_name: str
    request_value: Incomplete
    asn1_spec: NmasSetUniversalPasswordResponseValue | None
    response_attribute: str
    def config(self) -> None: ...
    def __init__(self, connection, user, new_password, controls: Incomplete | None = ...) -> None: ...
    def populate_result(self) -> None: ...
