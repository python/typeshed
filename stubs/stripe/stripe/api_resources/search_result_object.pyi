from _typeshed import Self
from typing import Any, Generic, Iterator, List, TypeVar

from stripe.stripe_object import StripeObject

_T = TypeVar("_T")

class SearchResultObject(StripeObject, Generic[_T]):
    OBJECT_NAME = "search_result"
    url: str
    has_more: bool
    data: List[_T]
    next_page: str
    total_count: int

    def search(
        self: Self, api_key: str | None = ..., stripe_version: str | None = ..., stripe_account: str | None = ..., **params
    ) -> Self: ...
    def __getitem__(self, k: str) -> Any: ...
    def __iter__(self) -> Iterator[_T]: ...
    def __len__(self) -> int: ...
    def auto_paging_iter(self) -> Iterator[_T]: ...
    @classmethod
    def empty_search_result(
        cls: type[Self], api_key: str | None = ..., stripe_version: str | None = ..., stripe_account: str | None = ...
    ) -> Self: ...
    @property
    def is_empty(self) -> bool: ...
    def next_search_result_page(
        self: Self, api_key: str | None = ..., stripe_version: str | None = ..., stripe_account: str | None = ..., **params
    ) -> Self: ...
