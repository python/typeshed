from abc import ABC, abstractmethod

class ReversibleProxy: ...

class StartableContext(ABC):
    @abstractmethod
    async def start(self, is_ctxmanager: bool = ...): ...
    def __await__(self): ...
    async def __aenter__(self): ...
    @abstractmethod
    async def __aexit__(self, type_, value, traceback): ...

class ProxyComparable(ReversibleProxy):
    def __hash__(self) -> int: ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
