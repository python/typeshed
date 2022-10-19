from typing import Any

class JSONRPCError(Exception):
    code: int
    message: str | None
    data: Any | None
    status_code: int
    def __init__(
        self, message: str | None = ..., code: int | None = ..., data: Any | None = ..., status_code: int | None = ...
    ) -> None: ...
    @property
    def jsonrpc_format(self) -> dict[str, Any]: ...

class ParseError(JSONRPCError):
    code: int
    message: str | None

class InvalidRequestError(JSONRPCError):
    code: int
    message: str | None

class MethodNotFoundError(JSONRPCError):
    code: int
    message: str | None

class InvalidParamsError(JSONRPCError):
    code: int
    message: str | None

class InternalError(JSONRPCError):
    code: int
    message: str | None

class ServerError(JSONRPCError):
    code: int
    message: str | None
    status_code: int
