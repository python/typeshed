# Stubs for werkzeug.test (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from urllib.request import Request as U2Request
from http.cookiejar import CookieJar

def stream_encode_multipart(values, use_tempfile=True, threshold=..., boundary=None, charset=''): ...
def encode_multipart(values, boundary=None, charset=''): ...
def File(fd, filename=None, mimetype=None): ...

class _TestCookieHeaders:
    headers = ...  # type: Any
    def __init__(self, headers): ...
    def getheaders(self, name): ...
    def get_all(self, name, default=None): ...

class _TestCookieResponse:
    headers = ...  # type: Any
    def __init__(self, headers): ...
    def info(self): ...

class _TestCookieJar(CookieJar):
    def inject_wsgi(self, environ): ...
    def extract_wsgi(self, environ, headers): ...

class EnvironBuilder:
    server_protocol = ...  # type: Any
    wsgi_version = ...  # type: Any
    request_class = ...  # type: Any
    charset = ...  # type: Any
    path = ...  # type: Any
    base_url = ...  # type: Any
    query_string = ...  # type: Any
    args = ...  # type: Any
    method = ...  # type: Any
    headers = ...  # type: Any
    content_type = ...  # type: Any
    errors_stream = ...  # type: Any
    multithread = ...  # type: Any
    multiprocess = ...  # type: Any
    run_once = ...  # type: Any
    environ_base = ...  # type: Any
    environ_overrides = ...  # type: Any
    input_stream = ...  # type: Any
    content_length = ...  # type: Any
    closed = ...  # type: Any
    def __init__(self, path='', base_url=None, query_string=None, method='', input_stream=None, content_type=None, content_length=None, errors_stream=None, multithread=False, multiprocess=False, run_once=False, headers=None, data=None, environ_base=None, environ_overrides=None, charset=''): ...
    def form_property(name, storage, doc): ...
    form = ...  # type: Any
    files = ...  # type: Any
    @property
    def server_name(self): ...
    @property
    def server_port(self): ...
    def __del__(self): ...
    def close(self): ...
    def get_environ(self): ...
    def get_request(self, cls=None): ...

class ClientRedirectError(Exception): ...

class Client:
    application = ...  # type: Any
    response_wrapper = ...  # type: Any
    cookie_jar = ...  # type: Any
    allow_subdomain_redirects = ...  # type: Any
    def __init__(self, application, response_wrapper=None, use_cookies=True, allow_subdomain_redirects=False): ...
    def set_cookie(self, server_name, key, value='', max_age=None, expires=None, path='', domain=None, secure=None, httponly=False, charset=''): ...
    def delete_cookie(self, server_name, key, path='', domain=None): ...
    def run_wsgi_app(self, environ, buffered=False): ...
    def resolve_redirect(self, response, new_location, environ, buffered=False): ...
    def open(self, *args, **kwargs): ...
    def get(self, *args, **kw): ...
    def patch(self, *args, **kw): ...
    def post(self, *args, **kw): ...
    def head(self, *args, **kw): ...
    def put(self, *args, **kw): ...
    def delete(self, *args, **kw): ...
    def options(self, *args, **kw): ...
    def trace(self, *args, **kw): ...

def create_environ(*args, **kwargs): ...
def run_wsgi_app(app, environ, buffered=False): ...
