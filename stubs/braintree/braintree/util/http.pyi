from _typeshed import Incomplete
from typing import Final

class Http:
    class ContentType:
        Xml: Final = "application/xml"
        Multipart: Final = "multipart/form-data"
        Json: Final = "application/json"

    @staticmethod
    def is_error_status(status): ...
    @staticmethod
    def raise_exception_from_status(status, message: Incomplete | None = None) -> None: ...
    config: Incomplete
    environment: Incomplete
    def __init__(self, config, environment: Incomplete | None = None) -> None: ...
    def post(self, path, params: Incomplete | None = None): ...
    def delete(self, path): ...
    def get(self, path): ...
    def put(self, path, params: Incomplete | None = None): ...
    def post_multipart(self, path, files, params: Incomplete | None = None): ...
    def http_do(self, http_verb, path, headers, request_body): ...
    def handle_exception(self, exception) -> None: ...
