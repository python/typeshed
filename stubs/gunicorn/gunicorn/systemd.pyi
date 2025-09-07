from logging import Logger

SD_LISTEN_FDS_START: int


def listen_fds(unset_environment: bool = True) -> int: ...
def sd_notify(state: str, logger: Logger, unset_environment: bool = False) -> None: ...
