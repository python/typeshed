from authlib.oauth2.rfc6749 import ClientMixin
from authlib.oauth2.rfc9101 import JWTAuthenticationRequest

class OpenIDJWTAuthenticationRequest(JWTAuthenticationRequest):
    def get_client_request_uris(self, client: ClientMixin) -> list[str]: ...
