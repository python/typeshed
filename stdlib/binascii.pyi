import sys
from typing import Union

def a2b_uu(__data: Union[str, bytes]) -> bytes: ...

if sys.version_info >= (3, 7):
    def b2a_uu(__data: bytes, *, backtick: bool = ...) -> bytes: ...

else:
    def b2a_uu(__data: bytes) -> bytes: ...

def a2b_base64(__data: Union[str, bytes]) -> bytes: ...
def b2a_base64(__data: bytes, *, newline: bool = ...) -> bytes: ...
def a2b_qp(data: Union[str, bytes], header: bool = ...) -> bytes: ...
def b2a_qp(data: bytes, quotetabs: bool = ..., istext: bool = ..., header: bool = ...) -> bytes: ...
def a2b_hqx(__data: Union[str, bytes]) -> bytes: ...
def rledecode_hqx(__data: bytes) -> bytes: ...
def rlecode_hqx(__data: bytes) -> bytes: ...
def b2a_hqx(__data: bytes) -> bytes: ...
def crc_hqx(__data: bytes, __crc: int) -> int: ...
def crc32(__data: bytes, __crc: int = ...) -> int: ...
def b2a_hex(__data: bytes) -> bytes: ...

if sys.version_info >= (3, 8):
    def hexlify(data: bytes, sep: Union[str, bytes] = ..., bytes_per_sep: int = ...) -> bytes: ...

else:
    def hexlify(__data: bytes) -> bytes: ...

def a2b_hex(__hexstr: Union[str, bytes]) -> bytes: ...
def unhexlify(__hexstr: Union[str, bytes]) -> bytes: ...

class Error(ValueError): ...
class Incomplete(Exception): ...
