import abc
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Any

import google
import google.auth
import google.auth.transport
from google.auth import credentials

@dataclass
class SupplierContext:
    subject_token_type: str
    audience: str

class Credentials(
    credentials.Scoped,
    credentials.CredentialsWithQuotaProject,
    credentials.CredentialsWithTokenUri,
    credentials.CredentialsWithTrustBoundary,
    metaclass=abc.ABCMeta,
):
    def __init__(
        self,
        audience: str,
        subject_token_type: str,
        token_url: str,
        credential_source: Mapping[str, Any],
        service_account_impersonation_url: str | None = None,
        service_account_impersonation_options: Mapping[str, str] | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        token_info_url: str | None = None,
        quota_project_id: str | None = None,
        scopes: Sequence[str] | None = None,
        default_scopes: Sequence[str] | None = None,
        workforce_pool_user_project: str | None = None,
        universe_domain: str = credentials.DEFAULT_UNIVERSE_DOMAIN,
        trust_boundary: Mapping[str, str] | None = None,
    ) -> None: ...
    @property
    def info(self) -> Mapping[str, Any]: ...
    @property
    def service_account_email(self) -> str | None: ...
    @property
    def is_user(self) -> bool: ...
    @property
    def is_workforce_pool(self) -> bool: ...
    @property
    def requires_scopes(self) -> bool: ...
    @property
    def project_number(self) -> str | None: ...
    @property
    def token_info_url(self) -> str | None: ...
    def get_cred_info(self) -> Mapping[str, str] | None: ...
    def with_scopes(self, scopes: Sequence[str], default_scopes: Sequence[str] | None = None) -> Credentials: ...
    @abc.abstractmethod
    def retrieve_subject_token(self, request: google.auth.transport.Request) -> str: ...
    def get_project_id(self, request: google.auth.transport.Request) -> str | None: ...
    def refresh(self, request: google.auth.transport.Request) -> None: ...
    def with_quota_project(self, quota_project_id: str | None) -> Credentials: ...
    def with_token_uri(self, token_uri: str) -> Credentials: ...
    def with_universe_domain(self, universe_domain: str) -> Credentials: ...
    def with_trust_boundary(self, trust_boundary: Mapping[str, str] | None) -> Credentials: ...
    @classmethod
    def from_info(cls, info: Mapping[str, Any], **kwargs: Any) -> Credentials: ...
    @classmethod
    def from_file(cls, filename: str, **kwargs: Any) -> Credentials: ...
