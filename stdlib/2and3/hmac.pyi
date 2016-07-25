# Stubs for hmac

from typing import Any, Callable, Optional, Union, overload
from types import ModuleType
import sys

# TODO more precise type for object of hashlib
_Hash = Any

def new(key: Union[bytes,bytearray],
        msg: Optional[Union[bytes, bytearray]] = ...,
        digestmod: Optional[Union[str, Callable[[], _Hash], ModuleType]] = ...) -> HMAC: ...

class HMAC:
    digest_size = ...  # type: int
    if sys.version_info >= (3, 4):
        block_size = ...  # type: int
        name = ...  # type: str
    def update(self, msg: Union[bytes, bytearray]) -> None: ...
    def digest(self) -> bytes: ...
    def hexdigest(self) -> str: ...
    def copy(self) -> HMAC: ...

@overload
def compare_digest(a: str, b: str) -> bool: ...
@overload
def compare_digest(a: bytes, b: bytes) -> bool: ...
@overload
def compare_digest(a: bytearray, b: bytearray) -> bool: ...
