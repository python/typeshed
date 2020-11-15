import socket
from typing import List, Mapping, Tuple

from paramiko.pkey import PKey

class SSHException(Exception): ...
class AuthenticationException(SSHException): ...
class PasswordRequiredException(AuthenticationException): ...

class BadAuthenticationType(AuthenticationException):
    explanation: str
    allowed_types: List[str]
    def __init__(self, explanation: str, types: List[str]) -> None: ...

class PartialAuthentication(AuthenticationException):
    allowed_types: List[str]
    def __init__(self, types: List[str]) -> None: ...

class ChannelException(SSHException):
    code: int
    text: int
    def __init__(self, code: int, text: int) -> None: ...

class BadHostKeyException(SSHException):
    hostname: str
    key: PKey
    expected_key: PKey
    def __init__(self, hostname: str, got_key: PKey, expected_key: PKey) -> None: ...

class ProxyCommandFailure(SSHException):
    command: str
    error: str
    def __init__(self, command: str, error: str) -> None: ...

class NoValidConnectionsError(socket.error):
    errors: Mapping[Tuple[str, int], Exception]
    def __init__(self, errors: Mapping[Tuple[str, int], Exception]) -> None: ...
    def __reduce__(self): ...

class CouldNotCanonicalize(SSHException): ...
class ConfigParseError(SSHException): ...
