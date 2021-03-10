from types import TracebackType
from typing import Optional, Text, Type, Union

from redis.client import Redis

_TokenValue = Union[bytes, Text]

class Lock:
    def __init__(
        self,
        redis: Redis,
        name: str,
        # could be Union[int, float]
        timeout: Union[None, int, float] = ...,
        sleep: float = ...,
        blocking: bool = ...,
        # could be bool
        blocking_timeout: Optional[bool] = ...,
        thread_local: bool = ...,
    ) -> None: ...
    def register_scripts(self) -> None: ...
    def __enter__(self) -> Lock: ...
    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> Optional[bool]: ...
    def acquire(
        self,
        # could be bool
        blocking: Optional[bool] = ...,
        # could be Union[int, float]
        blocking_timeout: Union[None, int, float] = ...,
        token: Optional[_TokenValue] = ...,
    ) -> bool: ...
    def do_acquire(self, token: _TokenValue) -> bool: ...
    def locked(self) -> bool: ...
    def owned(self) -> bool: ...
    def release(self) -> None: ...
    def do_release(self, expected_token: _TokenValue) -> None: ...
    # could be Literal[True]
    def extend(self, additional_time: Union[int, float], replace_ttl: bool = ...) -> bool: ...
    # could be Literal[True]
    def do_extend(self, additional_time: Union[int, float], replace_ttl: bool) -> bool: ...
    # could be Literal[True]
    def reacquire(self) -> bool: ...
    # could be Literal[True]
    def do_reacquire(self) -> bool: ...
