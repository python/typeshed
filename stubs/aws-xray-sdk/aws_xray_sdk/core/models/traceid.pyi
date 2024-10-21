class TraceId:
    VERSION: str
    DELIMITER: str
    start_time: int
    __number: str
    def __init__(self) -> None: ...
    def to_id(self) -> str: ...
