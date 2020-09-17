from typing import Any, Dict, Text, TypeVar, Union

from google.protobuf.message import Message

_M = TypeVar("_M", bound=Message)

class Error(Exception): ...
class ParseError(Error): ...
class SerializeToJsonError(Error): ...

def MessageToJson(
    message: Message,
    including_default_value_fields: bool = ...,
    preserving_proto_field_name: bool = ...,
    indent: int = ...,
    sort_keys: bool = ...,
    use_integers_for_enums: bool = ...,
) -> str: ...
def MessageToDict(
    message: Message,
    including_default_value_fields: bool = ...,
    preserving_proto_field_name: bool = ...,
    use_integers_for_enums: bool = ...,
) -> Dict[Text, Any]: ...
def Parse(text: Union[bytes, Text], message: _M, ignore_unknown_fields: bool = ...) -> _M: ...
def ParseDict(js_dict: Any, message: _M, ignore_unknown_fields: bool = ...) -> _M: ...
