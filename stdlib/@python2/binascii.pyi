import sys
from typing import Text, Union

# Python 2 accepts unicode ascii pretty much everywhere.
_Bytes = Text
_Ascii = Text

def a2b_uu(__data: _Ascii) -> bytes: ...
def b2a_uu(__data: _Bytes) -> bytes: ...
def a2b_base64(__data: _Ascii) -> bytes: ...
def b2a_base64(__data: _Bytes) -> bytes: ...
def a2b_qp(data: _Ascii, header: bool = ...) -> bytes: ...
def b2a_qp(data: _Bytes, quotetabs: bool = ..., istext: bool = ..., header: bool = ...) -> bytes: ...
def a2b_hqx(__data: _Ascii) -> bytes: ...
def rledecode_hqx(__data: _Bytes) -> bytes: ...
def rlecode_hqx(__data: _Bytes) -> bytes: ...
def b2a_hqx(__data: _Bytes) -> bytes: ...
def crc_hqx(__data: _Bytes, __crc: int) -> int: ...
def crc32(__data: _Bytes, __crc: int = ...) -> int: ...
def b2a_hex(__data: _Bytes) -> bytes: ...
def hexlify(__data: _Bytes) -> bytes: ...
def a2b_hex(__hexstr: _Ascii) -> bytes: ...
def unhexlify(__hexstr: _Ascii) -> bytes: ...

class Error(ValueError): ...
class Incomplete(Exception): ...
