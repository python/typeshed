from _typeshed import Incomplete
from typing import Any

def load_endpoint_json(path): ...
def merge_endpoints(defaults, additions): ...
def load_regions(): ...
def get_regions(service_name, region_cls: Incomplete | None = ..., connection_cls: Incomplete | None = ...): ...

class RegionInfo:
    connection: Any
    name: Any
    endpoint: Any
    connection_cls: Any
    def __init__(
        self, connection: Incomplete | None = ..., name: Incomplete | None = ..., endpoint: Incomplete | None = ..., connection_cls: Incomplete | None = ...
    ) -> None: ...
    def startElement(self, name, attrs, connection): ...
    def endElement(self, name, value, connection): ...
    def connect(self, **kw_params): ...