# Stubs for logging.config (Python 3.4)

from typing import Any, Callable, Dict, Optional, IO, Union
import sys
# TODO uncomment when mypy handle conditionals
#if sys.version_info >= (3,):
#    from configparser import RawConfigParser
#else:
#    from ConfigParser import RawConfigParser
# TODO add RawConfigParser to configparser stubs
RawConfigParser = Any


def dictConfig(config: Dict[str, Any]) -> None: ...
if sys.version_info >= (3, 4):
    def fileConfig(fname: Union[str, IO[str], RawConfigParser],
                   defaults: Optional[Dict[str, str]] = ...,
                   disable_existing_loggers: bool = ...) -> None: ...
    def listen(port: int = ...,
               verify: Optional[Callable[[bytes], Optional[bytes]]] = ...) \
               -> None: ...
else:
    def fileConfig(  # type: ignore
                   fname: Union[str, IO[str]],
                   defaults: Optional[Dict[str, str]] = ...,
                   disable_existing_loggers: bool = ...) -> None: ...
    def listen(  # type: ignore
               port: int = ...) -> None: ...
def stopListening() -> None: ...
