from google.protobuf.message import (
    Message,
)
from google.protobuf.internal import well_known_types

from typing import (
    Optional,
    Text,
)


class Any(Message, well_known_types.Any_):
    type_url = ...  # type: Text
    value = ...  # type: bytes

    def __init__(self,
                 type_url: Optional[Text] = ...,
                 value: Optional[bytes] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> Any: ...
