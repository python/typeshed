from ldap3.protocol.novell import Identity

from ...extend.operation import ExtendedOperation

class GetBindDn(ExtendedOperation):
    request_name: str
    response_name: str
    response_attribute: str
    asn1_spec: Identity | None
    def config(self) -> None: ...
    def populate_result(self) -> None: ...
