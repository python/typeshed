from logging import Logger

LOG: Logger
__version__: str
__version_info__: tuple[int, int, int]
LOG_FORMAT: str

def configure_logging(
    verbosity: int,
    filename: str | None = None,
    logformat: str = "%(name)-25s %(processName)-11s %(relativeCreated)6d %(levelname)-8s %(message)s",
) -> None: ...
