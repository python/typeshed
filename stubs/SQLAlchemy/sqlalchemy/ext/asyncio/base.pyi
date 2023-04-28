from abc import ABC, ABCMeta, abstractmethod
from types import TracebackType

class ReversibleProxy: ...

class StartableContext(ABC, metaclass=ABCMeta):
    @abstractmethod
    async def start(self, is_ctxmanager: bool = False): ...
    def __await__(self): ...
    async def __aenter__(self): ...
    @abstractmethod
    async def __aexit__(
        self, type_: type[BaseException] | None, value: BaseException | None, traceback: TracebackType | None
    ) -> None: ...

class ProxyComparable(ReversibleProxy):
    def __hash__(self) -> int: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
