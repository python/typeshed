from _typeshed import SupportsItems
from collections.abc import Callable
from typing import Any

from pynput import _util

from ._base import Controller as Controller, Key as Key, KeyCode as KeyCode, Listener as Listener

class Events(_util.Events[Any, Listener]):
    class Press(_util.Events.Event):
        key: Key | KeyCode | None
        def __init__(self, key: Key | KeyCode | None) -> None: ...

    class Release(_util.Events.Event):
        key: Key | KeyCode | None
        def __init__(self, key: Key | KeyCode | None) -> None: ...

    def __init__(self) -> None: ...
    def __next__(self) -> Press | Release: ...
    def get(self, timeout: float | None = ...) -> Press | Release | None: ...

class HotKey:
    def __init__(self, keys: list[KeyCode], on_activate: Callable[[], None]) -> None: ...
    @staticmethod
    def parse(keys: str) -> list[KeyCode]: ...
    def press(self, key: Key | KeyCode) -> None: ...
    def release(self, key: Key | KeyCode) -> None: ...

class GlobalHotKeys(Listener):
    def __init__(self, hotkeys: SupportsItems[str, Callable[[], None]], *args: Any, **kwargs: Any) -> None: ...
