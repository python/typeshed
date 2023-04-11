from types import TracebackType
from typing import Any

KERNEL_VERSION: tuple[int, int]

class GPIOError(IOError): ...

class EdgeEvent:
    def __new__(cls, edge: str, timestamp: int) -> EdgeEvent: ...  # noqa: Y034

class GPIO:
    def __new__(cls, *args: Any, **kwargs: Any) -> GPIO: ...  # noqa: Y034
    def __del__(self) -> None: ...
    def __enter__(self) -> GPIO: ...  # noqa: Y034
    def __exit__(self, t: type[BaseException] | None, value: BaseException | None, traceback: TracebackType | None) -> None: ...
    def read(self) -> bool: ...
    def write(self, value: bool) -> None: ...
    def poll(self, timeout: float | None = ...) -> bool: ...
    def read_event(self) -> EdgeEvent: ...
    @staticmethod
    def poll_multiple(gpios: list[GPIO], timeout: float | None = ...) -> list[GPIO]: ...
    def close(self) -> None: ...
    @property
    def devpath(self) -> str: ...
    @property
    def fd(self) -> int: ...
    @property
    def line(self) -> int: ...
    @property
    def name(self) -> str: ...
    @property
    def label(self) -> str: ...
    @property
    def chip_fd(self) -> int: ...
    @property
    def chip_name(self) -> str: ...
    @property
    def chip_label(self) -> str: ...
    direction: str
    edge: str
    bias: str
    drive: str
    inverted: bool

class CdevGPIO(GPIO):
    def __init__(
        self,
        path: str,
        line: int | str,
        direction: str,
        edge: str = ...,
        bias: str = ...,
        drive: str = ...,
        inverted: bool = ...,
        label: str | None = ...,
    ) -> None: ...
    def __new__(self, path: str, line: int | str, direction: str, **kwargs: Any) -> CdevGPIO: ...  # noqa: Y034

class SysfsGPIO(GPIO):
    GPIO_OPEN_RETRIES: int
    GPIO_OPEN_DELAY: float
    def __init__(self, line: int, direction: str) -> None: ...
    def __new__(self, line: int, direction: str) -> SysfsGPIO: ...  # noqa: Y034
