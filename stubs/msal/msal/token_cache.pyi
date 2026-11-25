from collections.abc import Callable, Generator, Mapping
from logging import Logger
from typing import Any, Final
from typing_extensions import deprecated

logger: Logger

def is_subdict_of(small: Mapping[str, Any], big: Mapping[str, Any]) -> bool: ...

class TokenCache:
    class CredentialType:
        ACCESS_TOKEN: Final = "AccessToken"
        ACCESS_TOKEN_EXTENDED: Final = "atext"
        REFRESH_TOKEN: Final = "RefreshToken"
        ACCOUNT: Final = "Account"
        ID_TOKEN: Final = "IdToken"
        APP_METADATA: Final = "AppMetadata"

    class AuthorityType:
        ADFS: Final = "ADFS"
        MSSTS: Final = "MSSTS"

    key_makers: dict[str, Callable[..., str]]
    def __init__(self) -> None: ...
    def search(
        self,
        credential_type: str,
        target: list[str] | None = None,
        query: Mapping[str, Any] | None = None,
        *,
        now: float | None = None,
    ) -> Generator[dict[str, Any]]: ...
    @deprecated("Use list(search(...)) instead to explicitly get a list.")
    def find(
        self,
        credential_type: str,
        target: list[str] | None = None,
        query: Mapping[str, Any] | None = None,
        *,
        now: float | None = None,
    ) -> list[dict[str, Any]]: ...
    def add(self, event: Mapping[str, Any], now: float | None = None) -> None: ...
    def modify(
        self, credential_type: str, old_entry: Mapping[str, Any], new_key_value_pairs: Mapping[str, Any] | None = None
    ) -> None: ...
    def remove_rt(self, rt_item: Mapping[str, Any]) -> None: ...
    def update_rt(self, rt_item: Mapping[str, Any], new_rt: str) -> None: ...
    def remove_at(self, at_item: Mapping[str, Any]) -> None: ...
    def remove_idt(self, idt_item: Mapping[str, Any]) -> None: ...
    def remove_account(self, account_item: Mapping[str, Any]) -> None: ...

class SerializableTokenCache(TokenCache):
    has_state_changed: bool
    def add(self, event: Mapping[str, Any], *, now: float | None = None) -> None: ...  # type: ignore[override]
    def deserialize(self, state: str | None) -> None: ...
    def serialize(self) -> str: ...
