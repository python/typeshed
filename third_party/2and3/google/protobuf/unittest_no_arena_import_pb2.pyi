from google.protobuf.message import (
    Message,
)
from typing import (
    Optional,
)


class ImportNoArenaNestedMessage(Message):
    d = ...  # type: int

    def __init__(self,
                 d: Optional[int] = ...,
                 ) -> None: ...
