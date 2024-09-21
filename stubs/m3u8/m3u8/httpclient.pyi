import urllib.request
from typing import Any, Protocol, type_check_only

@type_check_only
class HTTPClientProtocol(Protocol):
    def download(
        self, uri: str, timeout: float | None = None, headers: dict[str, Any] = {}, verify_ssl: bool = True
    ) -> tuple[str, str]: ...

class DefaultHTTPClient(HTTPClientProtocol):
    proxies: dict[str, str] | None

    def __init__(self, proxies: dict[str, str] | None = None) -> None: ...

class HTTPSHandler(urllib.request.HTTPSHandler):
    # return a urllib.request.HTTPSHandler
    def __new__(cls, verify_ssl: bool = True) -> urllib.request.HTTPSHandler: ...  # type: ignore # pyright: ignore[reportInconsistentConstructor]
