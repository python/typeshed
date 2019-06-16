# Stubs for email.mime.multipart (Python 3.4)

from email.message import Message
from email.mime.base import MIMEBase
from typing import Optional, Sequence, Tuple, Union

_ParamsType = Union[str, None, Tuple[str, Optional[str], str]]

class MIMEMultipart(MIMEBase):
    def __init__(self, _subtype: str = ..., boundary: Optional[str] = ...,
                 _subparts: Optional[Sequence[Message]] = ...,
                 **_params: _ParamsType) -> None: ...
