import abc
from abc import abstractmethod
from hammurabi.rules.common import SinglePathRule as SinglePathRule
from pathlib import Path
from typing import Any, Optional

class SingleAttributeRule(SinglePathRule, metaclass=abc.ABCMeta):
    new_value: Any = ...
    def __init__(
        self,
        name: str,
        path: Optional[Path] = ...,
        new_value: Optional[str] = ...,
        **kwargs: Any
    ) -> None: ...
    def post_task_hook(self) -> None: ...
    @abstractmethod
    def task(self) -> Any: ...

class OwnerChanged(SingleAttributeRule):
    def task(self) -> Path: ...

class ModeChanged(SingleAttributeRule):
    new_value: Any = ...
    def __init__(
        self,
        name: str,
        path: Optional[Path] = ...,
        new_value: Optional[int] = ...,
        **kwargs: Any
    ) -> None: ...
    def task(self) -> Path: ...
