from .json import JSON
from .search import Search
from .timeseries import TimeSeries

class RedisModuleCommands:
    def json(self, encoder=..., decoder=...) -> JSON: ...
    def ft(self, index_name: str = 'idx') -> Search: ...
    def ts(self) -> TimeSeries: ...
    def bf(self): ...
    def cf(self): ...
    def cms(self): ...
    def topk(self): ...
    def tdigest(self): ...
    def graph(self, index_name: str = 'idx'): ...
