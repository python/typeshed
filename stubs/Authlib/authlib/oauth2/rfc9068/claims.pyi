from _typeshed import Incomplete

from authlib.jose import JWTClaims

class JWTAccessTokenClaims(JWTClaims):
    REGISTERED_CLAIMS: Incomplete
    def validate(self, now: Incomplete | None = None, leeway: int = 0, **kwargs) -> None: ...
    def validate_typ(self) -> None: ...
    def validate_client_id(self): ...
    def validate_auth_time(self) -> None: ...
    def validate_acr(self): ...
    def validate_amr(self) -> None: ...
    def validate_scope(self): ...
    def validate_groups(self): ...
    def validate_roles(self): ...
    def validate_entitlements(self): ...
