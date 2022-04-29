from _typeshed import Incomplete
from collections.abc import Callable
from functools import partial as partial
from typing import Generic, TypeVar
from typing_extensions import ParamSpec

from huey.constants import EmptyData as EmptyData
from huey.consumer import Consumer as Consumer
from huey.exceptions import (
    CancelExecution as CancelExecution,
    ConfigurationError as ConfigurationError,
    HueyException as HueyException,
    RetryTask as RetryTask,
    TaskException as TaskException,
    TaskLockedException as TaskLockedException,
)
from huey.registry import Registry as Registry
from huey.serializer import Serializer as Serializer
from huey.storage import (
    BlackHoleStorage as BlackHoleStorage,
    FileStorage as FileStorage,
    MemoryStorage as MemoryStorage,
    PriorityRedisExpireStorage as PriorityRedisExpireStorage,
    PriorityRedisStorage as PriorityRedisStorage,
    RedisExpireStorage as RedisExpireStorage,
    RedisStorage as RedisStorage,
    SqliteStorage as SqliteStorage,
)
from huey.utils import (
    Error as Error,
    normalize_expire_time as normalize_expire_time,
    normalize_time as normalize_time,
    reraise_as as reraise_as,
    string_type as string_type,
    time_clock as time_clock,
    to_timestamp as to_timestamp,
)

logger: Incomplete

_T = TypeVar("_T")
_P = ParamSpec("_P")

# When changing methods of this class, also change corresponding functions in
# stubs/django-huey/django_huey/__init__.pyi and
# stubs/huey/huey/contrib/djhuey/__init__.pyi
class Huey:
    storage_class: Incomplete
    name: Incomplete
    results: Incomplete
    store_none: Incomplete
    utc: Incomplete
    immediate_use_memory: Incomplete
    serializer: Incomplete
    storage_kwargs: Incomplete
    storage: Incomplete
    def __init__(
        self,
        name: str = ...,
        results: bool = ...,
        store_none: bool = ...,
        utc: bool = ...,
        immediate: bool = ...,
        serializer: Incomplete | None = ...,
        compression: bool = ...,
        use_zlib: bool = ...,
        immediate_use_memory: bool = ...,
        always_eager: Incomplete | None = ...,
        storage_class: Incomplete | None = ...,
        **storage_kwargs,
    ) -> None: ...
    def create_storage(self): ...
    def get_immediate_storage(self): ...
    def get_storage(self, **kwargs): ...
    @property
    def immediate(self): ...
    @immediate.setter
    def immediate(self, value) -> None: ...
    def create_consumer(self, **options): ...
    def task(
        self,
        retries: int = ...,
        retry_delay: int = ...,
        priority: Incomplete | None = ...,
        context: bool = ...,
        name: Incomplete | None = ...,
        expires: Incomplete | None = ...,
        **kwargs,
    ) -> Callable[[Callable[_P, _T]], TaskWrapper[_T, _P]]: ...
    def periodic_task(
        self,
        validate_datetime,
        retries: int = ...,
        retry_delay: int = ...,
        priority: Incomplete | None = ...,
        context: bool = ...,
        name: Incomplete | None = ...,
        expires: Incomplete | None = ...,
        **kwargs,
    ) -> Callable[[Callable[_P, _T]], TaskWrapper[_T, _P]]: ...
    def context_task(self, obj, as_argument: bool = ..., **kwargs): ...
    def pre_execute(self, name: Incomplete | None = ...): ...
    def unregister_pre_execute(self, name): ...
    def post_execute(self, name: Incomplete | None = ...): ...
    def unregister_post_execute(self, name): ...
    def on_startup(self, name: Incomplete | None = ...): ...
    def unregister_on_startup(self, name): ...
    def on_shutdown(self, name: Incomplete | None = ...): ...
    def unregister_on_shutdown(self, name: Incomplete | None = ...): ...
    def notify_interrupted_tasks(self) -> None: ...
    def signal(self, *signals): ...
    def disconnect_signal(self, receiver, *signals) -> None: ...
    def serialize_task(self, task): ...
    def deserialize_task(self, data): ...
    def enqueue(self, task: Task[_T]) -> Result[_T]: ...
    def dequeue(self): ...
    def put(self, key, data): ...
    def put_result(self, key, data): ...
    def put_if_empty(self, key, data): ...
    def get_raw(self, key, peek: bool = ...): ...
    def get(self, key, peek: bool = ...): ...
    def delete(self, key): ...
    def execute(self, task, timestamp: Incomplete | None = ...): ...
    def build_error_result(self, task, exception): ...
    def revoke_all(self, task_class, revoke_until: Incomplete | None = ..., revoke_once: bool = ...) -> None: ...
    def restore_all(self, task_class): ...
    def revoke(self, task, revoke_until: Incomplete | None = ..., revoke_once: bool = ...) -> None: ...
    def restore(self, task): ...
    def revoke_by_id(self, id, revoke_until: Incomplete | None = ..., revoke_once: bool = ...): ...
    def restore_by_id(self, id): ...
    def is_revoked(self, task, timestamp: Incomplete | None = ..., peek: bool = ...): ...
    def add_schedule(self, task) -> None: ...
    def read_schedule(self, timestamp: Incomplete | None = ...): ...
    def read_periodic(self, timestamp): ...
    def ready_to_run(self, task, timestamp: Incomplete | None = ...): ...
    def pending(self, limit: Incomplete | None = ...): ...
    def pending_count(self): ...
    def scheduled(self, limit: Incomplete | None = ...): ...
    def scheduled_count(self): ...
    def all_results(self): ...
    def result_count(self): ...
    def __len__(self): ...
    def flush(self) -> None: ...
    def lock_task(self, lock_name): ...
    def flush_locks(self, *names): ...
    def result(
        self,
        id,
        blocking: bool = ...,
        timeout: Incomplete | None = ...,
        backoff: float = ...,
        max_delay: float = ...,
        revoke_on_timeout: bool = ...,
        preserve: bool = ...,
    ): ...

