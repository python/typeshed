from _typeshed import Incomplete

log: Incomplete

class HTTPClient:
    @classmethod
    def request(cls, method, url, headers, params, data, timeout, proxies, verify, max_retries) -> None: ...

class RequestClient(HTTPClient):
    @classmethod
    def request(cls, method, url, headers, params, data, timeout, proxies, verify, max_retries): ...

class URLFetchClient(HTTPClient):
    @classmethod
    def request(cls, method, url, headers, params, data, timeout, proxies, verify, max_retries): ...
    @classmethod
    def raise_on_status(cls, result) -> None: ...

def resolve_http_client(): ...
