from email.mime.nonmultipart import MIMENonMultipart
from email.policy import Policy
from typing import Any

__all__ = ["MIMEText"]

class MIMEText(MIMENonMultipart):
    def __init__(
        self, _text: str, _subtype: str = "plain", _charset: str | None = None, *, policy: Policy[Any] | None = None
    ) -> None: ...
