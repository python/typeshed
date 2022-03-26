from _typeshed.email import ParamsType
from collections.abc import Callable
from email.mime.nonmultipart import MIMENonMultipart
from email.policy import Policy

__all__ = ["MIMEAudio"]

class MIMEAudio(MIMENonMultipart):
    def __init__(
        self,
        _audiodata: str | bytes,
        _subtype: str | None = ...,
        _encoder: Callable[[MIMEAudio], None] = ...,
        *,
        policy: Policy | None = ...,
        **_params: ParamsType,
    ) -> None: ...
