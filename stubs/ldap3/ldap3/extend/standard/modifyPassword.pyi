from _typeshed import Incomplete

from ldap3.protocol.rfc3062 import PasswdModifyResponseValue

from ...extend.operation import ExtendedOperation

class ModifyPassword(ExtendedOperation):
    request_name: str
    request_value: Incomplete
    asn1_spec: PasswdModifyResponseValue | None
    response_attribute: str
    def config(self) -> None: ...
    def __init__(
        self,
        connection,
        user: Incomplete | None = ...,
        old_password: Incomplete | None = ...,
        new_password: Incomplete | None = ...,
        hash_algorithm: Incomplete | None = ...,
        salt: Incomplete | None = ...,
        controls: Incomplete | None = ...,
    ) -> None: ...
    def populate_result(self) -> None: ...
