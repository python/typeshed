from collections.abc import Iterable, Sequence
from typing import ClassVar, Final, Literal

from netaddr.fbsocket import AF_INET6

OPT_IMPORTS: bool
width: Literal[128]
word_size: Literal[16]
word_sep: Literal[":"]
family: Final = AF_INET6
family_name: Literal["IPv6"]
version: Literal[6]
word_base: Literal[16]
max_int: int
num_words: Literal[8]
max_word: int
prefix_to_netmask: dict[int, int]
netmask_to_prefix: dict[int, int]
prefix_to_hostmask: dict[int, int]
hostmask_to_prefix: dict[int, int]

class ipv6_compact:
    word_fmt: ClassVar[str]
    compact: ClassVar[bool]

class ipv6_full(ipv6_compact): ...
class ipv6_verbose(ipv6_compact): ...

def valid_str(addr: str, flags: int = 0) -> bool: ...
def str_to_int(addr: str, flags: int = 0) -> int: ...
def int_to_str(int_val: int, dialect: type[ipv6_compact] | None = None) -> str: ...
def int_to_arpa(int_val: int) -> str: ...
def int_to_packed(int_val: int) -> bytes: ...
def packed_to_int(packed_int: bytes) -> int: ...
def valid_words(words: Iterable[int]) -> bool: ...
def int_to_words(int_val: int, num_words: int | None = None, word_size: int | None = None) -> tuple[int, ...]: ...
def words_to_int(words: Sequence[int]) -> int: ...
def valid_bits(bits: str) -> bool: ...
def bits_to_int(bits: str) -> int: ...
def int_to_bits(int_val: int, word_sep: str | None = None) -> str: ...
def valid_bin(bin_val: str) -> bool: ...
def int_to_bin(int_val: int) -> str: ...
def bin_to_int(bin_val: str) -> int: ...
