from email.message import Message
from email.mime.base import MIMEBase
from email.policy import Policy
from typing import  Sequence, Tuple

_ParamsType = str | None | Tuple[str, str | None, str]

class MIMEMultipart(MIMEBase):
    def __init__(
        self,
        _subtype: str = ...,
        boundary: str | None = ...,
        _subparts: Sequence[Message] | None = ...,
        *,
        policy: Policy | None = ...,
        **_params: _ParamsType,
    ) -> None: ...
