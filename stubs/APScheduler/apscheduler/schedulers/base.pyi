from _typeshed import StrOrBytesPath, SupportsRead, SupportsWrite
from abc import ABCMeta, abstractmethod
from collections.abc import Callable, Iterable, Mapping, MutableMapping
from datetime import date, datetime, tzinfo
from logging import Logger
from typing import Final, TypedDict, TypeVar, overload, type_check_only
from typing_extensions import Unpack, deprecated

from apscheduler.events import SchedulerEvent
from apscheduler.executors.base import BaseExecutor
from apscheduler.job import Job, _JobChanges
from apscheduler.jobstores.base import BaseJobStore
from apscheduler.triggers.base import BaseTrigger

_F = TypeVar("_F", bound=Callable[..., object])
_EventT = TypeVar("_EventT", bound=SchedulerEvent)

STATE_STOPPED: Final = 0
STATE_RUNNING: Final = 1
STATE_PAUSED: Final = 2

# Integers may be given as strings, and coalesce as a string such as "true" or "off".
@type_check_only
class _JobDefaults(TypedDict, total=False):
    misfire_grace_time: int | str | None
    coalesce: bool | str
    max_instances: int | str

# A string for logger is a textual reference ("module:attribute") to a Logger. An executor or job
# store is an instance, or a mapping naming its plugin under "type" or its class (or a textual
# reference to it) under "class", its other items passed to the constructor.
@type_check_only
class _SchedulerOptions(TypedDict, total=False):
    logger: Logger | str | None
    timezone: tzinfo | str | None
    jobstore_retry_interval: float | str
    job_defaults: _JobDefaults
    executors: Mapping[str, BaseExecutor | MutableMapping[str, object]]
    jobstores: Mapping[str, BaseJobStore | MutableMapping[str, object]]

class BaseScheduler(metaclass=ABCMeta):
    # One of STATE_STOPPED, STATE_RUNNING and STATE_PAUSED.
    state: int
    # Set by configure, and by the constructor through it.
    timezone: tzinfo
    jobstore_retry_interval: float
    # gconfig holds the options under keys starting with prefix, nested ones dotted
    # ("apscheduler.job_defaults.coalesce"); the keyword options override it.
    def __init__(self, gconfig: Mapping[str, object] = {}, **options: Unpack[_SchedulerOptions]) -> None: ...
    def configure(
        self, gconfig: Mapping[str, object] = {}, prefix: str | None = "apscheduler.", **options: Unpack[_SchedulerOptions]
    ) -> None: ...
    def start(self, paused: bool = False) -> None: ...
    @abstractmethod
    def shutdown(self, wait: bool = True) -> None: ...
    def pause(self) -> None: ...
    def resume(self) -> None: ...
    @property
    def running(self) -> bool: ...
    # executor_opts go to the constructor of the executor plugin that executor names (an entry point
    # of the apscheduler.executors group); an executor instance ignores them.
    def add_executor(self, executor: BaseExecutor | str, alias: str = "default", **executor_opts: object) -> None: ...
    def remove_executor(self, alias: str, shutdown: bool = True) -> None: ...
    # jobstore_opts go to the constructor of the job store plugin that jobstore names (an entry point
    # of the apscheduler.jobstores group); a job store instance ignores them.
    def add_jobstore(self, jobstore: BaseJobStore | str, alias: str = "default", **jobstore_opts: object) -> None: ...
    def remove_jobstore(self, alias: str, shutdown: bool = True) -> None: ...
    # mask is a bitwise or of the EVENT_* constants of apscheduler.events; the callback is called with the
    # events it selects, each of the SchedulerEvent subclass its code has (JobExecutionEvent for
    # EVENT_JOB_EXECUTED, EVENT_JOB_ERROR and EVENT_JOB_MISSED, for one).
    def add_listener(self, callback: Callable[[_EventT], object], mask: int = 131071) -> None: ...
    def remove_listener(self, callback: Callable[[_EventT], object]) -> None: ...
    # args and kwargs are passed to func when the job runs. trigger_args go to the constructor of the
    # trigger class that trigger names (an entry point of the apscheduler.triggers group, "date"
    # for None); a trigger instance ignores them.
    def add_job(
        self,
        func: Callable[..., object] | str,
        trigger: BaseTrigger | str | None = None,
        args: Iterable[object] | None = None,
        kwargs: Mapping[str, object] | None = None,
        id: str | None = None,
        name: str | None = None,
        misfire_grace_time: int | None = ...,
        coalesce: bool = ...,
        max_instances: int = ...,
        next_run_time: datetime | date | str | None = ...,
        jobstore: str = "default",
        executor: str = "default",
        replace_existing: bool = False,
        **trigger_args: object,
    ) -> Job: ...
    def scheduled_job(
        self,
        trigger: BaseTrigger | str | None,
        args: Iterable[object] | None = None,
        kwargs: Mapping[str, object] | None = None,
        id: str | None = None,
        name: str | None = None,
        misfire_grace_time: int | None = ...,
        coalesce: bool = ...,
        max_instances: int = ...,
        next_run_time: datetime | date | str | None = ...,
        jobstore: str = "default",
        executor: str = "default",
        **trigger_args: object,
    ) -> Callable[[_F], _F]: ...
    def modify_job(self, job_id: str, jobstore: str | None = None, **changes: Unpack[_JobChanges]) -> Job: ...
    def reschedule_job(
        self, job_id: str, jobstore: str | None = None, trigger: BaseTrigger | str | None = None, **trigger_args: object
    ) -> Job: ...
    def pause_job(self, job_id: str, jobstore: str | None = None) -> Job: ...
    # None when the job's trigger gives no next run time, the job then removed.
    def resume_job(self, job_id: str, jobstore: str | None = None) -> Job | None: ...

    @overload
    def get_jobs(self, jobstore: str | None = None, pending: None = None) -> list[Job]: ...
    @overload
    @deprecated(
        'The "pending" option is deprecated -- get_jobs() always returns scheduled jobs if the scheduler has been '
        "started and pending jobs otherwise"
    )
    def get_jobs(self, jobstore: str | None, pending: bool) -> list[Job]: ...
    @overload
    @deprecated(
        'The "pending" option is deprecated -- get_jobs() always returns scheduled jobs if the scheduler has been '
        "started and pending jobs otherwise"
    )
    def get_jobs(self, jobstore: str | None = None, *, pending: bool) -> list[Job]: ...

    def get_job(self, job_id: str, jobstore: str | None = None) -> Job | None: ...
    def remove_job(self, job_id: str, jobstore: str | None = None) -> None: ...
    def remove_all_jobs(self, jobstore: str | None = None) -> None: ...
    def print_jobs(self, jobstore: str | None = None, out: SupportsWrite[str] | None = None) -> None: ...
    def export_jobs(self, outfile: SupportsWrite[str] | StrOrBytesPath, jobstore: str | None = None) -> None: ...
    def import_jobs(self, infile: SupportsRead[str] | StrOrBytesPath, jobstore: str = "default") -> None: ...
    @abstractmethod
    def wakeup(self) -> None: ...
