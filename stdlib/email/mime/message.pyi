from email.message import Message
from email.mime.nonmultipart import MIMENonMultipart
from email.policy import Policy
from typing import Any

__all__ = ["MIMEMessage"]

class MIMEMessage(MIMENonMultipart):
    def __init__(self, _msg: Message, _subtype: str = "rfc822", *, policy: Policy[Any] | None = None) -> None: ...
