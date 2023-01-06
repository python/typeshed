from _typeshed import Incomplete

from ldap3.protocol.novell import CreateGroupTypeResponseValue

from ...extend.operation import ExtendedOperation

class StartTransaction(ExtendedOperation):
    request_name: str
    response_name: str
    request_value: Incomplete
    asn1_spec: CreateGroupTypeResponseValue | None
    def config(self) -> None: ...
    def __init__(self, connection, controls: Incomplete | None = ...) -> None: ...
    def populate_result(self) -> None: ...
    response_value: Incomplete
    def set_response(self) -> None: ...
