from typing import Any

class FileList:
    allfiles: Any
    files: Any
    def __init__(self, warn: Any | None = ..., debug_print: Any | None = ...) -> None: ...
    def set_allfiles(self, allfiles) -> None: ...
    def findall(self, dir=...) -> None: ...
    def debug_print(self, msg) -> None: ...
    def append(self, item) -> None: ...
    def extend(self, items) -> None: ...
    def sort(self) -> None: ...
    def remove_duplicates(self) -> None: ...
    def process_template_line(self, line) -> None: ...
    def include_pattern(self, pattern, anchor: int = ..., prefix: Any | None = ..., is_regex: int = ...): ...
    def exclude_pattern(self, pattern, anchor: int = ..., prefix: Any | None = ..., is_regex: int = ...): ...

class _UniqueDirs(set):
    def __call__(self, walk_item): ...
    @classmethod
    def filter(cls, items): ...

def findall(dir=...): ...
def glob_to_re(pattern): ...
def translate_pattern(pattern, anchor: int = ..., prefix: Any | None = ..., is_regex: int = ...): ...
