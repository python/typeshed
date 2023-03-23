from _typeshed import StrOrBytesPath
from collections.abc import Iterable
from typing import IO, Any
from typing_extensions import Literal

import webob.static  # type:ignore  # pyright:ignore[reportMissingTypeStubs]  # FIXME: Remove once types-WebOb exists
from fanstatic.core import Library
from fanstatic.injector import _StartResponse, _WSGIApplication
from fanstatic.registry import LibraryRegistry
from webob import (  # type:ignore  # pyright:ignore[reportMissingTypeStubs]  # FIXME: Remove once types-WebOb exists
    Request,
    Response,
)

MINUTE_IN_SECONDS: Literal[60]
HOUR_IN_SECONDS: Literal[3600]
DAY_IN_SECONDS: Literal[86400]
YEAR_IN_SECONDS: int
FOREVER: int

class BundleApp(webob.static.FileApp):  # pyright:ignore[reportUntypedBaseClass]
    filenames: list[str]
    def __init__(self, rootpath: str, bundle: IO[bytes], filenames: Iterable[StrOrBytesPath]) -> None: ...
    def __call__(self, req: Request) -> Response: ...

class LibraryPublisher(webob.static.DirectoryApp):  # pyright:ignore[reportUntypedBaseClass]
    ignores: list[str]
    library: Library
    cached_apps: dict[str, webob.static.FileApp]
    def __init__(self, library: Library) -> None: ...
    def __call__(self, req: Request) -> Response: ...

class Publisher:
    registry: LibraryRegistry
    directory_publishers: dict[str, LibraryPublisher]
    def __init__(self, registry: LibraryRegistry) -> None: ...
    def __call__(self, request: Request) -> Response: ...

class Delegator:
    app: _WSGIApplication
    publisher: Publisher
    publisher_signature: str
    trigger: str
    def __init__(self, app: _WSGIApplication, publisher: Publisher, publisher_signature: str = ...) -> None: ...
    def is_resource(self, request: Request) -> bool: ...
    def __call__(self, environ: dict[str, Any], start_response: _StartResponse) -> Iterable[bytes]: ...

def make_publisher(global_config) -> Publisher: ...
