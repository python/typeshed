from typing import ClassVar, Protocol, type_check_only

# A query a command filters its rows by.
@type_check_only
class _Query(Protocol):
    def get_api_format(self) -> list[bytes]: ...

# A str key or value is encoded.
class BasicQuery:  # undocumented
    operator: ClassVar[bytes | None]
    key: bytes
    value: bytes
    def __init__(self, key: str | bytes, value: str | bytes) -> None: ...
    def get_api_format(self) -> list[bytes]: ...

class IsEqualQuery(BasicQuery):  # undocumented
    operator: ClassVar[bytes]

class IsLessQuery(BasicQuery):  # undocumented
    operator: ClassVar[bytes]

class IsGreaterQuery(BasicQuery):  # undocumented
    operator: ClassVar[bytes]

class HasValueQuery:  # undocumented
    key: bytes
    def __init__(self, key: str | bytes) -> None: ...
    def get_api_format(self) -> list[bytes]: ...

class OperatorQuery:  # undocumented
    operator: ClassVar[bytes | None]
    others: tuple[_Query, ...]
    def __init__(self, *others: _Query) -> None: ...
    def get_api_format(self) -> list[bytes]: ...

class OrQuery(OperatorQuery):  # undocumented
    operator: ClassVar[bytes]

class AndQuery(OperatorQuery):  # undocumented
    operator: ClassVar[bytes]

class NandQuery(AndQuery): ...  # undocumented
