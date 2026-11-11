from typing import Final

class PopAuthScheme:
    HTTP_GET: Final = "GET"
    HTTP_POST: Final = "POST"
    HTTP_PUT: Final = "PUT"
    HTTP_DELETE: Final = "DELETE"
    HTTP_PATCH: Final = "PATCH"
    def __init__(self, http_method: str | None = None, url: str | None = None, nonce: str | None = None) -> None: ...
