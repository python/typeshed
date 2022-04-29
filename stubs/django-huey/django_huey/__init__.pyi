from _typeshed import Incomplete
from collections.abc import Callable
from typing import TypeVar
from typing_extensions import ParamSpec

from django_huey.config import DjangoHueySettingsReader as DjangoHueySettingsReader
from huey.api import Result, Task, TaskWrapper

DJANGO_HUEY: Incomplete
config: Incomplete

_T = TypeVar("_T")
_P = ParamSpec("_P")

def get_close_db_for_queue(queue: str | None = ...): ...
def get_queue(queue: str | None = ...): ...
def get_queue_name(queue): ...

# When changing these functions, also change the corresponding functions in
# stubs/django-huey/django_huey/__init__.pyi and
# stubs/huey/huey/contrib/djhuey/__init__.pyi
def task(
    retries: int = ...,
    retry_delay: int = ...,
    priority: Incomplete | None = ...,
    context: bool = ...,
    name: Incomplete | None = ...,
    expires: Incomplete | None = ...,
    *,
    queue: str | None = ...,
    **kwargs,
) -> Callable[[Callable[_P, _T]], TaskWrapper[_T, _P]]: ...
def periodic_task(
    validate_datetime,
    retries: int = ...,
    retry_delay: int = ...,
    priority: Incomplete | None = ...,
    context: bool = ...,
    name: Incomplete | None = ...,
    expires: Incomplete | None = ...,
    *,
    queue: str | None = ...,
    **kwargs,
) -> Callable[[Callable[_P, _T]], TaskWrapper[_T, _P]]: ...
def lock_task(lock_name, *, queue: str | None = ...): ...
def enqueue(task: Task[_T], *, queue: str | None = ...) -> Result[_T]: ...
def restore(task: Task, *, queue: str | None = ...): ...
def restore_all(task_class, *, queue: str | None = ...): ...
def restore_by_id(id, *, queue: str | None = ...): ...
def revoke(task, revoke_until: Incomplete | None = ..., revoke_once: bool = ..., *, queue: str | None = ...): ...
def revoke_all(task_class, revoke_until: Incomplete | None = ..., revoke_once: bool = ..., *, queue: str | None = ...): ...
def revoke_by_id(id, revoke_until: Incomplete | None = ..., revoke_once: bool = ..., *, queue: str | None = ...): ...
def is_revoked(task, timestamp: Incomplete | None = ..., peek: bool = ..., *, queue: str | None = ...): ...
def result(
    id,
    blocking: bool = ...,
    timeout: Incomplete | None = ...,
    backoff: float = ...,
    max_delay: float = ...,
    revoke_on_timeout: bool = ...,
    preserve: bool = ...,
    *,
    queue: str | None = ...,
): ...
def scheduled(limit: Incomplete | None = ..., *, queue: str | None = ...): ...
def on_startup(name: Incomplete | None = ..., *, queue: str | None = ...): ...
def on_shutdown(name: Incomplete | None = ..., *, queue: str | None = ...): ...
def pre_execute(name: Incomplete | None = ..., *, queue: str | None = ...): ...
def post_execute(name: Incomplete | None = ..., *, queue: str | None = ...): ...
def signal(*signals, queue: str | None = ...): ...
def disconnect_signal(receiver, *signals, queue: str | None = ...): ...
def db_task(
    retries: int = ...,
    retry_delay: int = ...,
    priority: Incomplete | None = ...,
    context: bool = ...,
    name: Incomplete | None = ...,
    expires: Incomplete | None = ...,
    *,
    queue: str | None = ...,
    **kwargs,
) -> Callable[[Callable[_P, _T]], TaskWrapper[_T, _P]]: ...
def db_periodic_task(
    validate_datetime,
    retries: int = ...,
    retry_delay: int = ...,
    priority: Incomplete | None = ...,
    context: bool = ...,
    name: Incomplete | None = ...,
    expires: Incomplete | None = ...,
    *,
    queue: str | None = ...,
    **kwargs,
) -> Callable[[Callable[_P, _T]], TaskWrapper[_T, _P]]: ...
