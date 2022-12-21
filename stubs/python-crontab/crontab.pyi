import re
import subprocess
from _typeshed import Incomplete, Self
from collections import OrderedDict
from collections.abc import Callable, Generator
from logging import Logger
from types import TracebackType
from typing import Any, Iterator, SupportsIndex
from typing_extensions import Literal

from cronlog import CronLog

__pkgname__: str
ITEMREX: re.Pattern[str]
SPECREX: re.Pattern[str]
DEVNULL: str
WEEK_ENUM: list[str]
MONTH_ENUM: list[str | None]
SPECIALS: dict[str, str]
SPECIAL_IGNORE: list[str]
S_INFO: list[dict[str, Any]]
PY3: Literal[True]
WINOS: bool
POSIX: bool
SYSTEMV: bool
ZERO_PAD: bool
LOG: Logger
CRON_COMMAND: str
SHELL: str
current_user: Callable[[], str | None]

def open_pipe(cmd: str, *args: str, **flags) -> subprocess.Popen[Any]: ...

class CronTab:
    lines: Incomplete
    crons: list[CronItem]
    filen: str | None
    cron_command: Incomplete
    env: OrderedVariableList
    root: bool
    intab: str | None
    def __init__(
        self, user: bool | str | None = ..., tab: str | None = ..., tabfile: str | None = ..., log: str | None = ...
    ) -> None: ...
    def __enter__(self: Self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...
    @property
    def log(self) -> CronLog: ...
    @property
    def user(self) -> str | None: ...
    @property
    def user_opt(self) -> dict[str, str]: ...
    def read(self, filename: str | None = ...) -> None: ...
    def append(
        self,
        item: CronItem,
        line: str = ...,
        read: bool = ...,
        before: str | re.Pattern[str] | list[CronItem] | tuple[CronItem, ...] | Generator[CronItem, Any, Any] | None = ...,
    ) -> None: ...
    def write(self, filename: str | None = ..., user: bool | None = ..., errors: bool = ...) -> None: ...
    def write_to_user(self, user: bool = ...) -> None: ...
    def run_pending(self, **kwargs) -> Generator[Incomplete, None, None]: ...
    def run_scheduler(self, timeout: int = ..., **kwargs) -> Generator[Incomplete, None, None]: ...
    def render(self, errors: bool = ..., specials: bool = ...) -> str: ...
    def new(
        self,
        command: str = ...,
        comment: str = ...,
        user: Incomplete | None = ...,
        pre_comment: bool = ...,
        before: str | re.Pattern[str] | list[CronItem] | tuple[CronItem, ...] | Generator[CronItem, Any, Any] | None = ...,
    ) -> CronItem: ...
    def find_command(self, command: str | re.Pattern[str]) -> Generator[Incomplete, None, None]: ...
    def find_comment(self, comment: str | re.Pattern[str]) -> Generator[Incomplete, None, None]: ...
    def find_time(self, *args) -> Generator[Incomplete, None, None]: ...
    @property
    def commands(self) -> Generator[Incomplete, None, None]: ...
    @property
    def comments(self) -> Generator[Incomplete, None, None]: ...
    def remove_all(self, *, command: str | re.Pattern[str] = ..., comment: str | re.Pattern[str] = ..., time=...) -> int: ...
    def remove(self, *items: CronItem | list[CronItem] | tuple[CronItem, ...] | Generator[CronItem, Any, Any]) -> int: ...
    def __iter__(self) -> Iterator[CronItem]: ...
    def __getitem__(self, i: SupportsIndex) -> CronItem: ...
    def __unicode__(self) -> str: ...
    def __len__(self) -> int: ...

class CronItem:
    cron: Incomplete
    user: Incomplete
    valid: bool
    enabled: bool
    special: bool
    comment: Incomplete
    command: Incomplete
    last_run: Incomplete
    env: Incomplete
    pre_comment: bool
    marker: Incomplete
    stdin: Incomplete
    slices: Incomplete
    def __init__(
        self, command: str = ..., comment: str = ..., user: Incomplete | None = ..., pre_comment: bool = ...
    ) -> None: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: object) -> bool: ...
    @classmethod
    def from_line(cls: type[Self], line: str, user: Incomplete | None = ..., cron: Incomplete | None = ...) -> Self: ...
    def delete(self) -> None: ...
    def set_command(self, cmd: str, parse_stdin: bool = ...) -> None: ...
    def set_comment(self, cmt: str, pre_comment: bool = ...) -> None: ...
    def parse(self, line) -> None: ...
    def enable(self, enabled: bool = ...) -> bool: ...
    def is_enabled(self) -> bool: ...
    def is_valid(self) -> bool: ...
    def render(self, specials: bool = ...) -> str: ...
    def every_reboot(self): ...
    def every(self, unit: int = ...): ...
    def setall(self, *args: Any): ...
    def clear(self): ...
    def frequency(self, year: int | None = ...) -> int: ...
    def frequency_per_year(self, year: int | None = ...) -> int: ...
    def frequency_per_day(self) -> int: ...
    def frequency_per_hour(self) -> int: ...
    def run_pending(self, now: Incomplete | None = ...): ...
    def run(self): ...
    def schedule(self, date_from: Incomplete | None = ...): ...
    def description(self, **kw: Any): ...
    @property
    def log(self): ...
    @property
    def minute(self) -> CronSlice: ...
    @property
    def minutes(self) -> CronSlice: ...
    @property
    def hour(self) -> CronSlice: ...
    @property
    def hours(self) -> CronSlice: ...
    @property
    def day(self) -> CronSlice: ...
    @property
    def dom(self) -> CronSlice: ...
    @property
    def month(self) -> CronSlice: ...
    @property
    def months(self) -> CronSlice: ...
    @property
    def dow(self) -> CronSlice: ...
    def __len__(self) -> int: ...
    def __getitem__(self, key: str) -> CronSlice: ...
    def __lt__(self, value) -> bool: ...
    def __gt__(self, value) -> bool: ...
    def __unicode__(self) -> str: ...

