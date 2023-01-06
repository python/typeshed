from _typeshed import Incomplete

from ldap3.protocol.novell import ReplicaList

from ...extend.operation import ExtendedOperation

class ListReplicas(ExtendedOperation):
    request_name: str
    response_name: str
    request_value: Incomplete
    asn1_spec: ReplicaList | None
    response_attribute: str
    def config(self) -> None: ...
    def __init__(self, connection, server_dn, controls: Incomplete | None = ...) -> None: ...
    def populate_result(self) -> None: ...
