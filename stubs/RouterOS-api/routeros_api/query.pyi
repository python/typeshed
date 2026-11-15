from typing import ClassVar, Protocol, type_check_only

# A query a command filters its rows by.
@type_check_only
class _Query(Protocol):
    def get_api_format(self) -> list[bytes]: ...

# A str key or value is encoded.
class BasicQuery:
    operator: ClassVar[bytes | None]
    key: bytes
    value: bytes
    def __init__(self, key: str | bytes, value: str | bytes) -> None: ...
    def get_api_format(self) -> list[bytes]: ...

class IsEqualQuery(BasicQuery):
    operator: ClassVar[bytes]

class IsLessQuery(BasicQuery):
    operator: ClassVar[bytes]

class IsGreaterQuery(BasicQuery):
    operator: ClassVar[bytes]

class HasValueQuery:
    key: bytes
    def __init__(self, key: str | bytes) -> None: ...
    def get_api_format(self) -> list[bytes]: ...

class OperatorQuery:
    operator: ClassVar[bytes | None]
    others: tuple[_Query, ...]
    def __init__(self, *others: _Query) -> None: ...
    def get_api_format(self) -> list[bytes]: ...

class OrQuery(OperatorQuery):
    operator: ClassVar[bytes]

class AndQuery(OperatorQuery):
    operator: ClassVar[bytes]

class NandQuery(AndQuery): ...
