# Stubs for flask.testing (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import IO, Any, Iterable, Mapping, Optional, Union

from click import BaseCommand
from click.testing import CliRunner, Result

from werkzeug.test import Client

def make_test_environ_builder(
    app: Any,
    path: str = ...,
    base_url: Optional[Any] = ...,
    subdomain: Optional[Any] = ...,
    url_scheme: Optional[Any] = ...,
    *args: Any,
    **kwargs: Any,
): ...

class FlaskClient(Client):
    preserve_context: bool = ...
    environ_base: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def session_transaction(self, *args: Any, **kwargs: Any) -> None: ...
    def open(self, *args: Any, **kwargs: Any): ...
    def __enter__(self): ...
    def __exit__(self, exc_type: Any, exc_value: Any, tb: Any) -> None: ...

class FlaskCliRunner(CliRunner):
    app: Any = ...
    def __init__(self, app: Any, **kwargs: Any) -> None: ...
    def invoke(
        self,
        cli: Optional[BaseCommand] = ...,
        args: Optional[Union[str, Iterable[str]]] = ...,
        input: Optional[IO] = ...,
        env: Optional[Mapping[str, str]] = ...,
        catch_exceptions: bool = ...,
        color: bool = ...,
        **extra: Any,
    ) -> Result: ...
