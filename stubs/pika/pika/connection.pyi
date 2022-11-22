import abc
from _typeshed import Incomplete, Self
from collections.abc import Callable
from typing_extensions import Final

from .callback import CallbackManager
from .channel import Channel
from .compat import AbstractBase
from .credentials import _Credentials
from .frame import Method

PRODUCT: str
LOGGER: Incomplete

class Parameters:
    DEFAULT_USERNAME: str
    DEFAULT_PASSWORD: str
    DEFAULT_BLOCKED_CONNECTION_TIMEOUT: Incomplete
    DEFAULT_CHANNEL_MAX: Incomplete
    DEFAULT_CLIENT_PROPERTIES: Incomplete
    DEFAULT_CREDENTIALS: Incomplete
    DEFAULT_CONNECTION_ATTEMPTS: int
    DEFAULT_FRAME_MAX: Incomplete
    DEFAULT_HEARTBEAT_TIMEOUT: Incomplete
    DEFAULT_HOST: str
    DEFAULT_LOCALE: str
    DEFAULT_PORT: int
    DEFAULT_RETRY_DELAY: float
    DEFAULT_SOCKET_TIMEOUT: float
    DEFAULT_STACK_TIMEOUT: float
    DEFAULT_SSL: bool
    DEFAULT_SSL_OPTIONS: Incomplete
    DEFAULT_SSL_PORT: int
    DEFAULT_VIRTUAL_HOST: str
    DEFAULT_TCP_OPTIONS: Incomplete
    def __init__(self) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    @property
    def blocked_connection_timeout(self): ...
    @blocked_connection_timeout.setter
    def blocked_connection_timeout(self, value) -> None: ...
    @property
    def channel_max(self): ...
    @channel_max.setter
    def channel_max(self, value) -> None: ...
    @property
    def client_properties(self): ...
    @client_properties.setter
    def client_properties(self, value) -> None: ...
    @property
    def connection_attempts(self): ...
    @connection_attempts.setter
    def connection_attempts(self, value) -> None: ...
    @property
    def credentials(self): ...
    @credentials.setter
    def credentials(self, value) -> None: ...
    @property
    def frame_max(self): ...
    @frame_max.setter
    def frame_max(self, value) -> None: ...
    @property
    def heartbeat(self): ...
    @heartbeat.setter
    def heartbeat(self, value) -> None: ...
    @property
    def host(self): ...
    @host.setter
    def host(self, value) -> None: ...
    @property
    def locale(self): ...
    @locale.setter
    def locale(self, value) -> None: ...
    @property
    def port(self): ...
    @port.setter
    def port(self, value) -> None: ...
    @property
    def retry_delay(self): ...
    @retry_delay.setter
    def retry_delay(self, value) -> None: ...
    @property
    def socket_timeout(self): ...
    @socket_timeout.setter
    def socket_timeout(self, value) -> None: ...
    @property
    def stack_timeout(self): ...
    @stack_timeout.setter
    def stack_timeout(self, value) -> None: ...
    @property
    def ssl_options(self): ...
    @ssl_options.setter
    def ssl_options(self, value) -> None: ...
    @property
    def virtual_host(self): ...
    @virtual_host.setter
    def virtual_host(self, value) -> None: ...
    @property
    def tcp_options(self): ...
    @tcp_options.setter
    def tcp_options(self, value) -> None: ...

class ConnectionParameters(Parameters):
    class _DEFAULT: ...
    # The following attributes only exist if set in the constructor.
    blocked_connection_timeout: float
    channel_max: int
    client_properties: Incomplete
    connection_attempts: int
    credentials: _Credentials
    frame_max: int
    heartbeat: int | Callable[[Connection, int], int] | None
    host: str
    locale: str
    retry_delay: int | float
    socket_timeout: int | float
    stack_timeout: int | float
    ssl_options: SSLOptions
    port: int
    virtual_host: str
    tcp_options: Incomplete | None

    def __init__(
        self,
        host: str = ...,
        port: int = ...,
        virtual_host: str = ...,
        credentials: _Credentials = ...,
        channel_max: int = ...,
        frame_max: int = ...,
        heartbeat: int | Callable[[Connection, int], int] | None = ...,
        ssl_options: SSLOptions = ...,
        connection_attempts: int = ...,
        retry_delay: float = ...,
        socket_timeout: float = ...,
        stack_timeout: float = ...,
        locale: str = ...,
        blocked_connection_timeout: float = ...,
        client_properties: Incomplete | None = ...,
        tcp_options: Incomplete | None = ...,
    ) -> None: ...

class URLParameters(Parameters):
    ssl_options: Incomplete
    host: Incomplete
    port: Incomplete
    credentials: _Credentials
    virtual_host: Incomplete
    def __init__(self, url) -> None: ...

class SSLOptions:
    context: Incomplete
    server_hostname: Incomplete
    def __init__(self, context, server_hostname: Incomplete | None = ...) -> None: ...

class Connection(AbstractBase, metaclass=abc.ABCMeta):
    ON_CONNECTION_CLOSED: str
    ON_CONNECTION_ERROR: str
    ON_CONNECTION_OPEN_OK: str
    CONNECTION_CLOSED: Final[int]
    CONNECTION_INIT: Final[int]
    CONNECTION_PROTOCOL: Final[int]
    CONNECTION_START: Final[int]
    CONNECTION_TUNE: Final[int]
    CONNECTION_OPEN: Final[int]
    CONNECTION_CLOSING: Final[int]
    connection_state: int  # one of the constants above
    params: Parameters
    callbacks: CallbackManager
    server_capabilities: Incomplete
    server_properties: Incomplete
    known_hosts: Incomplete
    def __init__(
        self: Self,
        parameters: Parameters | None = ...,
        on_open_callback: Callable[[Self], object] | None = ...,
        on_open_error_callback: Callable[[Self, BaseException], object] | None = ...,
        on_close_callback: Callable[[Self, BaseException], object] | None = ...,
        internal_connection_workflow: bool = ...,
    ) -> None: ...
    def add_on_close_callback(self: Self, callback: Callable[[Self, BaseException], object]) -> None: ...
    def add_on_connection_blocked_callback(self: Self, callback: Callable[[Self, Method], object]) -> None: ...
    def add_on_connection_unblocked_callback(self: Self, callback: Callable[[Self, Method], object]) -> None: ...
    def add_on_open_callback(self: Self, callback: Callable[[Self], object]) -> None: ...
    def add_on_open_error_callback(
        self: Self, callback: Callable[[Self, BaseException], object], remove_default: bool = ...
    ) -> None: ...
    def channel(
        self, channel_number: int | None = ..., on_open_callback: Callable[[Channel], object] | None = ...
    ) -> Channel: ...
    def update_secret(self, new_secret, reason, callback: Incomplete | None = ...) -> None: ...
    def close(self, reply_code: int = ..., reply_text: str = ...) -> None: ...
    @property
    def is_closed(self) -> bool: ...
    @property
    def is_closing(self) -> bool: ...
    @property
    def is_open(self) -> bool: ...
    @property
    def basic_nack(self) -> bool: ...
    @property
    def consumer_cancel_notify(self) -> bool: ...
    @property
    def exchange_exchange_bindings(self) -> bool: ...
    @property
    def publisher_confirms(self) -> bool: ...
