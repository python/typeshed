class Response:
    def __init__(self, response) -> None: ...
    @property
    def status_code(self): ...
    @property
    def body(self): ...
    @property
    def headers(self): ...
    @property
    def to_dict(self): ...

class Client:
    methods: set[str]
    host: str
    request_headers: dict[str, str]
    append_slash: bool
    timeout: int
    def __init__(
        self,
        host,
        request_headers: dict[str, str] | None = None,
        version: int | None = None,
        url_path: list[str] | None = None,
        append_slash: bool = False,
        timeout: int | None = None,
    ) -> None: ...
    def _(self, name): ...
    def __getattr__(self, name): ...
