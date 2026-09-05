from _typeshed import Incomplete
from collections.abc import AsyncIterable, Iterable, Mapping, MutableMapping, Sequence
from typing import Final, TypeAlias

HTTPX_CLIENT_KWARGS: Final[list[str]]

Request: TypeAlias = Incomplete  # actual type is httpx2.Request
_URL: TypeAlias = Incomplete  # actual type is httpx2.URL
_Headers: TypeAlias = MutableMapping[str, str]  # actual type is httpx2.Headers
_HeaderTypes: TypeAlias = (  # actual type is httpx2._types.HeaderTypes
    _Headers | Mapping[str, str] | Mapping[bytes, bytes] | Sequence[tuple[str, str]] | Sequence[tuple[bytes, bytes]]
)
_RequestContent: TypeAlias = str | bytes | Iterable[bytes] | AsyncIterable[bytes]  # actual type is httpx2._types.RequestContent

def extract_client_kwargs(kwargs: dict[str, Incomplete]) -> dict[str, Incomplete]: ...
def build_request(url: _URL | str, headers: _HeaderTypes | None, body: _RequestContent, initial_request: Request) -> Request: ...
