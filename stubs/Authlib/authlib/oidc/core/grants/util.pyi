from _typeshed import Incomplete

def is_openid_scope(scope): ...
def validate_request_prompt(grant, redirect_uri, redirect_fragment: bool = False): ...
def validate_nonce(request, exists_nonce, required: bool = False): ...
def generate_id_token(
    token,
    user_info,
    key,
    iss,
    aud,
    alg: str = "RS256",
    exp: int = 3600,
    nonce: Incomplete | None = None,
    auth_time: Incomplete | None = None,
    code: Incomplete | None = None,
): ...
def create_response_mode_response(redirect_uri, params, response_mode): ...
