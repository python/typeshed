from collections.abc import Callable
from email import _ParamsType
from email.mime.nonmultipart import MIMENonMultipart
from email.policy import Policy
from typing import Any

__all__ = ["MIMEAudio"]

class MIMEAudio(MIMENonMultipart):
    def __init__(
        self,
        _audiodata: str | bytes | bytearray,
        _subtype: str | None = None,
        _encoder: Callable[[MIMEAudio], object] = ...,
        *,
        policy: Policy[Any] | None = None,
        **_params: _ParamsType,
    ) -> None: ...
