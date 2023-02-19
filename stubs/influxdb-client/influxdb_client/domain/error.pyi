from _typeshed import Incomplete

class Error:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        code: Incomplete | None = ...,
        message: Incomplete | None = ...,
        op: Incomplete | None = ...,
        err: Incomplete | None = ...,
    ) -> None: ...
    @property
    def code(self): ...
    @code.setter
    def code(self, code) -> None: ...
    @property
    def message(self): ...
    @message.setter
    def message(self, message) -> None: ...
    @property
    def op(self): ...
    @op.setter
    def op(self, op) -> None: ...
    @property
    def err(self): ...
    @err.setter
    def err(self, err) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
