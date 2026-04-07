from _typeshed import Incomplete
from collections.abc import Mapping
from typing import Any

import google
import google.auth
import google.auth.transport
from google.auth import credentials
from google.auth.crypt import Signer as _Signer

TOKEN_EXCHANGE_TYPE: str
ACCESS_TOKEN_TOKEN_TYPE: str
SERVICE_ACCOUNT_TOKEN_TYPE: str
JWT_LIFETIME: Incomplete

class ServiceAccountCredentials(credentials.Credentials):
    def __init__(
        self,
        signer: _Signer,
        service_identity_name: str,
        project: str,
        audience: str | None,
        token_uri: str,
        ca_cert_path: str | None,
    ) -> None: ...
    @classmethod
    def from_service_account_info(cls, info: Mapping[str, str], **kwargs: Any) -> ServiceAccountCredentials: ...
    @classmethod
    def from_service_account_file(cls, filename: str, **kwargs: Any) -> ServiceAccountCredentials: ...
    def refresh(self, request: google.auth.transport.Request) -> None: ...
    def with_gdch_audience(self, audience: str) -> ServiceAccountCredentials: ...
