from _typeshed import StrOrBytesPath
from _typeshed.wsgi import StartResponse, WSGIApplication
from collections.abc import Iterable
from typing import IO, Any
from typing_extensions import Literal

import webob
import webob.dec
import webob.static
from fanstatic.core import Library
from fanstatic.registry import LibraryRegistry

MINUTE_IN_SECONDS: Literal[60]
HOUR_IN_SECONDS: Literal[3600]
DAY_IN_SECONDS: Literal[86400]
YEAR_IN_SECONDS: int
FOREVER: int

class BundleApp(webob.static.FileApp):
    filenames: list[str]
    def __init__(self, rootpath: str, bundle: IO[bytes], filenames: Iterable[StrOrBytesPath]) -> None: ...
    def __call__(self, req: webob.Request) -> webob.Response: ...

class LibraryPublisher(webob.static.DirectoryApp):
    ignores: list[str]
    library: Library
    cached_apps: dict[str, webob.static.FileApp]
    def __init__(self, library: Library) -> None: ...
    @webob.dec.wsgify
    def __call__(self, req: webob.static.Request) -> webob.Response: ...

class Publisher:
    registry: LibraryRegistry
    directory_publishers: dict[str, LibraryPublisher]
    def __init__(self, registry: LibraryRegistry) -> None: ...
    @webob.dec.wsgify
    def __call__(self, request: webob.Request) -> webob.Response: ...

class Delegator:
    app: WSGIApplication
    publisher: Publisher
    publisher_signature: str
    trigger: str
    def __init__(self, app: WSGIApplication, publisher: Publisher, publisher_signature: str = ...) -> None: ...
    def is_resource(self, request: webob.Request) -> bool: ...
    def __call__(self, environ: dict[str, Any], start_response: StartResponse) -> Iterable[bytes]: ...

def make_publisher(global_config: Any) -> Publisher: ...
