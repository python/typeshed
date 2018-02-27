from typing import IO, List, Text, Optional

from click.core import Context, Parameter


class ClickException(Exception):
    exit_code: int
    message: str

    def __init__(self, message: Text) -> None:
        ...

    def format_message(self) -> Text:
        ...

    def show(self, file=None) -> None:
        ...


class UsageError(ClickException):
    ctx: Optional[Context]

    def __init__(self, message: Text, ctx: Optional[Context] = ...) -> None:
        ...

    def show(self, file: Optional[IO] = ...) -> None:
        ...


class BadParameter(UsageError):
    param: Optional[Parameter]
    param_hint: Optional[Text]

    def __init__(
        self,
        message: Text,
        ctx: Optional[Context] = ...,
        param: Optional[Parameter] = ...,
        param_hint: Optional[Text] = ...
    ) -> None:
        ...


class MissingParameter(BadParameter):
    param_type: Text  # valid values: 'parameter', 'option', 'argument'

    def __init__(
        self,
        message: Optional[Text] = ...,
        ctx: Optional[Context] = ...,
        param: Optional[Parameter] = ...,
        param_hint: Optional[Text] = ...,
        param_type: Optional[Text] = ...
    ) -> None:
        ...


class NoSuchOption(UsageError):
    option_name: Text
    possibilities: Optional[List[Text]]

    def __init__(
        self,
        option_name: Text,
        message: Optional[Text] = ...,
        possibilities: Optional[List[Text]] = ...,
        ctx: Optional[Context] = ...
    ) -> None:
        ...


class BadOptionUsage(UsageError):
    def __init__(self, message: Text, ctx: Optional[Context] = ...) -> None:
        ...


class BadArgumentUsage(UsageError):
    def __init__(self, message: Text, ctx: Optional[Context] = ...) -> None:
        ...


class FileError(ClickException):
    ui_filename: Text
    filename: Text

    def __init__(self, filename: Text, hint: Optional[Text] = ...) -> None:
        ...


class Abort(RuntimeError):
    ...
