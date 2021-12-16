from email.mime.nonmultipart import MIMENonMultipart
from email.policy import Policy
from typing import Callable, Tuple

_ParamsType = str | None | Tuple[str, str | None, str]

class MIMEAudio(MIMENonMultipart):
    def __init__(
        self,
        _audiodata: str | bytes,
        _subtype: str | None = ...,
        _encoder: Callable[[MIMEAudio], None] = ...,
        *,
        policy: Policy | None = ...,
        **_params: _ParamsType,
    ) -> None: ...
