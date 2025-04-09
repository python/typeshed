from _typeshed import FileDescriptorOrPath, Incomplete, ReadableBuffer
from logging import Logger
from typing import Final

INDEX_NAME: Final[str]
INDEX_URL: Final[str]
TOKEN_USERNAME: Final[str]
log: Logger

def resolve_repository_name(repo_name: str) -> tuple[str, str]: ...
def resolve_index_name(index_name: str) -> str: ...
def get_config_header(client, registry) -> bytes | None: ...
def split_repo_name(repo_name: str) -> tuple[str, str]: ...
def get_credential_store(authconfig: AuthConfig | dict[str, Incomplete], registry: str | None): ...

class AuthConfig(dict[str, Incomplete]):
    def __init__(self, dct: dict[str, Incomplete], credstore_env: Incomplete | None = None) -> None: ...
    @classmethod
    def parse_auth(
        cls, entries: dict[str, dict[Incomplete, Incomplete]], raise_on_error: bool = False
    ) -> dict[str, Incomplete]: ...
    @classmethod
    def load_config(
        cls,
        config_path: FileDescriptorOrPath | None,
        config_dict: dict[str, Incomplete] | None,
        credstore_env: Incomplete | None = None,
    ) -> AuthConfig: ...
    @property
    def auths(self) -> dict[str, Incomplete]: ...
    @property
    def creds_store(self): ...
    @property
    def cred_helpers(self): ...
    @property
    def is_empty(self) -> bool: ...
    def resolve_authconfig(self, registry: str | None = None): ...
    def get_credential_store(self, registry: str | None): ...
    def get_all_credentials(self): ...
    def add_auth(self, reg: str, data) -> None: ...

def resolve_authconfig(authconfig, registry: str | None = None, credstore_env: Incomplete | None = None): ...
def convert_to_hostname(url: str) -> str: ...
def decode_auth(auth: str | ReadableBuffer) -> tuple[str, str]: ...
def encode_header(auth) -> bytes: ...
def parse_auth(entries: dict[Incomplete, Incomplete], raise_on_error: bool = False): ...
def load_config(
    config_path: FileDescriptorOrPath | None = None,
    config_dict: dict[str, Incomplete] | None = None,
    credstore_env: Incomplete | None = None,
) -> AuthConfig: ...
