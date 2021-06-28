from typing import Any

from . import treewalkers as treewalkers
from .constants import (
    booleanAttributes as booleanAttributes,
    entities as entities,
    rcdataElements as rcdataElements,
    spaceCharacters as spaceCharacters,
    voidElements as voidElements,
    xmlEntities as xmlEntities,
)

v: Any

def htmlentityreplace_errors(exc): ...
def serialize(input, tree: str = ..., encoding: Any | None = ..., **serializer_opts): ...

class HTMLSerializer:
    quote_attr_values: str
    quote_char: str
    use_best_quote_char: bool
    omit_optional_tags: bool
    minimize_boolean_attributes: bool
    use_trailing_solidus: bool
    space_before_trailing_solidus: bool
    escape_lt_in_attrs: bool
    escape_rcdata: bool
    resolve_entities: bool
    alphabetical_attributes: bool
    inject_meta_charset: bool
    strip_whitespace: bool
    sanitize: bool
    options: Any
    errors: Any
    strict: bool
    def __init__(self, **kwargs) -> None: ...
    def encode(self, string): ...
    def encodeStrict(self, string): ...
    encoding: Any
    def serialize(self, treewalker, encoding: Any | None = ...) -> None: ...
    def render(self, treewalker, encoding: Any | None = ...): ...
    def serializeError(self, data: str = ...) -> None: ...

class SerializeError(Exception): ...
