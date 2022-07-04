import logging
from collections.abc import Iterator, Sequence

from ..std import tqdm as std_tqdm

def logging_redirect_tqdm(loggers: Sequence[logging.Logger] | None = ..., tqdm_class: type[std_tqdm[object]] = ...) -> Iterator[
    None]: ...


def tqdm_logging_redirect(*args, **kwargs) -> Iterator[None]: ...
