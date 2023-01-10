from _typeshed import ReadableBuffer, StrOrBytesPath, SupportsRead
from typing import Any, TypeVar

_T = TypeVar("_T")

class _Readable(SupportsRead[_T]):
    def close(self) -> Any: ...

# SupportsRead type parameter is the same as pyexpat.XMLParserType.Parse's first argument
def read_string_table(xml_source: StrOrBytesPath | int | _Readable[str | ReadableBuffer]) -> list[str]: ...
