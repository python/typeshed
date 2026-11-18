from collections.abc import MutableMapping, Sequence
from typing import TypeAlias

__all__ = [
    "LDAPAddModList",
    "LDAPControlTuple",
    "LDAPControlTuples",
    "LDAPEntryDict",
    "LDAPModList",
    "LDAPModListAddEntry",
    "LDAPModListEntry",
    "LDAPModListModifyEntry",
    "LDAPModifyModList",
    "LDAPSearchResult",
]

LDAPModListAddEntry: TypeAlias = tuple[str, list[bytes]]
LDAPModListModifyEntry: TypeAlias = tuple[int, str, bytes | list[bytes] | None]
LDAPModListEntry: TypeAlias = LDAPModListAddEntry | LDAPModListModifyEntry
LDAPAddModList: TypeAlias = Sequence[LDAPModListAddEntry]
LDAPModifyModList: TypeAlias = Sequence[LDAPModListModifyEntry]
LDAPModList: TypeAlias = Sequence[LDAPModListEntry]
LDAPEntryDict: TypeAlias = MutableMapping[str, list[bytes]]
LDAPControlTuple: TypeAlias = tuple[str, str, str | None]
LDAPControlTuples: TypeAlias = list[LDAPControlTuple]
LDAPSearchResult: TypeAlias = tuple[str, LDAPEntryDict]
