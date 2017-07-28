# Stubs for requests.sessions (Python 3)

from typing import Any, Union, MutableMapping, Text, Optional, IO, Tuple, Callable
from . import adapters
from . import auth
from . import compat
from . import cookies
from . import models
from .models import Response
from . import hooks
from . import utils
from . import exceptions
from .packages.urllib3 import _collections
from . import structures
from . import adapters
from . import status_codes

BaseAdapter = adapters.BaseAdapter
AuthBase = auth.AuthBase
OrderedDict = compat.OrderedDict
cookiejar_from_dict = cookies.cookiejar_from_dict
extract_cookies_to_jar = cookies.extract_cookies_to_jar
RequestsCookieJar = cookies.RequestsCookieJar
merge_cookies = cookies.merge_cookies
Request = models.Request
PreparedRequest = models.PreparedRequest
DEFAULT_REDIRECT_LIMIT = models.DEFAULT_REDIRECT_LIMIT
default_hooks = hooks.default_hooks
dispatch_hook = hooks.dispatch_hook
to_key_val_list = utils.to_key_val_list
default_headers = utils.default_headers
to_native_string = utils.to_native_string
TooManyRedirects = exceptions.TooManyRedirects
InvalidSchema = exceptions.InvalidSchema
ChunkedEncodingError = exceptions.ChunkedEncodingError
ContentDecodingError = exceptions.ContentDecodingError
RecentlyUsedContainer = _collections.RecentlyUsedContainer
CaseInsensitiveDict = structures.CaseInsensitiveDict
HTTPAdapter = adapters.HTTPAdapter
requote_uri = utils.requote_uri
get_environ_proxies = utils.get_environ_proxies
get_netrc_auth = utils.get_netrc_auth
should_bypass_proxies = utils.should_bypass_proxies
get_auth_from_url = utils.get_auth_from_url
codes = status_codes.codes
REDIRECT_STATI = models.REDIRECT_STATI

REDIRECT_CACHE_SIZE = ...  # type: Any

def merge_setting(request_setting, session_setting, dict_class=...): ...
def merge_hooks(request_hooks, session_hooks, dict_class=...): ...

class SessionRedirectMixin:
    def resolve_redirects(self, resp, req, stream=..., timeout=..., verify=..., cert=...,
                          proxies=...): ...
    def rebuild_auth(self, prepared_request, response): ...
    def rebuild_proxies(self, prepared_request, proxies): ...

_Data = Union[None, bytes, MutableMapping[Text, Text], IO]

class Session(SessionRedirectMixin):
    __attrs__ = ...  # type: Any
    headers = ...  # type: Optional[MutableMapping[Text, Text]]
    auth = ...  # type: Union[None, Tuple[Text, Text], AuthBase, Callable[[Request], Request]]
    proxies = ...  # type: Optional[MutableMapping[Text, Text]]
    hooks = ...  # type: Optional[MutableMapping[Text, Callable[[Request], Any]]]
    params = ...  # type: Union[None, bytes, MutableMapping[Text, Text]]
    stream = ...  # type: bool
    verify = ...  # type: Union[None, bool, Text]
    cert = ...  # type: Union[None, Text, Tuple[Text, Text]]
    max_redirects = ...  # type: int
    trust_env = ...  # type: bool
    cookies = ...  # type: Union[None, RequestsCookieJar, MutableMapping[Text, Text]]
    adapters = ...  # type: MutableMapping
    redirect_cache = ...  # type: RecentlyUsedContainer
    def __init__(self) -> None: ...
    def __enter__(self) -> 'Session': ...
    def __exit__(self, *args) -> None: ...
    def prepare_request(self, request): ...
    def request(self, method: str, url: str,
                params: Union[None, bytes, MutableMapping[Text, Text]] = ...,
                data: _Data = ...,
                headers: Optional[MutableMapping[Text, Text]] = ...,
                cookies: Union[None, RequestsCookieJar, MutableMapping[Text, Text]] = ...,
                files: Optional[MutableMapping[Text, IO]] = ...,
                auth: Union[None, Tuple[Text, Text], AuthBase, Callable[[Request], Request]] = ...,
                timeout: Union[None, float, Tuple[float, float]] = ...,
                allow_redirects: Optional[bool] = ...,
                proxies: Optional[MutableMapping[Text, Text]] = ...,
                hooks: Optional[MutableMapping[Text, Callable[[Request], Any]]] = ...,
                stream: Optional[bool] = ...,
                verify: Union[None, bool, Text] = ...,
                cert: Union[Text, Tuple[Text, Text], None] = ...,
                json: Optional[MutableMapping] = ...,
                ) -> Response: ...
    def get(self, url: Union[Text, bytes], **kwargs) -> Response: ...
    def options(self, url: Union[Text, bytes], **kwargs) -> Response: ...
    def head(self, url: Union[Text, bytes], **kwargs) -> Response: ...
    def post(self, url: Union[Text, bytes], data: _Data = ..., json: Optional[MutableMapping] = ..., **kwargs) -> Response: ...
    def put(self, url: Union[Text, bytes], data: _Data = ..., **kwargs) -> Response: ...
    def patch(self, url: Union[Text, bytes], data: _Data = ..., **kwargs) -> Response: ...
    def delete(self, url: Union[Text, bytes], **kwargs) -> Response: ...
    def send(self, request, **kwargs): ...
    def merge_environment_settings(self, url, proxies, stream, verify, cert): ...
    def get_adapter(self, url): ...
    def close(self) -> None: ...
    def mount(self, prefix:
              Union[Text, bytes],
              adapter: BaseAdapter) -> None: ...

def session() -> Session: ...
