from _typeshed import Incomplete

from hvac.api.auth_methods.jwt import JWT

class OIDC(JWT):
    DEFAULT_PATH: str
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
    ) -> None: ...
