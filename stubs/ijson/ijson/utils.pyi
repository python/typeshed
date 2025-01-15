from _typeshed import Incomplete
from collections.abc import Generator

def coroutine(func): ...
def chain(sink, *coro_pipeline): ...

class sendable_list(list):
    send: Incomplete

def coros2gen(source, *coro_pipeline) -> Generator[Incomplete]: ...
