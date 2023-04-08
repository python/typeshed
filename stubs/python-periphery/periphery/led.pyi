from types import TracebackType

class LEDError(IOError): ...

class LED:
    def __init__(self, name: str, brightness: bool | int | None = ...) -> None: ...
    def __del__(self) -> None: ...
    def __enter__(self) -> LED: ...  # noqa: Y034
    def __exit__(self, t: type[BaseException] | None, value: BaseException | None, traceback: TracebackType | None) -> None: ...
    def read(self) -> int: ...
    def write(self, brightness: bool | int) -> None: ...
    def close(self) -> None: ...
    @property
    def devpath(self) -> str: ...
    @property
    def fd(self) -> int: ...
    @property
    def name(self) -> str: ...
    @property
    def max_brightness(self) -> int: ...
    brightness: int
