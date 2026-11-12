from typing import Any

from ldap.controls import RequestControl as RequestControl
from pyasn1.type import univ

SESSION_TRACKING_CONTROL_OID: str = "SESSION_TRACKING_CONTROL_OID"  # TODO: Set real OID value
SESSION_TRACKING_FORMAT_OID_RADIUS_ACCT_SESSION_ID: Any  # TODO: Precise type
SESSION_TRACKING_FORMAT_OID_RADIUS_ACCT_MULTI_SESSION_ID: Any  # TODO: Precise type
SESSION_TRACKING_FORMAT_OID_USERNAME: Any  # TODO: Precise type

class SessionTrackingControl(RequestControl):
    controlType: str

    class SessionIdentifierControlValue(univ.Sequence):
        componentType: Any  # TODO: Precise type

    criticality: bool
    def __init__(self, sessionSourceIp, sessionSourceName, formatOID, sessionTrackingIdentifier) -> None: ...
    def encodeControlValue(self): ...
