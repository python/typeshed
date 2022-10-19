from typing import Any
from typing_extensions import TypeAlias

from flask_jsonrpc.site import JSONRPCSite

Blueprint: TypeAlias = Any

def create_browse(name: str, jsonrpc_site: JSONRPCSite) -> Blueprint: ...
