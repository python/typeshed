from _typeshed import Incomplete

log: Incomplete
DEFAULT_HOST: str
DEFAULT_PORT: int
DEFAULT_FLUSH_INTERVAL: float
MIN_FLUSH_INTERVAL: float
ENTITY_ID_TAG_NAME: str
ENTITY_ID_ENV_VAR: str
ORIGIN_DETECTION_ENABLED: str
UDP_OPTIMAL_PAYLOAD_LENGTH: int
UDS_OPTIMAL_PAYLOAD_LENGTH: int
MIN_SEND_BUFFER_SIZE: Incomplete
DD_ENV_TAGS_MAPPING: Incomplete
DEFAULT_TELEMETRY_MIN_FLUSH_INTERVAL: int
TELEMETRY_FORMATTING_STR: Incomplete

class DogStatsd:
    OK: Incomplete
    WARNING: Incomplete
    CRITICAL: Incomplete
    UNKNOWN: Incomplete
    socket_timeout: Incomplete
    socket_path: Incomplete
    host: Incomplete
    port: Incomplete
    telemetry_socket_path: Incomplete
    telemetry_host: Incomplete
    telemetry_port: Incomplete
    telemetry_socket_timeout: Incomplete
    socket: Incomplete
    telemetry_socket: Incomplete
    encoding: str
    constant_tags: Incomplete
    namespace: Incomplete
    use_ms: Incomplete
    default_sample_rate: Incomplete
    def __init__(
        self,
        host: str = "localhost",
        port: int = 8125,
        max_buffer_size: None = None,
        flush_interval: float = 0.3,
        disable_buffering: bool = True,
        namespace: str | None = None,
        constant_tags: list[str] | None = None,
        use_ms: bool = False,
        use_default_route: bool = False,
        socket_path: str | None = None,
        default_sample_rate: float = 1,
        disable_telemetry: bool = False,
        telemetry_min_flush_interval: int = 10,
        telemetry_host: str = None,
        telemetry_port: str | int = None,
        telemetry_socket_path: str = None,
        max_buffer_len: int = 0,
        container_id: str | None = None,
        origin_detection_enabled: bool = True,
        socket_timeout: float | None = 0,
        telemetry_socket_timeout: float | None = 0,
        disable_background_sender: bool = True,
        sender_queue_size: int = 0,
        sender_queue_timeout: float | None = 0,
    ) -> None: ...
    def enable_background_sender(self, sender_queue_size: int = 0, sender_queue_timeout: int = 0) -> None: ...
    def disable_telemetry(self) -> None: ...
    def enable_telemetry(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type, value, traceback) -> None: ...
    @property
    def disable_buffering(self): ...
    @staticmethod
    def resolve_host(host, use_default_route): ...
    def get_socket(self, telemetry: bool = False): ...
    def set_socket_timeout(self, timeout) -> None: ...
    def open_buffer(self, max_buffer_size: Incomplete | None = None) -> None: ...
    def close_buffer(self) -> None: ...
    def flush(self) -> None: ...
    def gauge(self, metric: str, value: float, tags: list[str] | None = None, sample_rate: float | None = None): ...
    def increment(
        self, metric: str, value: float = 1, tags: list[str] | None = None, sample_rate: float | None = None
    ) -> None: ...
    def decrement(self, metric: str, value: float = 1, tags: list[str] | None = None, sample_rate: float | None = None): ...
    def histogram(self, metric: str, value: float, tags: list[str] | None = None, sample_rate: float | None = None): ...
    def distribution(self, metric: str, value: float, tags: list[str] | None = None, sample_rate: float | None = None): ...
    def timing(self, metric: str, value: float, tags: list[str] | None = None, sample_rate: float | None = None): ...
    def timed(
        self,
        metric: Incomplete | None = None,
        tags: Incomplete | None = None,
        sample_rate: Incomplete | None = None,
        use_ms: Incomplete | None = None,
    ): ...
    def distributed(
        self,
        metric: Incomplete | None = None,
        tags: Incomplete | None = None,
        sample_rate: Incomplete | None = None,
        use_ms: Incomplete | None = None,
    ): ...
    def set(self, metric, value, tags: Incomplete | None = None, sample_rate: Incomplete | None = None) -> None: ...
    def close_socket(self) -> None: ...
    def event(
        self,
        title,
        message,
        alert_type: Incomplete | None = None,
        aggregation_key: Incomplete | None = None,
        source_type_name: Incomplete | None = None,
        date_happened: Incomplete | None = None,
        priority: Incomplete | None = None,
        tags: Incomplete | None = None,
        hostname: Incomplete | None = None,
    ) -> None: ...
    def service_check(
        self,
        check_name,
        status,
        tags: Incomplete | None = None,
        timestamp: Incomplete | None = None,
        hostname: Incomplete | None = None,
        message: Incomplete | None = None,
    ) -> None: ...
    def wait_for_pending(self) -> None: ...

statsd: Incomplete
