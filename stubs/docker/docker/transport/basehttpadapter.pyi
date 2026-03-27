from collections.abc import Mapping

import requests.adapters
from typing_extensions import override
from urllib3 import ConnectionPool

class BaseHTTPAdapter(requests.adapters.HTTPAdapter):
    @override
    def close(self) -> None: ...
    @override
    def get_connection_with_tls_context(
        self,
        request: requests.PreparedRequest,
        verify: bool | str | None,
        proxies: Mapping[str, str] | None = None,
        cert: tuple[str, str] | str | None = None,
    ) -> ConnectionPool: ...
