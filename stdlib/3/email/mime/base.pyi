# Stubs for email.mime.base (Python 3.4)

import sys
from typing import Optional, Tuple, Union
import email.message
from email.policy import Policy

_ParamsType = Union[str, None, Tuple[str, Optional[str], str]]

class MIMEBase(email.message.Message):
    if sys.version_info >= (3, 6):
        def __init__(self, _maintype: str, _subtype: str,
                     *, policy: Optional[Policy] = ...,
                     **_params: _ParamsType) -> None: ...
    else:
        def __init__(self, _maintype: str, _subtype: str,
                     **_params: _ParamsType) -> None: ...
