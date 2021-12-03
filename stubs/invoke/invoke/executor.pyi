from typing import Any, Iterable
from .collection import Collection
from .config import Config
from .parser import ParseResult, ParserContext
from .tasks import Task, Call

_TaskType = str | tuple[str, dict[str, Any]] | ParserContext

class Executor:
    collection: Collection | None
    config: Config
    core: ParseResult | None
    def __init__(self, collection: Collection, config: Config | None = ..., core: ParseResult | None = ...) -> None: ...
    def execute(self, *tasks: _TaskType) -> dict[Task, Any]: ...
    def normalize(self, tasks: Iterable[_TaskType]): ...
    def dedupe(self, calls: list[Call]) -> list[Call]: ...
    def expand_calls(self, calls: list[Call | Task]) -> list[Call]: ...
