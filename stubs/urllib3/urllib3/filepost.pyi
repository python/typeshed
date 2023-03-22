from typing import Any, Iterable, Mapping, Sequence

from . import fields

RequestField = fields.RequestField

writer: Any

_TYPE_FIELDS_SEQUENCE = Sequence[tuple[str, _TYPE_FIELD_VALUE_TUPLE] | RequestField]
_TYPE_FIELDS = _TYPE_FIELDS_SEQUENCE | Mapping[str, _TYPE_FIELD_VALUE_TUPLE]

def choose_boundary() -> str: ...
def iter_field_objects(fields: _TYPE_FIELDS) -> Iterable[RequestField]: ...
def iter_fields(fields): ...
def encode_multipart_formdata(fields: _TYPE_FIELDS, boundary: str | None = ...) -> tuple[bytes, str]: ...
