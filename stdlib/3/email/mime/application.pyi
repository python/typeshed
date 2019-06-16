# Stubs for email.mime.application (Python 3.4)

from email.mime.nonmultipart import MIMENonMultipart
from typing import Callable, Optional, Tuple, Union

_ParamsType = Union[str, None, Tuple[str, Optional[str], str]]

class MIMEApplication(MIMENonMultipart):
    def __init__(self, _data: Union[str, bytes], _subtype: str = ...,
                 _encoder: Callable[[MIMEApplication], None] = ...,
                 **_params: _ParamsType) -> None: ...
