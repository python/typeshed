from datetime import datetime
from typing import Any, Final

__all__ = (
    "EVENT_ALL",
    "EVENT_ALL_JOBS_REMOVED",
    "EVENT_EXECUTOR_ADDED",
    "EVENT_EXECUTOR_REMOVED",
    "EVENT_JOBSTORE_ADDED",
    "EVENT_JOBSTORE_REMOVED",
    "EVENT_JOB_ADDED",
    "EVENT_JOB_ERROR",
    "EVENT_JOB_EXECUTED",
    "EVENT_JOB_MAX_INSTANCES",
    "EVENT_JOB_MISSED",
    "EVENT_JOB_MODIFIED",
    "EVENT_JOB_REMOVED",
    "EVENT_JOB_SUBMITTED",
    "EVENT_SCHEDULER_PAUSED",
    "EVENT_SCHEDULER_RESUMED",
    "EVENT_SCHEDULER_SHUTDOWN",
    "EVENT_SCHEDULER_STARTED",
    "JobEvent",
    "JobExecutionEvent",
    "JobSubmissionEvent",
    "SchedulerEvent",
)

EVENT_SCHEDULER_STARTED: Final = 1
EVENT_SCHEDULER_START: Final = 1  # undocumented
EVENT_SCHEDULER_SHUTDOWN: Final = 2
EVENT_SCHEDULER_PAUSED: Final = 4
EVENT_SCHEDULER_RESUMED: Final = 8
EVENT_EXECUTOR_ADDED: Final = 16
EVENT_EXECUTOR_REMOVED: Final = 32
EVENT_JOBSTORE_ADDED: Final = 64
EVENT_JOBSTORE_REMOVED: Final = 128
EVENT_ALL_JOBS_REMOVED: Final = 256
EVENT_JOB_ADDED: Final = 512
EVENT_JOB_REMOVED: Final = 1024
EVENT_JOB_MODIFIED: Final = 2048
EVENT_JOB_EXECUTED: Final = 4096
EVENT_JOB_ERROR: Final = 8192
EVENT_JOB_MISSED: Final = 16384
EVENT_JOB_SUBMITTED: Final = 32768
EVENT_JOB_MAX_INSTANCES: Final = 65536
EVENT_ALL: Final = 131071

class SchedulerEvent:
    code: int
    # The alias of the executor or job store added or removed, None for other events.
    alias: str | None
    def __init__(self, code: int, alias: str | None = None) -> None: ...

class JobEvent(SchedulerEvent):
    job_id: str
    jobstore: str | None
    def __init__(self, code: int, job_id: str, jobstore: str | None) -> None: ...

class JobSubmissionEvent(JobEvent):
    scheduled_run_times: list[datetime]
    def __init__(self, code: int, job_id: str, jobstore: str | None, scheduled_run_times: list[datetime]) -> None: ...

class JobExecutionEvent(JobEvent):
    scheduled_run_time: datetime
    # None unless the event is EVENT_JOB_EXECUTED.
    retval: Any  # the job function's return value, of a type only the job function knows
    # Set for EVENT_JOB_ERROR: the exception the job raised and its formatted traceback.
    exception: BaseException | None
    traceback: str | None
    def __init__(
        self,
        code: int,
        job_id: str,
        jobstore: str | None,
        scheduled_run_time: datetime,
        retval: object = None,
        exception: BaseException | None = None,
        traceback: str | None = None,
    ) -> None: ...
