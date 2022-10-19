from .site import JSONRPCSite
from .views import JSONRPCView
from .wrappers import JSONRPCDecoratorMixin

class JSONRPCBlueprint(JSONRPCDecoratorMixin):
    name: str
    import_name: str
    jsonrpc_site: type[JSONRPCSite]
    jsonrpc_site_api: type[JSONRPCView]
    def __init__(
        self, name: str, import_name: str, jsonrpc_site: type[JSONRPCSite] = ..., jsonrpc_site_api: type[JSONRPCView] = ...
    ) -> None: ...
    def get_jsonrpc_site(self) -> JSONRPCSite: ...
    def get_jsonrpc_site_api(self) -> type[JSONRPCView]: ...
