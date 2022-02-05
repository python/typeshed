from _typeshed import StrOrBytesPath, SupportsRead
from typing import Any, Sequence

from tokenizer import tokenize as tokenize

g_token_cache: dict[str, list[tuple[str, str]]]  # undocumented

def render(
    template: SupportsRead[str] | str = ...,
    data: dict[str, Any] = ...,
    partials_path: StrOrBytesPath | None = ...,
    partials_ext: str = ...,
    partials_dict: dict[str, str] = ...,
    padding: str = ...,
    def_ldel: str | None = ...,
    def_rdel: str | None = ...,
    scopes: Sequence[int] = ...,
    warn: bool = ...,
) -> str: ...
