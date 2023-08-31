from _typeshed import Incomplete

class UnexpectedStatusException(ValueError):
    allowed_statuses: Incomplete
    actual_status: Incomplete
    def __init__(self, message, allowed_statuses, actual_status) -> None: ...

class CapacityError(UnexpectedStatusException): ...

class AsyncInferenceError(Exception):
    fmt: str
    kwargs: Incomplete
    def __init__(self, **kwargs) -> None: ...

class ObjectNotExistedError(AsyncInferenceError):
    fmt: str
    def __init__(self, message, output_path) -> None: ...

class PollingTimeoutError(AsyncInferenceError):
    fmt: str
    def __init__(self, message, output_path, seconds) -> None: ...

class UnexpectedClientError(AsyncInferenceError):
    fmt: str
    def __init__(self, message) -> None: ...

class AutoMLStepInvalidModeError(Exception):
    fmt: str
    kwargs: Incomplete
    def __init__(self, **kwargs) -> None: ...

class AsyncInferenceModelError(AsyncInferenceError):
    fmt: str
    def __init__(self, message) -> None: ...
