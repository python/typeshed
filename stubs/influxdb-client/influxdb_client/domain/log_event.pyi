from _typeshed import Incomplete

class LogEvent:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self, time: Incomplete | None = None, message: Incomplete | None = None, run_id: Incomplete | None = None
    ) -> None: ...
    @property
    def time(self): ...
    @time.setter
    def time(self, time) -> None: ...
    @property
    def message(self): ...
    @message.setter
    def message(self, message) -> None: ...
    @property
    def run_id(self): ...
    @run_id.setter
    def run_id(self, run_id) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
