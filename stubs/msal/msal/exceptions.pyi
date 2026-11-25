class MsalError(Exception):
    msg: str

class MsalServiceError(MsalError):
    msg: str
    def __init__(self, *args: object, error: str | None, error_description: str | None) -> None: ...
