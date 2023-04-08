import ctypes
from _typeshed import Incomplete

KERNEL_VERSION: Incomplete

class SPIError(IOError): ...
class _CSpiIocTransfer(ctypes.Structure): ...

class SPI:
    def __init__(
        self, devpath, mode, max_speed, bit_order: str = ..., bits_per_word: int = ..., extra_flags: int = ...
    ) -> None: ...
    def __del__(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, t, value, traceback) -> None: ...
    def transfer(self, data): ...
    def close(self) -> None: ...
    @property
    def fd(self): ...
    @property
    def devpath(self): ...
    mode: Incomplete
    max_speed: Incomplete
    bit_order: Incomplete
    bits_per_word: Incomplete
    extra_flags: Incomplete
