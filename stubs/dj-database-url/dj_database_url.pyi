from typing import Any
from typing_extensions import TypedDict

DEFAULT_ENV: str
SCHEMES: dict[str, str]

class _DBConfig(TypedDict, total=False):
    ENGINE: str
    NAME: str
    USER: str
    PASSWORD: str
    HOST: str
    PORT: str
    CONN_MAX_AGE: int
    OPTIONS: dict[str, Any]

def parse(url: str, engine: str | None = ..., conn_max_age: int = ..., ssl_require: bool = ...) -> _DBConfig: ...
def config(
    env: str = ..., default: str | None = ..., engine: str | None = ..., conn_max_age: int = ..., ssl_require: bool = ...
) -> _DBConfig: ...
