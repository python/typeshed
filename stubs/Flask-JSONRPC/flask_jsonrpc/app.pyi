from collections.abc import Callable
from typing import Any
from typing_extensions import TypeAlias

from .blueprints import JSONRPCBlueprint
from .site import JSONRPCSite
from .views import JSONRPCView
from .wrappers import JSONRPCDecoratorMixin

Flask: TypeAlias = Any

class JSONRPC(JSONRPCDecoratorMixin):
    app: Flask | None
    service_url: str
    jsonrpc_site: type[JSONRPCSite]
    jsonrpc_site_api: type[JSONRPCView]
    browse_url: str
    enable_web_browsable_api: bool
    def __init__(
        self,
        app: Flask | None = ...,
        service_url: str = ...,
        jsonrpc_site: type[JSONRPCSite] = ...,
        jsonrpc_site_api: type[JSONRPCView] = ...,
        enable_web_browsable_api: bool = ...,
    ) -> None: ...
    def get_jsonrpc_site(self) -> JSONRPCSite: ...
    def get_jsonrpc_site_api(self) -> type[JSONRPCView]: ...
    def init_app(self, app: Flask) -> None: ...
    def register(self, view_func: Callable[..., Any], name: str | None = ..., validate: bool = ..., **options: Any) -> None: ...
    def register_blueprint(
        self, app: Flask, jsonrpc_app: JSONRPCBlueprint, url_prefix: str, enable_web_browsable_api: bool = ...
    ) -> None: ...
    def register_browse(self, app: Flask, jsonrpc_app: JSONRPC | JSONRPCBlueprint, url_prefix: str | None = ...) -> None: ...
