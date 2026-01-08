from collections.abc import Generator
from contextlib import contextmanager

__all__ = ["BusyCursor"]

@contextmanager
def BusyCursor() -> Generator[None]: ...
