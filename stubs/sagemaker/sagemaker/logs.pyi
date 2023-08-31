from _typeshed import Incomplete
from collections.abc import Generator
from typing import NamedTuple

class ColorWrap:
    colorize: Incomplete
    def __init__(self, force: bool = False) -> None: ...
    def __call__(self, index, s) -> None: ...

def argmin(arr, f): ...
def some(arr): ...

class Position(NamedTuple):
    timestamp: Incomplete
    skip: Incomplete

def multi_stream_iter(
    client, log_group, streams, positions: Incomplete | None = None
) -> Generator[Incomplete, None, Incomplete]: ...
def log_stream(client, log_group, stream_name, start_time: int = 0, skip: int = 0) -> Generator[Incomplete, None, None]: ...
