# Stubs for email.mime.text (Python 3.4)

from email.mime.nonmultipart import MIMENonMultipart
from typing import Optional

class MIMEText(MIMENonMultipart):
    def __init__(self, _text: str, _subtype: str = ...,
                 _charset: Optional[str] = ...) -> None: ...
