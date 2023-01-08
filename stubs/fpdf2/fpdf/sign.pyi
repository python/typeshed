from _typeshed import Incomplete

class Signature:
    type: str
    filter: str
    sub_filter: str
    contact_info: Incomplete | None
    location: Incomplete | None
    m: Incomplete | None
    reason: Incomplete | None
    byte_range: str
    contents: str
    def __init__(
        self,
        contact_info: Incomplete | None = ...,
        location: Incomplete | None = ...,
        m: Incomplete | None = ...,
        reason: Incomplete | None = ...,
    ) -> None: ...
    def serialize(self): ...

def sign_content(signer, buffer, key, cert, extra_certs, hashalgo, sign_time): ...
