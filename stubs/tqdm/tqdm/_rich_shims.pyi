from _typeshed import Incomplete
from abc import ABC, abstractmethod
from collections.abc import Iterable
from dataclasses import dataclass
from typing import Protocol, runtime_checkable
from typing_extensions import Literal, TypeAlias

# rich.align
VerticalAlignMethod: TypeAlias = Literal["top", "middle", "bottom"]

# rich.style
StyleType: TypeAlias = str | Incomplete

# rich.table

@dataclass
class Column(Protocol):
    header: RenderableType
    footer: RenderableType
    header_style: StyleType
    footer_style: StyleType
    style: StyleType
    justify: JustifyMethod
    vertical: VerticalAlignMethod
    overflow: OverflowMethod
    width: int | None
    min_width: int | None
    max_width: int | None
    ratio: int | None
    no_wrap: bool
    def copy(self) -> Column: ...
    @property
    def cells(self) -> Iterable[RenderableType]: ...
    @property
    def flexible(self) -> bool: ...

# rich.segment
Segment: TypeAlias = Incomplete

# region rich.console
JustifyMethod: TypeAlias = Literal["default", "left", "center", "right", "full"]
OverflowMethod: TypeAlias = Literal["fold", "crop", "ellipsis", "ignore"]
RenderResult: TypeAlias = Iterable[RenderableType | Segment]
Console: TypeAlias = Incomplete
ConsoleOptions: TypeAlias = Incomplete

@runtime_checkable
class RichCast(Protocol):
    def __rich__(self) -> ConsoleRenderable | RichCast | str: ...

@runtime_checkable
class ConsoleRenderable(Protocol):
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...

RenderableType: TypeAlias = ConsoleRenderable | RichCast | str

# endregion

# region rich.progress.Task
@dataclass
class Task(Protocol):
    id: int
    description: str
    total: float | None
    completed: float
    finished_time: float | None
    visible: bool
    fields: dict[str, Incomplete]
    start_time: float | None
    stop_time: float | None
    finished_speed: float | None
    def get_time(self) -> float: ...
    @property
    def started(self) -> bool: ...
    @property
    def remaining(self) -> float | None: ...
    @property
    def elapsed(self) -> float | None: ...
    @property
    def finished(self) -> bool: ...
    @property
    def percentage(self) -> float: ...
    @property
    def speed(self) -> float | None: ...
    @property
    def time_remaining(self) -> float | None: ...

class ProgressColumn(ABC):
    max_refresh: float | None
    def __init__(self, table_column: Column | None = ...) -> None: ...
    def get_table_column(self) -> Column: ...
    def __call__(self, task: Task) -> RenderableType: ...
    @abstractmethod
    def render(self, task: Task) -> RenderableType: ...

# endregion
