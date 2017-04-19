from typing import Dict, List, Any
import logging

class Flask:
    config = ...  # type: Dict
    logger = ...  # type: logging.Logger

    def __init__(self: Flask, name: str) -> None: ...
    def route(self: Flask, path: str, methods: List[str]=...) -> Any: ...
    def run(self: Flask, host: str=..., port: int=..., debug: bool=..., use_reloader: bool=...) -> Any: ...

class Request:
    data = ...  # type: str

request = ...  # type: Request
