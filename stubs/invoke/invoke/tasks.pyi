from _typeshed import Self
from typing import Any, Callable, Iterable, TypeVar

from .config import Config
from .context import Context
from .parser import Argument

NO_DEFAULT: object

class Task:
    body: Callable[..., Any]
    __doc__: str | None
    __name__: str
    __module__: str | None
    aliases: tuple[str]
    is_default: bool
    positional: Iterable[str]
    optional: Iterable[str]
    iterable: Iterable[str]
    incrementable: Iterable[str]
    auto_shortflags: bool
    help: dict[str, str]
    pre: list[Task]
    post: list[Task]
    times_called: int
    autoprint: bool
    def __init__(
        self,
        body: Callable[..., Any],
        name: str | None = ...,
        aliases: tuple[str] = ...,
        positional: Iterable[str] | None = ...,
        optional: Iterable[str] = ...,
        default: bool = ...,
        auto_shortflags: bool = ...,
        help: dict[str, str] | None = ...,
        pre: list[Task] | None = ...,
        post: list[Task] | None = ...,
        autoprint: bool = ...,
        iterable: Iterable[str] | None = ...,
        incrementable: Iterable[str] | None = ...,
    ) -> None: ...
    @property
    def name(self): ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __call__(self, *args, **kwargs): ...
    @property
    def called(self) -> int: ...
    def argspec(self, body): ...
    def fill_implicit_positionals(self, positional: Iterable[str] | None) -> Iterable[str]: ...
    def arg_opts(self, name: str, default: Any, taken_names: Iterable[str]) -> dict[str, Any]: ...
    def get_arguments(self) -> list[Argument]: ...

TASK = TypeVar("TASK", bound=Task)

def task(
    *args: Task,
    name: str | None = ...,
    aliases: tuple[str] = ...,
    positional: Iterable[str] | None = ...,
    optional: Iterable[str] = ...,
    default: bool = ...,
    auto_shortflags: bool = ...,
    help: dict[str, str] | None = ...,
    pre: list[Task] | None = ...,
    post: list[Task] | None = ...,
    autoprint: bool = ...,
    iterable: Iterable[str] | None = ...,
    incrementable: Iterable[str] | None = ...,
    klass: type[TASK] = ...,
) -> TASK: ...

class Call:
    task: Task
    called_as: str | None
    args: tuple[Any, ...]
    kwargs: dict[str, Any]
    def __init__(
        self, task: Task, called_as: str | None = ..., args: tuple[Any, ...] | None = ..., kwargs: dict[str, Any] | None = ...
    ) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    def __deepcopy__(self: Self, memo: Any) -> Self: ...
    def __eq__(self, other: Call) -> bool: ...  # type: ignore[override]
    def make_context(self, config: Config) -> Context: ...
    def clone_data(self): ...
    # TODO use overload
    def clone(self, into: type[Call] | None = ..., with_: dict[str, Any] | None = ...) -> Call: ...

def call(task: Task, *args: Any, **kwargs: Any) -> Call: ...
