import socket
from datetime import timedelta
from typing import Any
from typing_extensions import override

from gunicorn.config import Config
from gunicorn.glogging import Logger
from gunicorn.http import Request
from gunicorn.http.wsgi import Response

from .._types import _EnvironType
from ..glogging import _LogLevelType

METRIC_VAR: str
VALUE_VAR: str
MTYPE_VAR: str
GAUGE_TYPE: str
COUNTER_TYPE: str
HISTOGRAM_TYPE: str

class Statsd(Logger):
    prefix: str
    sock: socket.socket | None
    dogstatsd_tags: str | None
    cfg: Config

    def __init__(self, cfg: Config) -> None: ...
    @override
    def critical(self, msg: str, *args: Any, **kwargs: Any) -> None: ...
    @override
    def error(self, msg: str, *args: Any, **kwargs: Any) -> None: ...
    @override
    def warning(self, msg: str, *args: Any, **kwargs: Any) -> None: ...
    @override
    def exception(self, msg: str, *args: Any, **kwargs: Any) -> None: ...
    @override
    def info(self, msg: str, *args: Any, **kwargs: Any) -> None: ...
    @override
    def debug(self, msg: str, *args: Any, **kwargs: Any) -> None: ...
    @override
    def log(self, lvl: _LogLevelType, msg: str, *args: Any, **kwargs: Any) -> None: ...
    @override
    def access(self, resp: Response, req: Request, environ: _EnvironType, request_time: timedelta) -> None: ...
    def gauge(self, name: str, value: float) -> None: ...
    def increment(self, name: str, value: int, sampling_rate: float = 1.0) -> None: ...
    def decrement(self, name: str, value: int, sampling_rate: float = 1.0) -> None: ...
    def histogram(self, name: str, value: float) -> None: ...
