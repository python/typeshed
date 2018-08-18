
import ssl
from typing import Any, AnyStr, Dict, List, Union, Optional, Mapping, Callable, Sequence, Tuple, Type
from urllib import addinfourl
from httplib import HTTPResponse

_string = Union[str, unicode]

class URLError(IOError):
    reason = ...  # type: Union[str, BaseException]

class HTTPError(URLError, addinfourl):
    code = ...  # type: int
    headers = ...  # type: Dict[str, str]
    def __init__(self, url, code, msg, hdrs, fp) -> None: ...

class Request(object):
    host = ...  # type: str
    port = ...  # type: str
    data = ...  # type: str
    headers = ...  # type: Dict[str, str]
    unverifiable = ...  # type: bool
    type = ...  # type: Optional[str]
    origin_req_host = ...
    unredirected_hdrs = ...

    def __init__(self, url: str, data: Optional[str] = ..., headers: Dict[str, str] = ...,
                 origin_req_host: Optional[str] = ..., unverifiable: bool = ...) -> None: ...
    def __getattr__(self, attr): ...
    def get_method(self) -> str: ...
    def add_data(self, data) -> None: ...
    def has_data(self) -> bool: ...
    def get_data(self) -> str: ...
    def get_full_url(self) -> str: ...
    def get_type(self): ...
    def get_host(self) -> str: ...
    def get_selector(self): ...
    def set_proxy(self, host, type) -> None: ...
    def has_proxy(self) -> bool: ...
    def get_origin_req_host(self) -> str: ...
    def is_unverifiable(self) -> bool: ...
    def add_header(self, key: str, val: str) -> None: ...
    def add_unredirected_header(self, key: str, val: str) -> None: ...
    def has_header(self, header_name: str) -> bool: ...
    def get_header(self, header_name: str, default: Optional[str] = ...) -> str: ...
    def header_items(self): ...

class OpenerDirector(object):
    def add_handler(self, handler: BaseHandler) -> None: ...
    def open(self, url: Union[Request, _string], data: Optional[_string] = ..., timeout: int = ...): ...
    def error(self, proto: _string, *args: Any): ...

def urlopen(url: Union[Request, _string], data: Optional[_string] = ..., timeout: int = ...,
            cafile: Optional[_string] = ..., capath: Optional[_string] = ..., cadefault: bool = ...,
            context: Optional[ssl.SSLContext] = ...): ...
def install_opener(opener: OpenerDirector) -> None: ...
def build_opener(*handlers: Union[BaseHandler, Type[BaseHandler]]) -> OpenerDirector: ...

class BaseHandler:
    handler_order = ...  # type: int
    parent = ...  # type: OpenerDirector

    def add_parent(self, parent: OpenerDirector) -> None: ...
    def close(self) -> None: ...
    def __lt__(self, other: Any) -> bool: ...

class HTTPErrorProcessor(BaseHandler):
    def http_response(self, request, response): ...

class HTTPDefaultErrorHandler(BaseHandler):
    def http_error_default(self, req, fp, code, msg, hdrs): ...

class HTTPRedirectHandler(BaseHandler):
    max_repeats = ...  # type: int
    max_redirections = ...  # type: int
    def redirect_request(self, req, fp, code, msg, headers, newurl): ...
    def http_error_301(self, req, fp, code, msg, headers): ...
    def http_error_302(self, req, fp, code, msg, headers): ...
    def http_error_303(self, req, fp, code, msg, headers): ...
    def http_error_307(self, req, fp, code, msg, headers): ...
    inf_msg = ...  # type: str


class ProxyHandler(BaseHandler):
    def __init__(self, proxies=None): ...
    def proxy_open(self, req, proxy, type): ...

class HTTPPasswordMgr:
    def __init__(self) -> None: ...
    def add_password(self, realm: _string, uri: Union[_string, Sequence[_string]], user: _string, passwd: _string) -> None: ...
    def find_user_password(self, realm: _string, authuri: _string) -> Tuple[Any, Any]: ...
    def reduce_uri(self, uri: _string, default_port: bool = ...) -> Tuple[Any, Any]: ...
    def is_suburi(self, base: _string, test: _string) -> bool: ...

class HTTPPasswordMgrWithDefaultRealm(HTTPPasswordMgr): ...

class AbstractBasicAuthHandler:
    def __init__(self, password_mgr: Optional[HTTPPasswordMgr] = ...) -> None: ...
    def http_error_auth_reqed(self, authreq, host, req, headers): ...
    def retry_http_basic_auth(self, host, req, realm): ...

class HTTPBasicAuthHandler(AbstractBasicAuthHandler, BaseHandler):
    auth_header = ...  # type: str
    def http_error_401(self, req, fp, code, msg, headers): ...

class ProxyBasicAuthHandler(AbstractBasicAuthHandler, BaseHandler):
    auth_header = ...  # type: str
    def http_error_407(self, req, fp, code, msg, headers): ...

class AbstractDigestAuthHandler:
    def __init__(self, passwd: Optional[HTTPPasswordMgr] = ...) -> None: ...
    def reset_retry_count(self) -> None: ...
    def http_error_auth_reqed(self, auth_header: str, host: str, req: Request,
                              headers: Mapping[str, str]) -> None: ...
    def retry_http_digest_auth(self, req: Request, auth: str) -> Optional[HTTPResponse]: ...
    def get_cnonce(self, nonce: str) -> str: ...
    def get_authorization(self, req: Request, chal: Mapping[str, str]) -> str: ...
    def get_algorithm_impls(self, algorithm: str) -> Tuple[Callable[[str], str], Callable[[str, str], str]]: ...
    def get_entity_digest(self, data: Optional[bytes], chal: Mapping[str, str]) -> Optional[str]: ...

class HTTPDigestAuthHandler(BaseHandler, AbstractDigestAuthHandler):
    auth_header = ...  # type: str
    handler_order = ...  # type: int
    def http_error_401(self, req, fp, code, msg, headers): ...

class ProxyDigestAuthHandler(BaseHandler, AbstractDigestAuthHandler):
    auth_header = ...  # type: str
    handler_order = ...  # type: int
    def http_error_407(self, req, fp, code, msg, headers): ...

class AbstractHTTPHandler(BaseHandler):
    def __init__(self, debuglevel: int = ...) -> None: ...
    def do_request_(self, request): ...
    def do_open(self, http_class, req): ...

class HTTPHandler(AbstractHTTPHandler):
    def http_open(self, req): ...
    def http_request(self, request): ...

class HTTPSHandler(AbstractHTTPHandler):
    def __init__(self, debuglevel=0, context=None): ...
    def https_open(self, req): ...
    def https_request(self, request): ...

class HTTPCookieProcessor(BaseHandler):
    def __init__(self, cookiejar=None): ...
    def http_request(self, request): ...
    def http_response(self, request, response): ...

class UnknownHandler(BaseHandler):
    def unknown_open(self, req): ...

class FileHandler(BaseHandler):
    def file_open(self, req): ...
    def get_names(self): ...
    def open_local_file(self, req): ...

class FTPHandler(BaseHandler):
    def ftp_open(self, req): ...
    def connect_ftp(self, user, passwd, host, port, dirs, timeout): ...

class CacheFTPHandler(FTPHandler):
    def __init__(self) -> None: ...
    def setTimeout(self, t): ...
    def setMaxConns(self, m): ...
    def check_cache(self): ...
    def clear_cache(self): ...

def parse_http_list(s: AnyStr) -> List[AnyStr]: ...
def parse_keqv_list(l: List[AnyStr]) -> Dict[AnyStr, AnyStr]: ...
