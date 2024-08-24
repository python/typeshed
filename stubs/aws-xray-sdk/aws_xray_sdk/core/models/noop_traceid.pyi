class NoOpTraceId:
    VERSION: str
    DELIMITER: str
    start_time: str
    __number: str
    def __init__(self) -> None: ...
    def to_id(self) -> str: ...
