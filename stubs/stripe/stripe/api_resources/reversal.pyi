from typing import Any

from stripe import util as util
from stripe.api_resources.abstract import UpdateableAPIResource as UpdateableAPIResource
from stripe.api_resources.transfer import Transfer as Transfer

class Reversal(UpdateableAPIResource):
    OBJECT_NAME: str
    def instance_url(self): ...
    @classmethod
    def modify(cls, sid, **params) -> None: ...
    @classmethod
    def retrieve(cls, id, api_key: Any | None = ..., **params) -> None: ...
