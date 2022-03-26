from _typeshed.email import ParamsType
from collections.abc import Callable
from email.mime.nonmultipart import MIMENonMultipart
from email.policy import Policy

__all__ = ["MIMEImage"]

class MIMEImage(MIMENonMultipart):
    def __init__(
        self,
        _imagedata: str | bytes,
        _subtype: str | None = ...,
        _encoder: Callable[[MIMEImage], None] = ...,
        *,
        policy: Policy | None = ...,
        **_params: ParamsType,
    ) -> None: ...
