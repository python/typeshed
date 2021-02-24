from typing import IO

from logging import Handler, Logger

from .app import Flask

wsgi_errors_stream: IO[str]

def has_level_handler(logger: Logger) -> bool: ...

default_handler: Handler

def create_logger(app: Flask) -> Logger: ...
