import re
import subprocess
from _typeshed import Incomplete, Self
from builtins import range as _range
from collections import OrderedDict
from collections.abc import Callable, Iterable, Iterator
from datetime import datetime
from logging import Logger
from types import TracebackType
from typing import Any
from typing_extensions import Literal, SupportsIndex, TypeAlias

from cronlog import CronLog

_User: TypeAlias = str | bool | None

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

def open_pipe(cmd: str, *args: str, **flags: str) -> subprocess.Popen[Any]: ...

class CronTab:
    lines: list[str | CronItem] | None
    crons: list[CronItem] | None
    filen: str | None
    cron_command: str
    env: OrderedVariableList | None
    root: bool
    intab: str | None
    tabfile: str | None
    def __init__(
        self, user: _User = ..., tab: str | None = ..., tabfile: str | None = ..., log: CronLog | str | None = ...
    ) -> None: ...
    def __enter__(self: Self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...
    @property
    def log(self) -> CronLog: ...
    @property
    def user(self) -> _User: ...
    @property
    def user_opt(self) -> dict[str, _User]: ...
    def read(self, filename: str | None = ...) -> None: ...
    def append(
        self,
        item: CronItem,
        line: str = ...,
        read: bool = ...,
        before: str | re.Pattern[str] | list[CronItem] | tuple[CronItem, ...] | Generator[CronItem, Any, Any] | None = ...,
    ) -> None: ...
    def write(self, filename: str | None = ..., user: _User = ..., errors: bool = ...) -> None: ...
    def write_to_user(self, user: bool | str = ...) -> None: ...
    # Usually `kwargs` are just `now: datetime | None`, but technically this can
    # work for `CronItem` subclasses, which might define other kwargs.
    def run_pending(self, **kwargs: Any) -> Iterator[str]: ...
    # There are two known kwargs and others are unused:
    def run_scheduler(self, timeout: int = ..., *, warp: object = ..., cadence: int = ..., **kwargs: object) -> Iterator[str]: ...
    def render(self, errors: bool = ..., specials: bool | None = ...) -> str: ...
    def new(
        self,
        command: str = ...,
        comment: str = ...,
        user: str | None = ...,
        pre_comment: bool = ...,
        before: str | re.Pattern[str] | list[CronItem] | tuple[CronItem, ...] | Generator[CronItem, Any, Any] | None = ...,
    ) -> CronItem: ...
    def find_command(self, command: str | re.Pattern[str]) -> Iterator[CronItem]: ...
    def find_comment(self, comment: str | re.Pattern[str]) -> Iterator[CronItem]: ...
    def find_time(self, *args: Any) -> Iterator[CronItem]: ...
    @property
    def commands(self) -> Iterator[str]: ...
    @property
    def comments(self) -> Iterator[str]: ...
    # You cannot actually pass `*args`, it will raise an exception,
    # also known kwargs are added:
    def remove_all(
        self, *, command: str | re.Pattern[str] = ..., comment: str | re.Pattern[str] = ..., time: Any = ..., **kwargs: object
    ) -> int: ...
    def remove(self, *items: CronItem | Iterable[CronItem]) -> int: ...
    def __iter__(self) -> Iterator[CronItem]: ...
    def __getitem__(self, i: int) -> CronItem: ...
    def __unicode__(self) -> str: ...
    def __len__(self) -> int: ...

class CronItem:
    cron: CronTab | None
    user: _User
    valid: bool
    enabled: bool
    special: bool
    comment: str
    command: str
    last_run: datetime | None
    env: OrderedVariableList
    pre_comment: bool
    marker: str | None
    stdin: str | None
    slices: CronSlices
    def __init__(self, command: str = ..., comment: str = ..., user: _User = ..., pre_comment: bool = ...) -> None: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: object) -> bool: ...
    @classmethod
    def from_line(cls: type[Self], line: str, user: str | None = ..., cron: Incomplete | None = ...) -> Self: ...
    def delete(self) -> None: ...
    def set_command(self, cmd: str, parse_stdin: bool = ...) -> None: ...
    def set_comment(self, cmt: str, pre_comment: bool = ...) -> None: ...
    def parse(self, line: str) -> None: ...
    def enable(self, enabled: bool = ...) -> bool: ...
    def is_enabled(self) -> bool: ...
    def is_valid(self) -> bool: ...
    def render(self, specials: bool = ...) -> str: ...
    def every_reboot(self) -> None: ...
    def every(self, unit: int = ...) -> Every: ...
    def setall(self, *args: Any) -> None: ...
    def clear(self) -> None: ...
    def frequency(self, year: int | None = ...) -> int: ...
    def frequency_per_year(self, year: int | None = ...) -> int: ...
    def frequency_per_day(self) -> int: ...
    def frequency_per_hour(self) -> int: ...
    def run_pending(self, now: datetime | None = ...) -> int | str: ...
    def run(self) -> str: ...
    # TODO: use types from `croniter` module here:
    def schedule(self, date_from: datetime | None = ...) -> Incomplete: ...
    # TODO: use types from `cron_descriptor` here:
    def description(self, **kw: Incomplete) -> Incomplete: ...
    @property
    def log(self) -> CronLog: ...
    @property
    def minute(self) -> int | str: ...
    @property
    def minutes(self) -> int | str: ...
    @property
    def hour(self) -> int | str: ...
    @property
    def hours(self) -> int | str: ...
    @property
    def day(self) -> int | str: ...
    @property
    def dom(self) -> int | str: ...
    @property
    def month(self) -> int | str: ...
    @property
    def months(self) -> int | str: ...
    @property
    def dow(self) -> int | str: ...
    def __len__(self) -> int: ...
    def __getitem__(self, key: str) -> int | str: ...
    def __lt__(self, value: object) -> bool: ...
    def __gt__(self, value: object) -> bool: ...
    def __unicode__(self) -> str: ...

