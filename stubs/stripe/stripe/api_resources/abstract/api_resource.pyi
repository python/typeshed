from _typeshed import Incomplete
from typing_extensions import Self

from stripe import api_requestor as api_requestor, error as error
from stripe.stripe_object import StripeObject as StripeObject

class APIResource(StripeObject):
    @classmethod
    def retrieve(cls, id, api_key: Incomplete | None = None, **params) -> Self: ...
    def refresh(self) -> Self: ...
    @classmethod
    def class_url(cls) -> str: ...
    def instance_url(self) -> str: ...
