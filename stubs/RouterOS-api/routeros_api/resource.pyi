from collections.abc import Iterable, Iterator, Mapping
from typing import Generic, Protocol, TypeVar, type_check_only
from typing_extensions import Never

from routeros_api.api_communicator.base import AsynchronousResponse
from routeros_api.api_structure import _Field
from routeros_api.query import _Query

_In = TypeVar("_In")
_Out = TypeVar("_Out")
_V = TypeVar("_V")

# A reply still being received: its rows as they come, or the whole reply once done.
@type_check_only
class _ResponsePromise(Protocol[_V]):
    def get(self) -> AsynchronousResponse[dict[str, _V]]: ...
    def __iter__(self) -> Iterator[dict[str, _V]]: ...

# What a resource needs of its communicator, such as a RouterOsApi's. A str value is encoded; a
# None argument is sent without a value.
@type_check_only
class _Communicator(Protocol):
    def call(
        self,
        path: str,
        command: str,
        arguments: Mapping[str, bytes | str | None] | None = None,
        queries: Mapping[str, bytes | str] | None = None,
        additional_queries: Iterable[_Query] = (),
    ) -> _ResponsePromise[bytes]: ...

# get and its variants filter the rows by their keyword arguments; set, add and remove send them as
# the command's arguments, a None argument without a value. Rows hold the router's bytes.
class RouterOsBinaryResource:
    communicator: _Communicator
    path: str
    def __init__(self, communicator: _Communicator, path: str) -> None: ...
    def get(self, **kwargs: bytes | str) -> AsynchronousResponse[dict[str, bytes]]: ...
    def get_async(self, **kwargs: bytes | str) -> _ResponsePromise[bytes]: ...
    def detailed_get(self, **kwargs: bytes | str) -> AsynchronousResponse[dict[str, bytes]]: ...
    def detailed_get_async(self, **kwargs: bytes | str) -> _ResponsePromise[bytes]: ...
    def set(self, **kwargs: bytes | str | None) -> AsynchronousResponse[dict[str, bytes]]: ...
    # The runtime's set_async calls the synchronous call, so it returns the reply itself.
    def set_async(self, **kwargs: bytes | str | None) -> AsynchronousResponse[dict[str, bytes]]: ...
    def add(self, **kwargs: bytes | str | None) -> AsynchronousResponse[dict[str, bytes]]: ...
    def add_async(self, **kwargs: bytes | str | None) -> _ResponsePromise[bytes]: ...
    def remove(self, **kwargs: bytes | str | None) -> AsynchronousResponse[dict[str, bytes]]: ...
    def remove_async(self, **kwargs: bytes | str | None) -> _ResponsePromise[bytes]: ...
    def call(
        self,
        command: str,
        arguments: Mapping[str, bytes | str | None] | None = None,
        queries: Mapping[str, bytes | str] | None = None,
        additional_queries: Iterable[_Query] = (),
    ) -> AsynchronousResponse[dict[str, bytes]]: ...
    def call_async(
        self,
        command: str,
        arguments: Mapping[str, bytes | str | None] | None = None,
        queries: Mapping[str, bytes | str] | None = None,
        additional_queries: Iterable[_Query] = (),
    ) -> _ResponsePromise[bytes]: ...

# The structure's field for each key encodes the arguments and queries (_In) and decodes the rows'
# values (_Out). The runtime's methods take only what the structure's fields encode, unlike the
# binary resource's they inherit, hence the ignored overrides.
class RouterOsResource(RouterOsBinaryResource, Generic[_In, _Out]):
    structure: Mapping[str, _Field[_In, _Out]]
    def __init__(self, communicator: _Communicator, path: str, structure: Mapping[str, _Field[_In, _Out]]) -> None: ...
    def get(self, **kwargs: _In) -> AsynchronousResponse[dict[str, _Out]]: ...  # type: ignore[override]
    def get_async(self, **kwargs: _In) -> TypedPromiseDecorator[_Out]: ...  # type: ignore[override]
    def detailed_get(self, **kwargs: _In) -> AsynchronousResponse[dict[str, _Out]]: ...  # type: ignore[override]
    def detailed_get_async(self, **kwargs: _In) -> TypedPromiseDecorator[_Out]: ...  # type: ignore[override]
    def set(self, **kwargs: _In | None) -> AsynchronousResponse[dict[str, _Out]]: ...  # type: ignore[override]
    def set_async(self, **kwargs: _In | None) -> AsynchronousResponse[dict[str, _Out]]: ...  # type: ignore[override]
    def add(self, **kwargs: _In | None) -> AsynchronousResponse[dict[str, _Out]]: ...  # type: ignore[override]
    def add_async(self, **kwargs: _In | None) -> TypedPromiseDecorator[_Out]: ...  # type: ignore[override]
    def remove(self, **kwargs: _In | None) -> AsynchronousResponse[dict[str, _Out]]: ...  # type: ignore[override]
    def remove_async(self, **kwargs: _In | None) -> TypedPromiseDecorator[_Out]: ...  # type: ignore[override]
    def call(  # type: ignore[override]
        self,
        command: str,
        arguments: Mapping[str, _In | None] | None = None,
        queries: Mapping[str, _In] | None = None,
        additional_queries: Iterable[_Query] = (),
    ) -> AsynchronousResponse[dict[str, _Out]]: ...
    def call_async(  # type: ignore[override]
        self,
        command: str,
        arguments: Mapping[str, _In | None] | None = None,
        queries: Mapping[str, _In] | None = None,
        additional_queries: Iterable[_Query] = (),
    ) -> TypedPromiseDecorator[_Out]: ...
    def transform_dictionary(self, dictionary: Mapping[str, _In | None]) -> dict[str, bytes | None]: ...
    def transform_item(self, item: tuple[str, _In | None]) -> tuple[str, bytes | None]: ...
    def decorate_promise(self, promise: _ResponsePromise[bytes]) -> TypedPromiseDecorator[_Out]: ...

# The path with a leading and a trailing slash added where missing.
def clean_path(path: str) -> str: ...

# Decodes the rows of a binary reply by the structure's fields; a None value stays None.
class TypedPromiseDecorator(Generic[_Out]):
    inner: _ResponsePromise[bytes]
    structure: Mapping[str, _Field[Never, _Out]]
    def __init__(self, inner: _ResponsePromise[bytes], structure: Mapping[str, _Field[Never, _Out]]) -> None: ...
    def __iter__(self) -> Iterator[dict[str, _Out]]: ...
    def get(self) -> AsynchronousResponse[dict[str, _Out]]: ...
    def transform_dictionary(self, row: Mapping[str, bytes | None]) -> dict[str, _Out | None]: ...
    def transform_item(self, item: tuple[str, bytes | None]) -> tuple[str, _Out | None]: ...
