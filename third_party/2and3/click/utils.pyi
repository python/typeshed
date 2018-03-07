from typing import Any, Callable, Iterator, IO, List, Optional, Text, TypeVar, Union

_T = TypeVar('_T')
_Decorator = Callable[[_T], _T]


def _posixify(name: Text) -> Text:
    ...


def safecall(func: _T) -> _T:
    ...


def make_str(value: Any) -> Text:
    ...


def make_default_short_help(help: Text, max_length: int = ...):
    ...


class LazyFile:
    name: Text
    mode: Text
    encoding: Optional[Text]
    errors: Text
    atomic: bool

    def __init__(
        self,
        filename: Text,
        mode: Text = ...,
        encoding: Optional[Text] = ...,
        errors: Text = ...,
        atomic: bool = ...
    ) -> None:
        ...

    def open(self) -> IO:
        ...

    def close(self) -> None:
        ...

    def close_intelligently(self) -> None:
        ...

    def __enter__(self) -> 'LazyFile':
        ...

    def __exit__(self, exc_type, exc_value, tb):
        ...

    def __iter__(self) -> Iterator:
        ...


class KeepOpenFile:
    _file: IO

    def __init__(self, file: IO) -> None:
        ...

    def __enter__(self) -> 'KeepOpenFile':
        ...

    def __exit__(self, exc_type, exc_value, tb):
        ...

    def __iter__(self) -> Iterator:
        ...


def echo(
    message: Optional[Union[bytes, Text]] = ...,
    file: Optional[IO] = ...,
    nl: bool = ...,
    err: bool = ...,
    color: Optional[bool] = ...,
) -> None:
    ...


def get_binary_stream(name: Text) -> IO[bytes]:
    ...


def get_text_stream(
    name: Text, encoding: Optional[Text] = ..., errors: Text = ...
) -> IO[Text]:
    ...


def open_file(
    filename: Text,
    mode: Text = ...,
    encoding: Optional[Text] = ...,
    errors: Text = ...,
    lazy: bool = ...,
    atomic: bool = ...
) -> Union[IO, LazyFile, KeepOpenFile]:
    ...


def get_os_args() -> List[Text]:
    ...


def format_filename(filename: Text, shorten: bool = ...) -> Text:
    ...


def get_app_dir(
    app_name: Text, roaming: bool = ..., force_posix: bool = ...
) -> Text:
    ...
