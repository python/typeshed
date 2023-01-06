from _typeshed import Incomplete

from pyasn1.type.base import Asn1Type

class ExtendedOperation:
    connection: Incomplete
    decoded_response: Incomplete
    result: Incomplete
    asn1_spec: Asn1Type | None
    request_name: Incomplete
    response_name: Incomplete
    request_value: Incomplete
    response_value: Incomplete
    response_attribute: Incomplete
    controls: Incomplete
    def __init__(self, connection, controls: Incomplete | None = ...) -> None: ...
    def send(self): ...
    def populate_result(self) -> None: ...
    def decode_response(self, response: Incomplete | None = ...) -> None: ...
    def set_response(self) -> None: ...
    def config(self) -> None: ...
