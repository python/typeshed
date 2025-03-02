from collections.abc import Sequence
from email import _ParamsType
from email.mime.base import MIMEBase
from email.policy import Policy, _MessageT

__all__ = ["MIMEMultipart"]

class MIMEMultipart(MIMEBase):
    def __init__(
        self,
        _subtype: str = "mixed",
        boundary: str | None = None,
        _subparts: Sequence[_MessageT] | None = None,
        *,
        policy: Policy[_MessageT] | None = None,
        **_params: _ParamsType,
    ) -> None: ...
