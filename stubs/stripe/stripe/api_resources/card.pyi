from typing import Any

from stripe import error as error, util as util
from stripe.api_resources.abstract import (
    DeletableAPIResource as DeletableAPIResource,
    UpdateableAPIResource as UpdateableAPIResource,
)
from stripe.api_resources.account import Account as Account
from stripe.api_resources.customer import Customer as Customer
from stripe.api_resources.recipient import Recipient as Recipient

class Card(DeletableAPIResource, UpdateableAPIResource):
    OBJECT_NAME: str
    def instance_url(self): ...
    @classmethod
    def modify(cls, sid, **params) -> None: ...
    @classmethod
    def retrieve(
        cls, id, api_key: Any | None = ..., stripe_version: Any | None = ..., stripe_account: Any | None = ..., **params
    ) -> None: ...
