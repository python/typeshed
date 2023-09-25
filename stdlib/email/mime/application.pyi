from collections.abc import Callable
from email import _ParamsType
from email.mime.nonmultipart import MIMENonMultipart
from email.policy import Policy
from typing import Any

__all__ = ["MIMEApplication"]

class MIMEApplication(MIMENonMultipart):
    def __init__(
        self,
        _data: str | bytes | bytearray,
        _subtype: str = "octet-stream",
        _encoder: Callable[[MIMEApplication], object] = ...,
        *,
        policy: Policy[Any] | None = None,
        **_params: _ParamsType,
    ) -> None: ...
