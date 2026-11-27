from _typeshed import Incomplete
from collections.abc import ItemsView, Iterator, KeysView, MutableMapping
from typing import ClassVar, TypeAlias
from typing_extensions import Self

import ldap.schema
from ldap._types import LDAPEntryDict as LDAPEntryDict
from ldap.cidict import cidict as cidict
from ldap.schema.subentry import SCHEMA_ATTR_MAPPING as SCHEMA_ATTR_MAPPING, SCHEMA_CLASS_MAPPING as SCHEMA_CLASS_MAPPING
from ldap.schema.tokenizer import LDAPTokenDict as LDAPTokenDict, parse_tokens as parse_tokens, split_tokens as split_tokens

EntryBase: TypeAlias = MutableMapping[str, list[bytes]]
NOT_HUMAN_READABLE_LDAP_SYNTAXES: Incomplete

class SchemaElement:
    oid: str
    names: tuple[str, ...]
    desc: str | None
    schema_attribute: ClassVar[str]
    known_tokens: ClassVar[list[str]]
    def __init__(self, schema_element_str: str | bytes | None = None) -> None: ...
    def _set_attrs(self, l: list[str], d: LDAPTokenDict) -> None: ...
    def set_id(self, element_id: str) -> None: ...
    def get_id(self) -> str: ...
    def key_attr(self, key: str, value: str | None, quoted: int = 0) -> str: ...
    def key_list(self, key: str, values: tuple[str, ...], sep: str = " ", quoted: int = 0) -> str: ...

class ObjectClass(SchemaElement):
    schema_attribute: str
    known_tokens: ClassVar[list[str]]
    obsolete: Incomplete
    must: Incomplete
    may: Incomplete
    x_origin: Incomplete
    kind: int
    sup: tuple[str, ...]
    def _set_attrs(self, l: list[str], d: LDAPTokenDict) -> None: ...

AttributeUsage: Incomplete

class AttributeType(SchemaElement):
    schema_attribute: str
    known_tokens: ClassVar[list[str]]
    obsolete: Incomplete
    sup: Incomplete
    equality: Incomplete
    ordering: Incomplete
    substr: Incomplete
    x_origin: Incomplete
    x_ordered: Incomplete
    syntax: Incomplete
    syntax_len: Incomplete
    single_value: Incomplete
    collective: Incomplete
    no_user_mod: Incomplete
    usage: int
    def _set_attrs(self, l: list[str], d: LDAPTokenDict) -> None: ...

class LDAPSyntax(SchemaElement):
    schema_attribute: str
    known_tokens: ClassVar[list[str]]
    x_subst: Incomplete
    not_human_readable: Incomplete
    x_binary_transfer_required: Incomplete
    def _set_attrs(self, l: list[str], d: LDAPTokenDict) -> None: ...

class MatchingRule(SchemaElement):
    schema_attribute: str
    known_tokens: ClassVar[list[str]]
    obsolete: Incomplete
    syntax: Incomplete
    def _set_attrs(self, l: list[str], d: LDAPTokenDict) -> None: ...

class MatchingRuleUse(SchemaElement):
    schema_attribute: str
    known_tokens: ClassVar[list[str]]
    obsolete: Incomplete
    applies: Incomplete
    def _set_attrs(self, l: list[str], d: LDAPTokenDict) -> None: ...

class DITContentRule(SchemaElement):
    schema_attribute: str
    known_tokens: ClassVar[list[str]]
    obsolete: Incomplete
    aux: Incomplete
    must: Incomplete
    may: Incomplete
    nots: Incomplete
    def _set_attrs(self, l: list[str], d: LDAPTokenDict) -> None: ...

class DITStructureRule(SchemaElement):
    schema_attribute: str
    known_tokens: ClassVar[list[str]]
    ruleid: Incomplete
    def set_id(self, element_id: str) -> None: ...
    def get_id(self) -> str: ...
    obsolete: Incomplete
    form: Incomplete
    sup: Incomplete
    def _set_attrs(self, l: list[str], d: LDAPTokenDict) -> None: ...

class NameForm(SchemaElement):
    schema_attribute: str
    known_tokens: ClassVar[list[str]]
    obsolete: Incomplete
    oc: Incomplete
    must: Incomplete
    may: Incomplete
    def _set_attrs(self, l: list[str], d: LDAPTokenDict) -> None: ...

class Entry(EntryBase):
    _keytuple2attrtype: dict[tuple[str, ...], str]
    _attrtype2keytuple: dict[str, tuple[str, ...]]
    data: dict[tuple[str, ...], list[bytes]]
    _s: Incomplete
    dn: Incomplete
    def __init__(self, schema: ldap.schema.subentry.SubSchema, dn: str, entry: LDAPEntryDict) -> None: ...
    def _at2key(self, nameoroid: str) -> tuple[str, ...]: ...
    def __contains__(self, nameoroid: object) -> bool: ...
    def __getitem__(self, nameoroid: object) -> list[bytes]: ...
    def __setitem__(self, nameoroid: object, attr_values: list[bytes]) -> None: ...
    def __delitem__(self, nameoroid: object) -> None: ...
    def __len__(self) -> int: ...
    def has_key(self, nameoroid: str) -> bool: ...
    def keys(self) -> KeysView[str]: ...
    def items(self) -> ItemsView[str, list[bytes]]: ...
    def __iter__(self) -> Iterator[str]: ...
    def copy(self) -> Self: ...
    __copy__ = copy
    def attribute_types(
        self, attr_type_filter: list[tuple[str, list[str]]] | None = None, raise_keyerror: int = 1
    ) -> tuple[cidict[AttributeType | None], cidict[AttributeType | None]]: ...
