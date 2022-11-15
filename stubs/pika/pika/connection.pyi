import abc
from _typeshed import Incomplete

import pika.heartbeat

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
    blocked_connection_timeout: Incomplete
    channel_max: Incomplete
    client_properties: Incomplete
    connection_attempts: Incomplete
    credentials: Incomplete
    frame_max: Incomplete
    heartbeat: Incomplete
    host: Incomplete
    locale: Incomplete
    retry_delay: Incomplete
    socket_timeout: Incomplete
    stack_timeout: Incomplete
    ssl_options: Incomplete
    port: Incomplete
    virtual_host: Incomplete
    tcp_options: Incomplete
    def __init__(
        self,
        host=...,
        port=...,
        virtual_host=...,
        credentials=...,
        channel_max=...,
        frame_max=...,
        heartbeat=...,
        ssl_options=...,
        connection_attempts=...,
        retry_delay=...,
        socket_timeout=...,
        stack_timeout=...,
        locale=...,
        blocked_connection_timeout=...,
        client_properties=...,
        tcp_options=...,
        **kwargs,
    ) -> None: ...

class URLParameters(Parameters):
    ssl_options: Incomplete
    host: Incomplete
    port: Incomplete
    credentials: Incomplete
    virtual_host: Incomplete
    def __init__(self, url) -> None: ...

class SSLOptions:
    context: Incomplete
    server_hostname: Incomplete
    def __init__(self, context, server_hostname: Incomplete | None = ...) -> None: ...

class Connection(pika.compat.AbstractBase, metaclass=abc.ABCMeta):
    ON_CONNECTION_CLOSED: str
    ON_CONNECTION_ERROR: str
    ON_CONNECTION_OPEN_OK: str
    CONNECTION_CLOSED: int
    CONNECTION_INIT: int
    CONNECTION_PROTOCOL: int
    CONNECTION_START: int
    CONNECTION_TUNE: int
    CONNECTION_OPEN: int
    CONNECTION_CLOSING: int
    connection_state: Incomplete
    params: Incomplete
    callbacks: Incomplete
    server_capabilities: Incomplete
    server_properties: Incomplete
    known_hosts: Incomplete
    def __init__(
        self,
        parameters: Incomplete | None = ...,
        on_open_callback: Incomplete | None = ...,
        on_open_error_callback: Incomplete | None = ...,
        on_close_callback: Incomplete | None = ...,
        internal_connection_workflow: bool = ...,
    ) -> None: ...
    def add_on_close_callback(self, callback) -> None: ...
    def add_on_connection_blocked_callback(self, callback) -> None: ...
    def add_on_connection_unblocked_callback(self, callback) -> None: ...
    def add_on_open_callback(self, callback) -> None: ...
    def add_on_open_error_callback(self, callback, remove_default: bool = ...) -> None: ...
    def channel(self, channel_number: Incomplete | None = ..., on_open_callback: Incomplete | None = ...): ...
    def update_secret(self, new_secret, reason, callback: Incomplete | None = ...) -> None: ...
    def close(self, reply_code: int = ..., reply_text: str = ...) -> None: ...
    @property
    def is_closed(self): ...
    @property
    def is_closing(self): ...
    @property
    def is_open(self): ...
    @property
    def basic_nack(self): ...
    @property
    def consumer_cancel_notify(self): ...
    @property
    def exchange_exchange_bindings(self): ...
    @property
    def publisher_confirms(self): ...
