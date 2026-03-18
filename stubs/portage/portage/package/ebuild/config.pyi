from collections.abc import Mapping
from typing import Literal, TypeVar

class config:
    def __init__(
        self,
        clone: config | None = None,
        mycpv: str | None = None,
        config_profile_path: str | None = None,
        config_incrementals: dict[str, str] | None = None,
        config_root: str | None = None,
        target_root: str | None = None,
        sysroot: str | None = None,
        eprefix: str | None = None,
        local_config: bool = True,
        env: dict[str, str] | None = None,
        _unmatched_removal: bool = False,
        repositories: list[str] | None = None,
    ) -> None: ...
    def __getitem__(self, key: str) -> str: ...
    def __setitem__(self, key: str, value: str) -> None: ...
    def __delitem__(self, key: str) -> None: ...
    def __iter__(self) -> str: ...
    def get(self, k: str, x=...): ...

_K = TypeVar("_K")
_V = TypeVar("_V")

def best_from_dict(
    key: _K,
    top_dict: Mapping[_K, _V],
    key_order,
    EmptyOnError: Literal[0, 1] = 1,
    FullCopy: Literal[0, 1] = 1,
    AllowEmpty: Literal[0, 1] = 1,
) -> Literal[""] | dict[_K, _V]: ...
def autouse(myvartree, use_cache: Literal[0, 1] = 1, mysettings: config | None = None) -> Literal[""]: ...
