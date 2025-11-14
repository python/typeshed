import abc
from dataclasses import dataclass
from functools import cached_property
from typing import Final

@dataclass(frozen=True)
class JsRuntimeInfo:
    name: str
    path: str
    version: str
    version_tuple: tuple[int, ...]
    supported: bool = True

class JsRuntime(abc.ABC):
    def __init__(self, path: str | None = None) -> None: ...
    @cached_property
    @abc.abstractmethod
    def info(self) -> JsRuntimeInfo | None: ...

class DenoJsRuntime(JsRuntime):
    MIN_SUPPORTED_VERSION: Final = (2, 0, 0)
    @cached_property
    def info(self) -> JsRuntimeInfo | None: ...

class BunJsRuntime(JsRuntime):
    MIN_SUPPORTED_VERSION: Final = (1, 0, 31)
    @cached_property
    def info(self) -> JsRuntimeInfo | None: ...

class NodeJsRuntime(JsRuntime):
    MIN_SUPPORTED_VERSION: Final = (20, 0, 0)
    @cached_property
    def info(self) -> JsRuntimeInfo | None: ...

class QuickJsRuntime(JsRuntime):
    MIN_SUPPORTED_VERSION: Final = (2023, 12, 9)
    @cached_property
    def info(self) -> JsRuntimeInfo | None: ...
