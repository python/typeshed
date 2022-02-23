from typing import TypeVar, overload

from stripe.api_resources.abstract.api_resource import APIResource as APIResource

_T = TypeVar("_T", bound=DeletableAPIResource)

class DeletableAPIResource(APIResource):
    @overload
    @classmethod
    def delete(cls: type[_T], **params) -> _T: ...
    @overload
    @classmethod
    def delete(cls: type[_T], sid: str, **params) -> _T: ...
