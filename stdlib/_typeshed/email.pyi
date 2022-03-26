from email.message import Message
from typing import TypeVar, Union

MessageT = TypeVar("MessageT", bound=Message)  # noqa: Y001
ParamType = Union[str, tuple[str | None, str | None, str]]
ParamsType = Union[str, None, tuple[str, str | None, str]]
