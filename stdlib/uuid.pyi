import builtins
import sys
from _typeshed import Unused
from enum import Enum
from typing import Final, NoReturn
from typing_extensions import LiteralString, TypeAlias

_FieldsType: TypeAlias = tuple[int, int, int, int, int, int]

class SafeUUID(Enum):
    safe = 0
    unsafe = -1
    unknown = None

class UUID:
    __slots__ = ("int", "is_safe", "__weakref__")

    is_safe: Final[SafeUUID]
    bytes: Final[builtins.bytes]
    bytes_le: Final[builtins.bytes]
    clock_seq: Final[builtins.int]
    clock_seq_hi_variant: Final[builtins.int]
    clock_seq_low: Final[builtins.int]
    fields: Final[_FieldsType]
    hex: Final[str]
    int: Final[builtins.int]
    node: Final[builtins.int]
    time: Final[builtins.int]
    time_hi_version: Final[builtins.int]
    time_low: Final[builtins.int]
    time_mid: Final[builtins.int]
    urn: Final[str]
    variant: Final[str]
    version: Final[builtins.int | None]

    def __init__(
        self,
        hex: str | None = None,
        bytes: builtins.bytes | None = None,
        bytes_le: builtins.bytes | None = None,
        fields: _FieldsType | None = None,
        int: builtins.int | None = None,
        version: builtins.int | None = None,
        *,
        is_safe: SafeUUID = SafeUUID.unknown,
    ) -> None: ...
    def __int__(self) -> builtins.int: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: UUID) -> bool: ...
    def __le__(self, other: UUID) -> bool: ...
    def __gt__(self, other: UUID) -> bool: ...
    def __ge__(self, other: UUID) -> bool: ...
    def __hash__(self) -> builtins.int: ...
    def __setattr__(self, name: Unused, value: Unused) -> NoReturn: ...

def getnode() -> int: ...
def uuid1(node: int | None = None, clock_seq: int | None = None) -> UUID: ...

if sys.version_info >= (3, 14):
    def uuid6(node: int | None = None, clock_seq: int | None = None) -> UUID: ...
    def uuid7() -> UUID: ...
    def uuid8(a: int | None = None, b: int | None = None, c: int | None = None) -> UUID: ...

if sys.version_info >= (3, 12):
    def uuid3(namespace: UUID, name: str | bytes) -> UUID: ...

else:
    def uuid3(namespace: UUID, name: str) -> UUID: ...

def uuid4() -> UUID: ...

if sys.version_info >= (3, 12):
    def uuid5(namespace: UUID, name: str | bytes) -> UUID: ...

else:
    def uuid5(namespace: UUID, name: str) -> UUID: ...

if sys.version_info >= (3, 14):
    NIL: Final[UUID]
    MAX: Final[UUID]

NAMESPACE_DNS: Final[UUID]
NAMESPACE_URL: Final[UUID]
NAMESPACE_OID: Final[UUID]
NAMESPACE_X500: Final[UUID]
RESERVED_NCS: Final[LiteralString]
RFC_4122: Final[LiteralString]
RESERVED_MICROSOFT: Final[LiteralString]
RESERVED_FUTURE: Final[LiteralString]

if sys.version_info >= (3, 12):
    def main() -> None: ...
