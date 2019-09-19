# Stubs for maxminddb (Python 3)

from typing import Any

from maxminddb import reader

def open_database(database: str, mode: int = ...) -> reader.Reader: ...

def Reader(database: str) -> reader.Reader: ...
