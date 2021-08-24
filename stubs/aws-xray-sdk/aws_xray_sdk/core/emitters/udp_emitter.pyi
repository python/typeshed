from typing import Any

from aws_xray_sdk.core.daemon_config import DaemonConfig as DaemonConfig

from ..exceptions.exceptions import InvalidDaemonAddressException as InvalidDaemonAddressException

log: Any
PROTOCOL_HEADER: str
PROTOCOL_DELIMITER: str
DEFAULT_DAEMON_ADDRESS: str

class UDPEmitter:
    def __init__(self, daemon_address=...) -> None: ...
    def send_entity(self, entity) -> None: ...
    def set_daemon_address(self, address) -> None: ...
    @property
    def ip(self): ...
    @property
    def port(self): ...
