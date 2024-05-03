from typing import Any, Generic, NoReturn, Sequence, TypeVar
from typing_extensions import Self

from docker import APIClient

_T = TypeVar("_T", bound=Model)

class Model:
    id_attribute: str
    client: APIClient | None
    collection: Collection[Self] | None
    attrs: dict[str, Any]
    def __init__(
        self, attrs: dict[str, Any] | None = None, client: APIClient | None = None, collection: Collection[Self] | None = None
    ) -> None: ...
    def __eq__(self, other) -> bool: ...
    def __hash__(self) -> int: ...
    @property
    def id(self) -> str | None: ...
    @property
    def short_id(self) -> str: ...
    def reload(self) -> None: ...

class Collection(Generic[_T]):
    model: type[_T]
    client: APIClient
    def __init__(self, client: APIClient | None = None) -> None: ...
    def __call__(self, *args, **kwargs) -> NoReturn: ...
    def list(self) -> Sequence[_T]: ...
    def get(self, key: str) -> _T: ...
    def create(self, attrs: Any | None = None) -> _T: ...
    def prepare_model(self, attrs: Model | dict[str, Any]) -> _T: ...
