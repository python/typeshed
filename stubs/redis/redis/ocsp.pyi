from _typeshed import Incomplete
from typing import Any

class OCSPVerifier:
    SOCK: Any
    HOST: Any
    PORT: Any
    CA_CERTS: Any
    def __init__(self, sock, host, port, ca_certs: Incomplete | None = ...) -> None: ...
    def components_from_socket(self): ...
    def components_from_direct_connection(self): ...
    def build_certificate_url(self, server, cert, issuer_cert): ...
    def check_certificate(self, server, cert, issuer_url): ...
    def is_valid(self): ...
