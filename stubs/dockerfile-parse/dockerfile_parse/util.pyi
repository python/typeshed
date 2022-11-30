import typing as t
from collections.abc import Generator
from io import StringIO
from typing_extensions import Literal, TypeAlias

def b2u(string: bytes | str) -> str: ...
def u2b(string: str | bytes) -> bytes: ...

_Quotes: TypeAlias = Literal["'", '"']
_ContextType: TypeAlias = Literal["ARG", "ENV", "LABEL"]

class WordSplitter:
    SQUOTE: t.ClassVar[_Quotes]
    DQUOTE: t.ClassVar[_Quotes]
    stream: StringIO
    args: t.Mapping[str, str] | None
    envs: t.Mapping[str, str] | None
    quotes: _Quotes | None
    escaped: bool
    def __init__(self, s: str, args: t.Mapping[str, str] | None = ..., envs: t.Mapping[str, str] | None = ...) -> None: ...
    def dequote(self) -> str: ...
    def split(self, maxsplit: int | None = ..., dequote: bool = ...) -> Generator[str | None, None, None]: ...

def extract_key_values(env_replace: bool, args: t.Mapping[str, str], envs: t.Mapping[str, str], instruction_value: str): ...
def get_key_val_dictionary(
    instruction_value, env_replace: bool = ..., args: t.Mapping[str, str] | None = ..., envs: t.Mapping[str, str] | None = ...
): ...

class Context:
    args: t.MutableMapping[str, str]
    envs: t.MutableMapping[str, str]
    labels: t.MutableMapping[str, str]
    line_args: t.Mapping[str, str]
    line_envs: t.Mapping[str, str]
    line_labels: t.Mapping[str, str]
    def __init__(
        self,
        args: t.MutableMapping[str, str] | None = ...,
        envs: t.MutableMapping[str, str] | None = ...,
        labels: t.MutableMapping[str, str] | None = ...,
        line_args: t.Mapping[str, str] | None = ...,
        line_envs: t.Mapping[str, str] | None = ...,
        line_labels: t.Mapping[str, str] | None = ...,
    ) -> None: ...
    def set_line_value(self, context_type: _ContextType, value: t.Mapping[str, str]) -> None: ...
    def get_line_value(self, context_type: _ContextType) -> t.Mapping[str, str]: ...
    def get_values(self, context_type: _ContextType) -> t.Mapping[str, str]: ...
