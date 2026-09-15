from _typeshed import Incomplete
from collections.abc import Mapping
from typing import Any, TypeAlias

LDAPTokenDictValue: TypeAlias = tuple[()] | tuple[str, ...]
LDAPTokenDict: TypeAlias = Mapping[str, LDAPTokenDictValue]
TOKENS_FINDALL: Incomplete
UNESCAPE_PATTERN: Incomplete

def split_tokens(s: str) -> list[str]: ...
def parse_tokens(tokens: list[str], known_tokens: list[str]) -> tuple[str, LDAPTokenDict]: ...
def extract_tokens(l: list[str], known_tokens: Mapping[str, Any]) -> dict[str, Any]: ...
