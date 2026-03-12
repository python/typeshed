from collections.abc import Callable
from typing import Any, Concatenate, TypeVar

from behave.runner import Context as Context

_F = TypeVar("_F", bound=Callable[Concatenate[Context, ...], None])

def given(pattern: str, **kwargs: Any) -> Callable[[_F], _F]: ...
def when(pattern: str, **kwargs: Any) -> Callable[[_F], _F]: ...
def then(pattern: str, **kwargs: Any) -> Callable[[_F], _F]: ...
def step(pattern: str, **kwargs: Any) -> Callable[[_F], _F]: ...

# Title-case aliases
Given = given
When = when
Then = then
Step = step
