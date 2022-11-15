from typing import Any, Union, Callable
from tkinter import Event, Text
from idlelib.delegator import Delegator as Delegator

class UndoDelegator(Delegator):
    max_undo: int
    def __init__(self) -> None: ...
    def setdelegate(self, delegate: object | None) -> None: ...
    def dump_event(self, event: Union['Event[Any]', None]) -> str: ...
    was_saved: int
    pointer: int
    undolist: list['Command']
    undoblock: int
    def reset_undo(self) -> None: ...
    saved: int
    can_merge: bool
    def set_saved(self, flag: int) -> None: ...
    def get_saved(self) -> bool: ...
    saved_change_hook: Callable[[], Any]
    def set_saved_change_hook(self, hook: Callable[[], Any]) -> None: ...
    def check_saved(self) -> None: ...
    def insert(self, index: str, chars: str, tags: str | None = ...) -> None: ...
    def delete(self, index1: str, index2: str | None = ...) -> None: ...
    def undo_block_start(self) -> None: ...
    def undo_block_stop(self) -> None: ...
    def addcmd(self, cmd: 'Command', execute: bool = ...) -> None: ...
    def undo_event(self, event: Union['Event[Any]', None]) -> str: ...
    def redo_event(self, event: Union['Event[Any]', None]) -> str: ...

class Command:
    tags: str | None
    marks_before: dict[str, str]
    marks_after: dict[str, str]
    index1: str | None
    index2: str | None
    chars: str
    def __init__(self, index1: str | None, index2: str | None, chars: str, tags: str | None = ...) -> None: ...
    def do(self, text: Text) -> None: ...
    def redo(self, text: Text) -> None: ...
    def undo(self, text: Text) -> None: ...
    def merge(self, cmd: 'Command') -> bool: ...
    def save_marks(self, text: Text) -> dict[str, str]: ...
    def set_marks(self, text: Text, marks: dict[str, str]) -> None: ...

class InsertCommand(Command):
    def __init__(self, index1: str, chars: str, tags: str | None = ...) -> None: ...
    marks_before: dict[str, str]
    index1: str
    index2: str | None
    marks_after: dict[str, str]
    def do(self, text: Text) -> None: ...
    def redo(self, text: Text) -> None: ...
    def undo(self, text: Text) -> None: ...
    chars: str
    def merge(self, cmd: Command) -> bool: ...
    alphanumeric: str
    def classify(self, c: str) -> str: ...

class DeleteCommand(Command):
    def __init__(self, index1: str | None, index2: str | None = ...) -> None: ...
    marks_before: dict[str, str]
    index1: str | None
    index2: str | None
    chars: str
    marks_after: dict[str, str]
    def do(self, text: Text) -> None: ...
    def redo(self, text: Text) -> None: ...
    def undo(self, text: Text) -> None: ...

class CommandSequence(Command):
    cmds: list[Command]
    depth: int
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def append(self, cmd: Command) -> None: ...
    def getcmd(self, i: int) -> Command: ...
    def redo(self, text: Text) -> None: ...
    def undo(self, text: Text) -> None: ...
    def bump_depth(self, incr: int = ...) -> int: ...
