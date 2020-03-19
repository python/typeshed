import abc
from abc import ABC, abstractmethod
from hammurabi.config import config as config
from hammurabi.helpers import full_strip as full_strip
from typing import Any, Iterable, List, Optional

class Rule(ABC, metaclass=abc.ABCMeta):
    param: Any = ...
    name: Any = ...
    pipe: Any = ...
    children: Any = ...
    preconditions: Any = ...
    made_changes: bool = ...
    def __init__(
        self,
        name: str,
        param: Any,
        preconditions: Iterable[Rule] = ...,
        pipe: Optional[Rule] = ...,
        children: Iterable[Rule] = ...,
    ) -> None: ...
    @staticmethod
    def validate(
        val: Any, cast_to: Optional[Any] = ..., required: Any = ...
    ) -> Any: ...
    @property
    def description(self) -> str: ...
    @property
    def documentation(self) -> str: ...
    @property
    def can_proceed(self) -> bool: ...
    def get_rule_chain(self, rule: Rule) -> List[Rule]: ...
    def get_execution_order(self) -> List[Rule]: ...
    def pre_task_hook(self) -> None: ...
    def post_task_hook(self) -> None: ...
    @abstractmethod
    def task(self) -> Any: ...
    def execute(self, param: Optional[Any] = ...) -> Any: ...
