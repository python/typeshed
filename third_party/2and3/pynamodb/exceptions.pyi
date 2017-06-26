from typing import Any, Optional

class PynamoDBException(Exception):
    msg: Any
    cause: Any
    def __init__(self, msg: Optional[Any] = ..., cause: Optional[Any] = ...) -> None: ...

class PynamoDBConnectionError(PynamoDBException):
    msg: str

class DeleteError(PynamoDBConnectionError):
    msg: str

class QueryError(PynamoDBConnectionError):
    msg: str

class ScanError(PynamoDBConnectionError):
    msg: str

class PutError(PynamoDBConnectionError):
    msg: str

class UpdateError(PynamoDBConnectionError):
    msg: str

class GetError(PynamoDBConnectionError):
    msg: str

class TableError(PynamoDBConnectionError):
    msg: str

class DoesNotExist(PynamoDBException):
    msg: str

class TableDoesNotExist(PynamoDBException):
    def __init__(self, table_name) -> None: ...

class VerboseClientError(Exception):
    MSG_TEMPLATE: Any
    def __init__(self, error_response, operation_name, verbose_properties: Optional[Any] = ...) -> None: ...
