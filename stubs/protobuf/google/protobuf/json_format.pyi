from typing import Any, TypeVar

from google.protobuf.descriptor_pool import DescriptorPool
from google.protobuf.message import Message

_MessageT = TypeVar("_MessageT", bound=Message)

class Error(Exception): ...
class ParseError(Error): ...
class SerializeToJsonError(Error): ...

def MessageToJson(
    message: Message,
    including_default_value_fields: bool = False,
    preserving_proto_field_name: bool = False,
    indent: int | None = 2,
    sort_keys: bool = False,
    use_integers_for_enums: bool = False,
    descriptor_pool: DescriptorPool | None = None,
    float_precision: int | None = None,
    ensure_ascii: bool = True,
) -> str: ...
def MessageToDict(
    message: Message,
    including_default_value_fields: bool = False,
    preserving_proto_field_name: bool = False,
    use_integers_for_enums: bool = False,
    descriptor_pool: DescriptorPool | None = None,
    float_precision: int | None = None,
) -> dict[str, Any]: ...
def Parse(
    text: bytes | str,
    message: _MessageT,
    ignore_unknown_fields: bool = False,
    descriptor_pool: DescriptorPool | None = None,
    max_recursion_depth: int = 100,
) -> _MessageT: ...
def ParseDict(
    js_dict: Any,
    message: _MessageT,
    ignore_unknown_fields: bool = False,
    descriptor_pool: DescriptorPool | None = None,
    max_recursion_depth: int = 100,
) -> _MessageT: ...
