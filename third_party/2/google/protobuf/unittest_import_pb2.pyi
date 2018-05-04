from google.protobuf.message import (
    Message,
)
from typing import (
    List,
    Optional,
    Tuple,
    cast,
)


class ImportEnum(int):

    @classmethod
    def Name(cls, number: int) -> str: ...

    @classmethod
    def Value(cls, name: str) -> ImportEnum: ...

    @classmethod
    def keys(cls) -> List[str]: ...

    @classmethod
    def values(cls) -> List[ImportEnum]: ...

    @classmethod
    def items(cls) -> List[Tuple[str, ImportEnum]]: ...


IMPORT_FOO = cast(ImportEnum, 7)
IMPORT_BAR = cast(ImportEnum, 8)
IMPORT_BAZ = cast(ImportEnum, 9)


class ImportEnumForMap(int):

    @classmethod
    def Name(cls, number: int) -> str: ...

    @classmethod
    def Value(cls, name: str) -> ImportEnumForMap: ...

    @classmethod
    def keys(cls) -> List[str]: ...

    @classmethod
    def values(cls) -> List[ImportEnumForMap]: ...

    @classmethod
    def items(cls) -> List[Tuple[str, ImportEnumForMap]]: ...


UNKNOWN = cast(ImportEnumForMap, 0)
FOO = cast(ImportEnumForMap, 1)
BAR = cast(ImportEnumForMap, 2)


class ImportMessage(Message):
    d = ...  # type: int

    def __init__(self,
                 d: Optional[int] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: str) -> ImportMessage: ...
