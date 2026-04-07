import enum
import ssl
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from requests import PreparedRequest, Response
from requests.adapters import HTTPAdapter

@dataclass
class MdsMtlsConfig:
    ca_cert_path: Path = ...
    client_combined_cert_path: Path = ...

class MdsMtlsMode(enum.Enum):

    STRICT = "strict"
    NONE = "none"
    DEFAULT = "default"

def _get_mds_root_crt_path() -> Path: ...
def _get_mds_client_combined_cert_path() -> Path: ...
def should_use_mds_mtls(mds_mtls_config: MdsMtlsConfig = ...) -> bool: ...

class MdsMtlsAdapter(HTTPAdapter):
    ssl_context: ssl.SSLContext

    def __init__(self, mds_mtls_config: MdsMtlsConfig = ..., *args: Any, **kwargs: Any) -> None: ...
    def init_poolmanager(self, *args: Any, **kwargs: Any) -> None: ...
    def proxy_manager_for(self, *args: Any, **kwargs: Any) -> None: ...
    def send(
        self,
        request: PreparedRequest,
        stream: bool = ...,
        timeout: float | tuple[float, float] | tuple[float, None] | None = ...,
        verify: bool | str = ...,
        cert: bytes | str | tuple[bytes | str, bytes | str] | None = ...,
        proxies: Mapping[str, str] | None = ...,
    ) -> Response: ...
