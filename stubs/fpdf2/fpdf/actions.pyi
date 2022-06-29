from _typeshed import Incomplete
from abc import ABC

from .syntax import PDFObject

class Action(ABC):
    def __init__(self, next_action: PDFObject | str | None = ...) -> None: ...
    def dict_as_string(self, key_values: dict[str, Incomplete] | None = ...) -> str: ...

class NamedAction(Action):
    action_name: Incomplete
    def __init__(self, action_name, next_action: PDFObject | str | None = ...) -> None: ...
    def dict_as_string(self) -> str: ...

class GoToAction(Action):
    dest: Incomplete
    def __init__(self, dest, next_action: PDFObject | str | None = ...) -> None: ...
    def dict_as_string(self) -> str: ...

class GoToRemoteAction(Action):
    file: Incomplete
    dest: Incomplete
    def __init__(self, file, dest, next_action: PDFObject | str | None = ...) -> None: ...
    def dict_as_string(self) -> str: ...

class LaunchAction(Action):
    file: Incomplete
    def __init__(self, file, next_action: PDFObject | str | None = ...) -> None: ...
    def dict_as_string(self) -> str: ...
