from _typeshed import Incomplete
from collections.abc import Callable
from typing import TypeVar
from typing_extensions import ParamSpec

from huey import Huey
from huey.api import Task, TaskWrapper

configuration_message: str
default_backend_path: str

def default_queue_name(): ...
def get_backend(import_path=...): ...
def config_error(msg) -> None: ...

HUEY: Huey
RedisHuey: Incomplete
huey_config: Incomplete
name: Incomplete
backend_path: Incomplete
conn_kwargs: Incomplete
backend_cls: Incomplete

_T = TypeVar("_T")
_P = ParamSpec("_P")

# When changing these functions, also change the corresponding functions in
# stubs/django-huey/django_huey/__init__.pyi and
# stubs/huey/huey/api.pyi
def task(
    retries: int = ...,
    retry_delay: int = ...,
    priority: Incomplete | None = ...,
    context: bool = ...,
    name: Incomplete | None = ...,
    expires: Incomplete | None = ...,
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
    **kwargs,
) -> Callable[[Callable[_P, _T]], TaskWrapper[_T, _P]]: ...
def lock_task(lock_name): ...
def enqueue(task: Task[_T]) -> _T: ...
def restore(task): ...
def restore_all(task_class): ...
def restore_by_id(id): ...
def revoke(task, revoke_until: Incomplete | None = ..., revoke_once: bool = ...) -> None: ...
def revoke_all(task_class, revoke_until: Incomplete | None = ..., revoke_once: bool = ...) -> None: ...
def revoke_by_id(id, revoke_until: Incomplete | None = ..., revoke_once: bool = ...): ...
def is_revoked(task, timestamp: Incomplete | None = ..., peek: bool = ...): ...
def result(
    id,
    blocking: bool = ...,
    timeout: Incomplete | None = ...,
    backoff: float = ...,
    max_delay: float = ...,
    revoke_on_timeout: bool = ...,
    preserve: bool = ...,
): ...
def scheduled(limit: Incomplete | None = ...): ...
def on_startup(name: Incomplete | None = ...): ...
def on_shutdown(name: Incomplete | None = ...): ...
def pre_execute(name: Incomplete | None = ...): ...
def post_execute(self, name: Incomplete | None = ...): ...
def signal(self, *signals): ...
def disconnect_signal(self, receiver, *signals) -> None: ...
def close_db(fn): ...
def db_task(
    retries: int = ...,
    retry_delay: int = ...,
    priority: Incomplete | None = ...,
    context: bool = ...,
    name: Incomplete | None = ...,
    expires: Incomplete | None = ...,
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
    **kwargs,
) -> Callable[[Callable[_P, _T]], TaskWrapper[_T, _P]]: ...