class Task(Generic[_T]):
    default_expires: Incomplete
    default_priority: Incomplete
    default_retries: int
    default_retry_delay: int
    name: Incomplete
    args: Incomplete
    kwargs: Incomplete
    id: Incomplete
    revoke_id: Incomplete
    eta: Incomplete
    retries: Incomplete
    retry_delay: Incomplete
    priority: Incomplete
    expires: Incomplete
    expires_resolved: Incomplete
    on_complete: Incomplete
    on_error: Incomplete
    def __init__(
        self,
        args: Incomplete | None = ...,
        kwargs: Incomplete | None = ...,
        id: Incomplete | None = ...,
        eta: Incomplete | None = ...,
        retries: Incomplete | None = ...,
        retry_delay: Incomplete | None = ...,
        priority: Incomplete | None = ...,
        expires: Incomplete | None = ...,
        on_complete: Incomplete | None = ...,
        on_error: Incomplete | None = ...,
        expires_resolved: Incomplete | None = ...,
    ) -> None: ...
    @property
    def data(self): ...
    def __hash__(self): ...
    def create_id(self): ...
    def resolve_expires(self, utc: bool = ...): ...
    def extend_data(self, data) -> None: ...
    def then(self, task, *args, **kwargs): ...
    def error(self, task, *args, **kwargs): ...
    def execute(self) -> None: ...
    def __eq__(self, rhs): ...

class PeriodicTask(Task[_T]):
    def validate_datetime(self, timestamp): ...

class TaskWrapper(Generic[_T, _P]):
    task_base: Incomplete
    __doc__: Incomplete
    huey: Incomplete
    func: Incomplete
    retries: Incomplete
    retry_delay: Incomplete
    context: Incomplete
    name: Incomplete
    settings: Incomplete
    task_class: Incomplete
    def __init__(
        self,
        huey,
        func,
        retries: Incomplete | None = ...,
        retry_delay: Incomplete | None = ...,
        context: bool = ...,
        name: Incomplete | None = ...,
        task_base: Incomplete | None = ...,
        **settings,
    ) -> None: ...
    def unregister(self): ...
    def create_task(self, func, context: bool = ..., name: Incomplete | None = ..., **settings): ...
    def is_revoked(self, timestamp: Incomplete | None = ..., peek: bool = ...): ...
    def revoke(self, revoke_until: Incomplete | None = ..., revoke_once: bool = ...) -> None: ...
    def restore(self): ...
    def schedule(
        self,
        args: Incomplete | None = ...,
        kwargs: Incomplete | None = ...,
        eta: Incomplete | None = ...,
        delay: Incomplete | None = ...,
        priority: Incomplete | None = ...,
        retries: Incomplete | None = ...,
        retry_delay: Incomplete | None = ...,
        expires: Incomplete | None = ...,
        id: Incomplete | None = ...,
    ): ...
    def map(self, it): ...
    def __call__(self, *args: _P.args, **kwargs: _P.kwargs) -> Result[_T]: ...
    def call_local(self, *args: _P.args, **kwargs: _P.kwargs) -> _T: ...
    def s(self, *args: _P.args, **kwargs: _P.kwargs) -> Task[_T]: ...

class TaskLock:
    def __init__(self, huey, name) -> None: ...
    def __call__(self, fn): ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...
    def clear(self): ...

class Result(Generic[_T]):
    huey: Incomplete
    task: Incomplete
    def __init__(self, huey, task) -> None: ...
    @property
    def id(self): ...
    def __call__(
        self,
        blocking: bool = ...,
        timeout: Incomplete | None = ...,
        backoff: float = ...,
        max_delay: float = ...,
        revoke_on_timeout: bool = ...,
        preserve: bool = ...,
    ) -> _T: ...
    def get_raw_result(
        self,
        blocking: bool = ...,
        timeout: Incomplete | None = ...,
        backoff: float = ...,
        max_delay: float = ...,
        revoke_on_timeout: bool = ...,
        preserve: bool = ...,
    ): ...
    def get(
        self,
        blocking: bool = ...,
        timeout: Incomplete | None = ...,
        backoff: float = ...,
        max_delay: float = ...,
        revoke_on_timeout: bool = ...,
        preserve: bool = ...,
    ) -> _T: ...
    def is_revoked(self): ...
    def revoke(self, revoke_once: bool = ...) -> None: ...
    def restore(self): ...
    def reschedule(self, eta: Incomplete | None = ..., delay: Incomplete | None = ..., expires: Incomplete | None = ...): ...
    def reset(self) -> None: ...

class ResultGroup:
    def __init__(self, results) -> None: ...
    def get(self, *args, **kwargs): ...
    __call__: Incomplete
    def __getitem__(self, idx): ...
    def __iter__(self): ...
    def __len__(self): ...

dash_re: Incomplete
every_re: Incomplete

def crontab(minute: str = ..., hour: str = ..., day: str = ..., month: str = ..., day_of_week: str = ..., strict: bool = ...): ...

class BlackHoleHuey(Huey):
    storage_class: Incomplete

class MemoryHuey(Huey):
    storage_class: Incomplete

class SqliteHuey(Huey):
    storage_class: Incomplete

class RedisHuey(Huey):
    storage_class: Incomplete

class RedisExpireHuey(Huey):
    storage_class: Incomplete

class PriorityRedisHuey(Huey):
    storage_class: Incomplete

class PriorityRedisExpireHuey(Huey):
    storage_class: Incomplete

class FileHuey(Huey):
    storage_class: Incomplete
