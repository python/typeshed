from _typeshed import Incomplete

from influxdb_client import Configuration

LOGGERS_NAMES: Incomplete

class _BaseClient:
    url: Incomplete
    token: Incomplete
    org: Incomplete
    default_tags: Incomplete
    conf: Incomplete
    auth_header_name: Incomplete
    auth_header_value: Incomplete
    retries: Incomplete
    profilers: Incomplete
    def __init__(
        self,
        url,
        token,
        debug: Incomplete | None = ...,
        timeout: int = ...,
        enable_gzip: bool = ...,
        org: str = ...,
        default_tags: dict[Incomplete, Incomplete] = ...,
        http_client_logger: str = ...,
        **kwargs,
    ) -> None: ...

class _BaseQueryApi:
    default_dialect: Incomplete
    def __init__(self, influxdb_client, query_options: Incomplete | None = ...) -> None: ...

class _BaseWriteApi:
    def __init__(self, influxdb_client, point_settings: Incomplete | None = ...) -> None: ...

class _BaseDeleteApi:
    def __init__(self, influxdb_client) -> None: ...

class _Configuration(Configuration):
    enable_gzip: bool
    username: Incomplete
    password: Incomplete
    def __init__(self) -> None: ...
    def update_request_header_params(self, path: str, params: dict[Incomplete, Incomplete]): ...
    def update_request_body(self, path: str, body): ...
