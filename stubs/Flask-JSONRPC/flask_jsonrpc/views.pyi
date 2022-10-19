from typing import Any
from typing_extensions import TypeAlias

from .site import JSONRPCSite

MethodView: TypeAlias = Any
ResponseReturnValue: TypeAlias = Any

class JSONRPCView(MethodView):
    jsonrpc_site: JSONRPCSite
    def __init__(self, jsonrpc_site: JSONRPCSite) -> None: ...
    def post(self) -> ResponseReturnValue: ...
