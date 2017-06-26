from typing import Any, Optional

class PynamoDBException(Exception):
    msg: str
    cause: Any
    def __init__(self, msg: Optional[Any] = ..., cause: Optional[Any] = ...) -> None: ...

class PynamoDBConnectionError(PynamoDBException):
    pass

class DeleteError(PynamoDBConnectionError):
    pass

class QueryError(PynamoDBConnectionError):
    pass

class ScanError(PynamoDBConnectionError):
    pass

class PutError(PynamoDBConnectionError):
    pass

class UpdateError(PynamoDBConnectionError):
    pass

class GetError(PynamoDBConnectionError):
    pass

class TableError(PynamoDBConnectionError):
    pass

class DoesNotExist(PynamoDBException):
    pass

class TableDoesNotExist(PynamoDBException):
    def __init__(self, table_name) -> None: ...

class VerboseClientError(Exception):
    MSG_TEMPLATE: Any
    def __init__(self, error_response, operation_name, verbose_properties: Optional[Any] = ...) -> None: ...
