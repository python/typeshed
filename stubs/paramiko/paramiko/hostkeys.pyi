from collections.abc import Iterator, Mapping, MutableMapping


from paramiko.pkey import PKey

class _SubDict(MutableMapping[str, PKey]):
    # Internal to HostKeys.lookup()
    def __init__(self, hostname: str, entries: list[HostKeyEntry], hostkeys: HostKeys) -> None: ...
    def __iter__(self) -> Iterator[str]: ...
    def __len__(self) -> int: ...
    def __delitem__(self, key: str) -> None: ...
    def __getitem__(self, key: str) -> PKey: ...
    def __setitem__(self, key: str, val: PKey) -> None: ...
    def keys(self) -> list[str]: ...  # type: ignore[override]

class HostKeys(MutableMapping[str, _SubDict]):
    def __init__(self, filename: str | None = ...) -> None: ...
    def add(self, hostname: str, keytype: str, key: PKey) -> None: ...
    def load(self, filename: str) -> None: ...
    def save(self, filename: str) -> None: ...
    def lookup(self, hostname: str) -> _SubDict | None: ...
    def check(self, hostname: str, key: PKey) -> bool: ...
    def clear(self) -> None: ...
    def __iter__(self) -> Iterator[str]: ...
    def __len__(self) -> int: ...
    def __getitem__(self, key: str) -> _SubDict: ...
    def __delitem__(self, key: str) -> None: ...
    def __setitem__(self, hostname: str, entry: Mapping[str, PKey]) -> None: ...
    def keys(self) -> list[str]: ...  # type: ignore[override]
    def values(self) -> list[_SubDict]: ...  # type: ignore[override]
    @staticmethod
    def hash_host(hostname: str, salt: str | None = ...) -> str: ...

class InvalidHostKey(Exception):
    line: str
    exc: Exception
    def __init__(self, line: str, exc: Exception) -> None: ...

class HostKeyEntry:
    valid: bool
    hostnames: list[str]
    key: PKey
    def __init__(self, hostnames: list[str] | None = ..., key: PKey | None = ...) -> None: ...
    @classmethod
    def from_line(cls, line: str, lineno: int | None = ...) -> HostKeyEntry | None: ...
    def to_line(self) -> str | None: ...
