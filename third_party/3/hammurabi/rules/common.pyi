import abc
from abc import abstractmethod
from hammurabi.mixins import GitMixin as GitMixin
from hammurabi.rules.base import Rule as Rule
from pathlib import Path
from typing import Any, Iterable, Optional

class SinglePathRule(Rule, GitMixin, metaclass=abc.ABCMeta):
    def __init__(
        self, name: str, path: Optional[Path] = ..., **kwargs: Any
    ) -> None: ...
    def post_task_hook(self) -> None: ...
    @abstractmethod
    def task(self) -> Any: ...

class MultiplePathRule(Rule, GitMixin, metaclass=abc.ABCMeta):
    def __init__(
        self, name: str, paths: Optional[Iterable[Path]] = ..., **kwargs: Any
    ) -> None: ...
    def post_task_hook(self) -> None: ...
    @abstractmethod
    def task(self) -> Any: ...
