from logging import Logger

log: Logger
SERVICE_NAME: str
ORIGIN: str
runtime_context: dict | None

def initialize() -> None: ...