class Every:
    slices: CronSlices
    unit: int
    # TODO: add generated attributes
    def __init__(self, item: CronSlices, units: int) -> None: ...
    def set_attr(self, target: int) -> Callable[[], None]: ...
    def year(self) -> None: ...

class CronSlices(list[CronSlice]):
    special: bool | None
    def __init__(self, *args: Any) -> None: ...
    def is_self_valid(self, *args: Any) -> bool: ...
    @classmethod
    def is_valid(cls, *args: Any) -> bool: ...
    def setall(self, *slices: str) -> None: ...
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
    obj: CronSlice
    def __init__(self, obj: CronSlice) -> None: ...
    # These method actually use `*args`, but pass them to `CronSlice` methods,
    # this is why they are typed as `Any`.
    def every(self, *a: Any) -> _Part: ...
    def on(self, *a: Any) -> list[_Part]: ...
    def during(self, *a: Any) -> _Part: ...

_Part: TypeAlias = int | CronValue | CronRange

class CronSlice:
    min: int | None
    max: int | None
    name: str | None
    enum: list[str | None] | None
    parts: list[_Part]
    def __init__(self, info: int | dict[str, Any], value: str | None = ...) -> None: ...
    def __hash__(self) -> int: ...
    def parse(self, value: str | None) -> None: ...
    def render(self, resolve: bool = ..., specials: bool = ...) -> str: ...
    def __eq__(self, arg: object) -> bool: ...
    def __unicode__(self) -> str: ...
    def every(self, n_value: int, also: bool = ...) -> _Part: ...
    # The only known kwarg, others are unused,
    # `*args`` are passed to `parse_value`, so they are `Any`
    def on(self, *n_value: Any, also: bool = ...) -> list[_Part]: ...
    def during(self, vfrom: int | str, vto: int | str, also: bool = ...) -> _Part: ...
    @property
    def also(self) -> Also: ...
    def clear(self) -> None: ...
    def get_range(self, *vrange: int | str | CronValue) -> list[int | CronRange]: ...
    def __iter__(self) -> Iterator[int]: ...
    def __len__(self) -> int: ...
    def parse_value(self, val: str, sunday: int | None = ...) -> int | CronValue: ...

def get_cronvalue(value: int, enums: list[str]) -> int | CronValue: ...

class CronValue:
    text: str
    value: int
    def __init__(self, value: str, enums: list[str]) -> None: ...
    def __lt__(self, value: object) -> bool: ...
    def __int__(self) -> int: ...

class CronRange:
    dangling: int | None
    slice: str
    cron: CronTab | None
    seq: int
    def __init__(self, vslice: str, *vrange: int | str | CronValue) -> None: ...
    # Are not set in `__init__`:
    vfrom: int | CronValue
    vto: int | CronValue
    def parse(self, value: str) -> None: ...
    def all(self) -> None: ...
    def render(self, resolve: bool = ...) -> str: ...
    def range(self) -> _range: ...
    def every(self, value: int | str) -> None: ...
    def __lt__(self, value: object) -> bool: ...
    def __gt__(self, value: object) -> bool: ...
    def __int__(self) -> int: ...
    def __unicode__(self) -> str: ...

# TODO: make generic
class OrderedVariableList(OrderedDict[Incomplete, Incomplete]):
    job: Incomplete
    def __init__(self, *args: Any, **kw: Any) -> None: ...
    @property
    def previous(self) -> Incomplete: ...
    def all(self: Self) -> Self: ...
    def __getitem__(self, key: Incomplete) -> Incomplete: ...