class Every:
    slices: Incomplete
    unit: Incomplete
    def __init__(self, item, units) -> None: ...
    def set_attr(self, target: int) -> Callable[[], None]: ...
    def year(self) -> None: ...

class CronSlices(list[CronSlice]):
    special: Incomplete
    def __init__(self, *args: Any) -> None: ...
    def is_self_valid(self, *args: Any) -> bool: ...
    @classmethod
    def is_valid(cls, *args: Any) -> bool: ...
    def setall(self, *slices) -> None: ...
    def clean_render(self) -> str: ...
    def render(self, specials: bool = ...) -> str: ...
    def clear(self) -> None: ...
    def frequency(self, year: int | None = ...) -> int: ...
    def frequency_per_year(self, year: int | None = ...) -> int: ...
    def frequency_per_day(self) -> int: ...
    def frequency_per_hour(self) -> int: ...
    def __eq__(self, arg: object) -> bool: ...

class SundayError(KeyError): ...

class Also:
    obj: Incomplete
    def __init__(self, obj) -> None: ...
    def every(self, *a): ...
    def on(self, *a): ...
    def during(self, *a): ...

class CronSlice:
    min: Incomplete
    max: Incomplete
    name: Incomplete
    enum: Incomplete
    parts: Incomplete
    def __init__(self, info, value: Incomplete | None = ...) -> None: ...
    def __hash__(self) -> int: ...
    def parse(self, value) -> None: ...
    def render(self, resolve: bool = ..., specials: bool = ...): ...
    def __eq__(self, arg: object) -> bool: ...
    def __unicode__(self) -> str: ...
    def every(self, n_value, also: bool = ...): ...
    def on(self, *n_value, **opts): ...
    def during(self, vfrom, vto, also: bool = ...): ...
    @property
    def also(self): ...
    def clear(self) -> None: ...
    def get_range(self, *vrange): ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def parse_value(self, val, sunday: Incomplete | None = ...): ...

def get_cronvalue(value, enums): ...

class CronValue:
    text: Incomplete
    value: Incomplete
    def __init__(self, value, enums) -> None: ...
    def __lt__(self, value): ...
    def __int__(self) -> int: ...

class CronRange:
    dangling: Incomplete
    slice: Incomplete
    cron: Incomplete
    seq: int
    def __init__(self, vslice, *vrange) -> None: ...
    vfrom: Incomplete
    vto: Incomplete
    def parse(self, value) -> None: ...
    def all(self) -> None: ...
    def render(self, resolve: bool = ...): ...
    def range(self): ...
    def every(self, value) -> None: ...
    def __lt__(self, value): ...
    def __gt__(self, value): ...
    def __int__(self) -> int: ...
    def __unicode__(self) -> str: ...

class OrderedVariableList(OrderedDict[Incomplete, Incomplete]):
    job: Incomplete
    def __init__(self, *args: Any, **kw: Any) -> None: ...
    @property
    def previous(self): ...
    def all(self): ...
    def __getitem__(self, key): ...
