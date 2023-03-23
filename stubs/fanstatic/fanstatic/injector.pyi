from abc import abstractmethod
from collections.abc import Callable, Iterable
from sys import _OptExcInfo
from typing import Any, Protocol
from typing_extensions import Literal, TypeAlias, TypedDict

from fanstatic.core import Dependable, NeededResources, Resource
from fanstatic.inclusion import Inclusion
from webob import (  # type:ignore  # pyright:ignore[reportMissingTypeStubs]  # FIXME: Remove once types-WebOb exists
    Request,
    Response,
)

class _NeededResourcesConfig(TypedDict, total=False):
    versioning: bool
    versioning_use_md5: bool
    recompute_hashes: bool
    base_url: str | None
    script_name: str | None
    publisher_signature: str
    resources: Iterable[Dependable] | None

class _StartResponse(Protocol):
    def __call__(
        self, __status: str, __headers: list[tuple[str, str]], __exc_info: _OptExcInfo | None = ...
    ) -> Callable[[bytes], object]: ...

_WSGIApplication: TypeAlias = Callable[[dict[str, Any], _StartResponse], Iterable[bytes]]

CONTENT_TYPES: list[str]

class Injector:
    app: _WSGIApplication
    config: _NeededResourcesConfig
    injector: InjectorPlugin
    def __init__(
        self, app: _WSGIApplication, injector: InjectorPlugin | None = ..., **config: Any
    ) -> None: ...  # FIXME: Switch to Unpack[_NeededResourcesConfig]
    def __call__(self, environ: dict[str, Any], start_response: _StartResponse) -> Iterable[bytes]: ...

class InjectorPlugin:
    @property
    @abstractmethod
    def name(self) -> str: ...
    def __init__(self, options: Any) -> None: ...  # FIXME: Use Unpack
    def make_inclusion(self, needed: NeededResources, resources: set[Resource] | None = None): ...
    def __call__(
        self, html: bytes, needed: NeededResources, request: Request | None = None, response: Response | None = None
    ) -> None: ...

class TopBottomInjector(InjectorPlugin):
    name: Literal["topbottom"]
    def __init__(self, options: Any) -> None: ...  # FIXME: Use Unpack
    def group(self, needed: NeededResources) -> tuple[Inclusion, Inclusion]: ...

def make_injector(app: _WSGIApplication, global_config: Any, **local_config: Any) -> Injector: ...
