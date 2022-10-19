from .site import JSONRPCSite
from .views import JSONRPCView

default_jsonrpc_site: type[JSONRPCSite]
default_jsonrpc_site_api: type[JSONRPCView]
