import selectors
import sys

from . import base_events

__all__ = ("BaseSelectorEventLoop",)

class BaseSelectorEventLoop(base_events.BaseEventLoop):
    def __init__(self, selector: selectors.BaseSelector | None = ...) -> None: ...
