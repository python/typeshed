import abc
from collections.abc import Mapping
from typing import Any

from google.auth import external_account

EXECUTABLE_SUPPORTED_MAX_VERSION: int
EXECUTABLE_TIMEOUT_MILLIS_DEFAULT: int
EXECUTABLE_TIMEOUT_MILLIS_LOWER_BOUND: int
EXECUTABLE_TIMEOUT_MILLIS_UPPER_BOUND: int
EXECUTABLE_INTERACTIVE_TIMEOUT_MILLIS_LOWER_BOUND: int
EXECUTABLE_INTERACTIVE_TIMEOUT_MILLIS_UPPER_BOUND: int

class Credentials(external_account.Credentials, metaclass=abc.ABCMeta):
    interactive: bool

    def __init__(
        self,
        audience: str,
        subject_token_type: str,
        token_url: str,
        credential_source: Mapping[str, Any] | None = None,
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
    def retrieve_subject_token(self, request: Any) -> Any: ...
    def revoke(self, request: Any) -> None: ...
    @property
    def external_account_id(self) -> str | None: ...
    @classmethod
    def from_info(cls, info: Mapping[str, Any], **kwargs: Any) -> Credentials: ...
    @classmethod
    def from_file(cls, filename: str, **kwargs: Any) -> Credentials: ...
