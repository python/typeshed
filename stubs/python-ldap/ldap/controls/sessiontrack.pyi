from _typeshed import Incomplete

from ldap.controls import RequestControl as RequestControl
from pyasn1.type import univ

SESSION_TRACKING_CONTROL_OID: str
SESSION_TRACKING_FORMAT_OID_RADIUS_ACCT_SESSION_ID: Incomplete
SESSION_TRACKING_FORMAT_OID_RADIUS_ACCT_MULTI_SESSION_ID: Incomplete
SESSION_TRACKING_FORMAT_OID_USERNAME: Incomplete

class SessionTrackingControl(RequestControl):
    class SessionIdentifierControlValue(univ.Sequence):
        componentType: Incomplete

    controlType = SESSION_TRACKING_CONTROL_OID
    criticality: bool
    def __init__(self, sessionSourceIp: str, sessionSourceName: str, formatOID: str, sessionTrackingIdentifier: str) -> None: ...
    def encodeControlValue(self) -> bytes: ...
