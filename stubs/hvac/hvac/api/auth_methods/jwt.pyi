from _typeshed import Incomplete

from hvac.api.vault_api_base import VaultApiBase

class JWT(VaultApiBase):
    DEFAULT_PATH: str
    def resolve_path(self, path): ...
    def configure(
        self,
        oidc_discovery_url: Incomplete | None = ...,
        oidc_discovery_ca_pem: Incomplete | None = ...,
        oidc_client_id: Incomplete | None = ...,
        oidc_client_secret: Incomplete | None = ...,
        oidc_response_mode: Incomplete | None = ...,
        oidc_response_types: Incomplete | None = ...,
        jwks_url: Incomplete | None = ...,
        jwks_ca_pem: Incomplete | None = ...,
        jwt_validation_pubkeys: Incomplete | None = ...,
        bound_issuer: Incomplete | None = ...,
        jwt_supported_algs: Incomplete | None = ...,
        default_role: Incomplete | None = ...,
        provider_config: Incomplete | None = ...,
        path: Incomplete | None = ...,
    ): ...
    def read_config(self, path: Incomplete | None = ...): ...
    def create_role(
        self,
        name,
        user_claim,
        allowed_redirect_uris,
        role_type: str = ...,
        bound_audiences: Incomplete | None = ...,
        clock_skew_leeway: Incomplete | None = ...,
        expiration_leeway: Incomplete | None = ...,
        not_before_leeway: Incomplete | None = ...,
        bound_subject: Incomplete | None = ...,
        bound_claims: Incomplete | None = ...,
        groups_claim: Incomplete | None = ...,
        claim_mappings: Incomplete | None = ...,
        oidc_scopes: Incomplete | None = ...,
        bound_claims_type: str = ...,
        verbose_oidc_logging: bool = ...,
        token_ttl: Incomplete | None = ...,
        token_max_ttl: Incomplete | None = ...,
        token_policies: Incomplete | None = ...,
        token_bound_cidrs: Incomplete | None = ...,
        token_explicit_max_ttl: Incomplete | None = ...,
        token_no_default_policy: Incomplete | None = ...,
        token_num_uses: Incomplete | None = ...,
        token_period: Incomplete | None = ...,
        token_type: Incomplete | None = ...,
        path: Incomplete | None = ...,
        user_claim_json_pointer: Incomplete | None = ...,
    ): ...
    def read_role(self, name, path: Incomplete | None = ...): ...
    def list_roles(self, path: Incomplete | None = ...): ...
    def delete_role(self, name, path: Incomplete | None = ...): ...
    def oidc_authorization_url_request(self, role, redirect_uri, path: Incomplete | None = ...): ...
    def oidc_callback(self, state, nonce, code, path: Incomplete | None = ...): ...
    def jwt_login(self, role, jwt, use_token: bool = ..., path: Incomplete | None = ...): ...
