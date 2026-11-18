from collections.abc import Callable, Iterable, Mapping
from datetime import date, datetime
from typing import Any, TypedDict, type_check_only
from typing_extensions import Self, Unpack

from apscheduler.schedulers.base import BaseScheduler
from apscheduler.triggers.base import BaseTrigger

# The attributes a job's constructor and modify() accept.
@type_check_only
class _JobChanges(TypedDict, total=False):
    # A callable, or a textual reference ("module:attribute") to one.
    func: Callable[..., object] | str
    args: Iterable[Any]  # passed to func, whose signature is the caller's
    kwargs: Mapping[str, Any]  # passed to func, whose signature is the caller's
    name: str
    misfire_grace_time: int | None
    coalesce: bool
    max_instances: int
    trigger: BaseTrigger
    executor: str
    next_run_time: datetime | date | str | None

class Job:
    id: str
    name: str
    func: Callable[..., Any]
    # The textual reference to func, None where func has none (a lambda, a nested function).
    func_ref: str | None  # undocumented
    args: Iterable[Any]  # passed to func when the job runs
    kwargs: Mapping[str, Any]  # passed to func when the job runs
    trigger: BaseTrigger
    executor: str
    # The four below are set from add_job's or modify's arguments, or from the scheduler's job
    # defaults (next_run_time from the trigger) when the scheduler schedules the job: a job added
    # before start() without them has none of these attributes.
    misfire_grace_time: int | None
    coalesce: bool
    max_instances: int
    next_run_time: datetime | None
    def __init__(self, scheduler: BaseScheduler, id: str | None = None, **kwargs: Unpack[_JobChanges]) -> None: ...
    def modify(self, **changes: Unpack[_JobChanges]) -> Self: ...
    # trigger_args go to the constructor of the trigger class that trigger names (an entry point of
    # the apscheduler.triggers group, "date" for None); a trigger instance ignores them.
    def reschedule(self, trigger: BaseTrigger | str | None, **trigger_args: Any) -> Self: ...  # Any: the trigger's parameters
    def pause(self) -> Self: ...
    def resume(self) -> Self: ...
    def remove(self) -> None: ...
    @property
    def pending(self) -> bool: ...
