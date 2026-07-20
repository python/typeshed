from typing import Literal

from .core import (
    EmptyRequestHeaders as EmptyRequestHeaders,
    Entry as Entry,
    HTTPrettyRequest as HTTPrettyRequest,
    HTTPrettyRequestEmpty as HTTPrettyRequestEmpty,
    URIInfo as URIInfo,
    URIMatcher as URIMatcher,
    get_default_thread_timeout as get_default_thread_timeout,
    httprettified as httprettified,
    httprettized as httprettized,
    httpretty as httpretty,
    set_default_thread_timeout as set_default_thread_timeout,
)
from .errors import HTTPrettyError as HTTPrettyError, UnmockedError as UnmockedError

__version__: str
HTTPretty = httpretty
activate = httprettified
enabled = httprettized
enable = httpretty.enable
register_uri = httpretty.register_uri
disable = httpretty.disable
is_enabled = httpretty.is_enabled
reset = httpretty.reset
Response = httpretty.Response
GET: Literal["GET"]
PUT: Literal["PUT"]
POST: Literal["POST"]
DELETE: Literal["DELETE"]
HEAD: Literal["HEAD"]
PATCH: Literal["PATCH"]
OPTIONS: Literal["OPTIONS"]
CONNECT: Literal["CONNECT"]

def last_request() -> HTTPrettyRequest | HTTPrettyRequestEmpty: ...
def latest_requests() -> list[HTTPrettyRequest]: ...
def has_request() -> bool: ...
