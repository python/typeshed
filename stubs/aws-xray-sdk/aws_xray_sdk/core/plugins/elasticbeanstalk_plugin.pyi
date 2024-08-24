from logging import Logger

log: Logger
CONF_PATH: str
SERVICE_NAME: str
ORIGIN: str
runtime_context: dict | None

def initialize() -> None: ...
