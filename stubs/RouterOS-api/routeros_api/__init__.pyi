from _typeshed import Incomplete

from routeros_api import api_structure as api_structure, query as query
from routeros_api.api import RouterOsApiPool as RouterOsApiPool, connect as connect

__all__ = ["connect", "RouterOsApiPool", "query", "api_structure"]

def __getattr__(name: str) -> Incomplete: ...
