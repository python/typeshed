from _typeshed import Incomplete, SupportsItems
from abc import ABC, abstractmethod
from re import Pattern
from typing import ClassVar, Generic, TypeVar
from typing_extensions import Literal

from .encryption import StandardSecurityHandler

_T = TypeVar("_T")

def clear_empty_fields(d): ...
def create_dictionary_string(
    dict_,
    open_dict: str = '<<',
    close_dict: str = '>>',
    field_join: str = '\n',
    key_value_join: str = ' ',
    has_empty_fields: bool = False,
): ...
def create_list_string(list_): ...
def iobj_ref(n): ...
def create_stream(
    stream: str | bytes | bytearray, encryption_handler: StandardSecurityHandler | None = None, obj_id: Incomplete | None = None
): ...

class Raw(str): ...

class Name(str):
    NAME_ESC: ClassVar[Pattern[bytes]]
    def serialize(self) -> str: ...

class PDFObject:
    def __init__(self) -> None: ...
    @property
    def id(self) -> int: ...
    @id.setter
    def id(self, n: int) -> None: ...
    @property
    def ref(self) -> str: ...
    def serialize(self, obj_dict: Incomplete | None = None, _security_handler: StandardSecurityHandler | None = None) -> str: ...
    def content_stream(self) -> bytes: ...

class PDFContentStream(PDFObject):
    filter: Name | None
    length: int
    def __init__(self, contents: bytes, compress: bool = False) -> None: ...
    def encrypt(self, security_handler: StandardSecurityHandler) -> None: ...

def build_obj_dict(key_values: SupportsItems[str, Incomplete]) -> dict[str, str]: ...
def camel_case(snake_case: str) -> str: ...

class PDFString(str):
    USE_HEX_ENCODING: ClassVar[bool]
    def serialize(self) -> str: ...

class PDFArray(list[_T], Generic[_T]):
    def serialize(self) -> str: ...

class Destination(ABC):
    @abstractmethod
    def serialize(self) -> str: ...

class DestinationXYZ(Destination):
    page_number: int
    top: float
    left: float
    zoom: float | Literal["null"]
    page_ref: Incomplete | None
    def __init__(self, page: int, top: float, left: float = 0, zoom: float | Literal["null"] = 'null') -> None: ...
    def serialize(self) -> str: ...
