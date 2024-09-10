from _typeshed import Incomplete

from httpx import Request

HTTPX_CLIENT_KWARGS: Incomplete

def extract_client_kwargs(kwargs): ...
def build_request(url, headers, body, initial_request: Request) -> Request: ...
