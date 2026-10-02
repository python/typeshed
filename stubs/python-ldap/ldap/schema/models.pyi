from _typeshed import SupportsKeysAndGetItem
from collections.abc import Iterable
from typing import Any, overload
from collections import UserDict

from ldap.schema.tokenizer import extract_tokens as extract_tokens, split_tokens as split_tokens

NOT_HUMAN_READABLE_LDAP_SYNTAXES: Any  # TODO: Precise type

class SchemaElement:
    token_defaults: Any  # TODO: Precise type
    def __init__(self, schema_element_str: Any | None = None) -> None: ...
    oid: Any  # TODO: Precise type
    def set_id(self, element_id) -> None: ...
    def get_id(self): ...
    def key_attr(self, key, value, quoted: int = 0): ...
    def key_list(self, key, values, sep: str = " ", quoted: int = 0): ...

class ObjectClass(SchemaElement):
    schema_attribute: str
    token_defaults: Any  # TODO: Precise type

AttributeUsage: Any  # TODO: Precise type

class AttributeType(SchemaElement):
    schema_attribute: str
    token_defaults: Any  # TODO: Precise type

class LDAPSyntax(SchemaElement):
    schema_attribute: str
    token_defaults: Any  # TODO: Precise type

class MatchingRule(SchemaElement):
    schema_attribute: str
    token_defaults: Any  # TODO: Precise type

class MatchingRuleUse(SchemaElement):
    schema_attribute: str
    token_defaults: Any  # TODO: Precise type

class DITContentRule(SchemaElement):
    schema_attribute: str
    token_defaults: Any  # TODO: Precise type

class DITStructureRule(SchemaElement):
    schema_attribute: str
    token_defaults: Any  # TODO: Precise type
    ruleid: Any  # TODO: Precise type
    def set_id(self, element_id) -> None: ...
    def get_id(self): ...

class NameForm(SchemaElement):
    schema_attribute: str
    token_defaults: Any  # TODO: Precise type

class Entry(UserDict[Any, Any]):
    dn: Any  # TODO: Precise type
    def __init__(self, schema, dn, entry) -> None: ...

    @overload
    def update(self, other: SupportsKeysAndGetItem[Any, Any], /, **kwargs: Any) -> None: ...
    @overload
    def update(self, other: Iterable[tuple[Any, Any]], /, **kwargs: Any) -> None: ...
    @overload
    def update(self, **kwargs: Any) -> None: ...

    def __contains__(self, nameoroid) -> bool: ...
    def __getitem__(self, nameoroid): ...
    def __setitem__(self, nameoroid, attr_values) -> None: ...
    def __delitem__(self, nameoroid) -> None: ...
    def has_key(self, nameoroid): ...
    def keys(self): ...
    def items(self): ...
    def attribute_types(
        self, attr_type_filter: Any | None = None, raise_keyerror: int = 1
    ): ...  # TODO: Precise type for attr_type_filter
