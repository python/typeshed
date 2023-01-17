from _typeshed import Incomplete
from typing import Any

class Options:
    @classmethod
    def options(cls, wrapped, _disambiguate_from_model_properties: bool = ...): ...
    @classmethod
    def slots(cls): ...
    def __init__(self, config: Incomplete | None = ..., **kwargs) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def copy(self, **kwargs): ...
    def items(self) -> None: ...

class ReadOptions(Options):
    def __init__(self, config: Incomplete | None = ..., **kwargs) -> None: ...