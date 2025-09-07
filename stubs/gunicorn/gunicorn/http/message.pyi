from _typeshed import Incomplete

MAX_REQUEST_LINE: int
MAX_HEADERS: int
DEFAULT_MAX_HEADERFIELD_SIZE: int
RFC9110_5_6_2_TOKEN_SPECIALS: str
TOKEN_RE: Incomplete
METHOD_BADCHAR_RE: Incomplete
VERSION_RE: Incomplete
RFC9110_5_5_INVALID_AND_DANGEROUS: Incomplete

class Message:
    cfg: Incomplete
    unreader: Incomplete
    peer_addr: Incomplete
    remote_addr: Incomplete
    version: Incomplete
    headers: Incomplete
    trailers: Incomplete
    body: Incomplete
    scheme: Incomplete
    must_close: bool
    limit_request_fields: Incomplete
    limit_request_field_size: Incomplete
    max_buffer_headers: Incomplete
    def __init__(self, cfg, unreader, peer_addr) -> None: ...
    def force_close(self) -> None: ...
    def parse(self, unreader) -> None: ...
    def parse_headers(self, data, from_trailer: bool = False): ...
    def set_body_reader(self) -> None: ...
    def should_close(self): ...

class Request(Message):
    method: Incomplete
    uri: Incomplete
    path: Incomplete
    query: Incomplete
    fragment: Incomplete
    limit_request_line: Incomplete
    req_number: Incomplete
    proxy_protocol_info: Incomplete
    def __init__(self, cfg, unreader, peer_addr, req_number: int = 1) -> None: ...
    def get_data(self, unreader, buf, stop: bool = False) -> None: ...
    headers: Incomplete
    def parse(self, unreader): ...
    def read_line(self, unreader, buf, limit: int = 0): ...
    def proxy_protocol(self, line): ...
    def proxy_protocol_access_check(self) -> None: ...
    def parse_proxy_protocol(self, line) -> None: ...
    version: Incomplete
    def parse_request_line(self, line_bytes) -> None: ...
    body: Incomplete
    def set_body_reader(self) -> None: ...
