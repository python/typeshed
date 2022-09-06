from _typeshed import Self
from typing import Iterator

from stripe.api_resources.abstract.api_resource import APIResource as APIResource
from stripe.api_resources.search_result_object import SearchResultObject

class SearchableAPIResource(APIResource):
    @classmethod
    def _search(
        cls: type[Self],
        search_url: str,
        api_key: str | None = ...,
        stripe_version: str | None = ...,
        stripe_account: str | None = ...,
        **params,
    ) -> SearchResultObject[Self]: ...
    @classmethod
    def search(cls: type[Self], *args: str | None, **kwargs) -> SearchResultObject[Self]: ...
    @classmethod
    def search_auto_paging_iter(cls: type[Self], *args: str | None, **kwargs) -> Iterator[Self]: ...
