from types import TracebackType

KERNEL_VERSION: tuple[int, int]

class SPIError(IOError): ...

class SPI:
    def __init__(
        self, devpath: str, mode: int, max_speed: float, bit_order: str = ..., bits_per_word: int = ..., extra_flags: int = ...
    ) -> None: ...
    def __del__(self) -> None: ...
    def __enter__(self) -> SPI: ...  # noqa: Y034
    def __exit__(self, t: type[BaseException] | None, value: BaseException | None, traceback: TracebackType | None) -> None: ...
    def transfer(self, data: bytes | bytearray | list[int]) -> bytes | bytearray | list[int]: ...
    def close(self) -> None: ...
    @property
    def fd(self) -> int: ...
    @property
    def devpath(self) -> str: ...
    mode: int
    max_speed: float
    bit_order: str
    bits_per_word: int
    extra_flags: int
