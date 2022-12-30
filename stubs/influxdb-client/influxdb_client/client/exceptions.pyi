from _typeshed import Incomplete

from urllib3 import HTTPResponse as HTTPResponse

logger: Incomplete

class InfluxDBError(Exception):
    response: Incomplete
    message: Incomplete
    retry_after: Incomplete
    def __init__(self, response: HTTPResponse = ..., message: str = ...) -> None: ...
