from _typeshed import Incomplete

SIGNAL_CANCELED: str
SIGNAL_COMPLETE: str
SIGNAL_ERROR: str
SIGNAL_EXECUTING: str
SIGNAL_EXPIRED: str
SIGNAL_LOCKED: str
SIGNAL_RETRYING: str
SIGNAL_REVOKED: str
SIGNAL_SCHEDULED: str
SIGNAL_INTERRUPTED: str

class Signal:
    receivers: Incomplete
    def __init__(self) -> None: ...
    def connect(self, receiver, *signals) -> None: ...
    def disconnect(self, receiver, *signals) -> None: ...
    def send(self, signal, task, *args, **kwargs) -> None: ...
