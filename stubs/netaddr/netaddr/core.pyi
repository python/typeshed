from _typeshed import Incomplete, SupportsWrite
from collections.abc import Iterator, Mapping
from typing_extensions import Final

BIG_ENDIAN_PLATFORM: bool
P: Final = 1
INET_PTON: Final = 1
Z: Final = 2
ZEROFILL: Final = 2
N: Final = 4
NOHOST: Final = 4

class AddrFormatError(Exception): ...
class AddrConversionError(Exception): ...
class NotRegisteredError(Exception): ...

def num_bits(int_val: int) -> int: ...

class Subscriber:
    def update(self, data: Incomplete) -> None: ...

class PrettyPrinter(Subscriber):
    fh: SupportsWrite[str]
    write_eol: bool
    def __init__(self, fh: SupportsWrite[str] = ..., write_eol: bool = True) -> None: ...
    def update(self, data: object) -> None: ...

class Publisher:
    subscribers: list[Subscriber]
    def __init__(self) -> None: ...
    def attach(self, subscriber: Subscriber) -> None: ...
    def detach(self, subscriber: Subscriber) -> None: ...
    def notify(self, data: object) -> None: ...

class DictDotLookup:
    def __init__(self, d: Mapping[str, object]) -> None: ...
    def __getitem__(self, name: str) -> object: ...
    def __iter__(self) -> Iterator[str]: ...
