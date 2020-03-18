from hammurabi.rules.common import MultiplePathRule as MultiplePathRule, SinglePathRule as SinglePathRule
from pathlib import Path
from typing import Iterable

class FileExists(SinglePathRule):
    def task(self) -> Path: ...

class FilesExist(MultiplePathRule):
    def task(self) -> Iterable[Path]: ...

class FileNotExists(SinglePathRule):
    def post_task_hook(self) -> None: ...
    def task(self) -> Path: ...

class FilesNotExist(MultiplePathRule):
    def post_task_hook(self) -> None: ...
    def task(self) -> Iterable[Path]: ...

class FileEmptied(SinglePathRule):
    def task(self) -> Path: ...
