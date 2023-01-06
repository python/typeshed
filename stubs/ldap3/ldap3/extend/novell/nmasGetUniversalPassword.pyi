from _typeshed import Incomplete

from ldap3.protocol.novell import NmasGetUniversalPasswordResponseValue

from ...extend.operation import ExtendedOperation

class NmasGetUniversalPassword(ExtendedOperation):
    request_name: str
    response_name: str
    request_value: Incomplete
    asn1_spec: NmasGetUniversalPasswordResponseValue | None
    response_attribute: str
    def config(self) -> None: ...
    def __init__(self, connection, user, controls: Incomplete | None = ...) -> None: ...
    def populate_result(self) -> None: ...
