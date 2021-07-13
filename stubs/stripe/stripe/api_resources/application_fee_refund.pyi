from typing import Any

from stripe import util as util
from stripe.api_resources import ApplicationFee as ApplicationFee
from stripe.api_resources.abstract import UpdateableAPIResource as UpdateableAPIResource

class ApplicationFeeRefund(UpdateableAPIResource):
    OBJECT_NAME: str
    @classmethod
    def modify(cls, fee, sid, **params): ...
    def instance_url(self): ...
    @classmethod
    def retrieve(cls, id, api_key: Any | None = ..., **params) -> None: ...
