import typing as t
from collections.abc import Generator
from typing_extensions import TypeAlias

def b2u(string: bytes | str) -> str: ...
def u2b(string: str | bytes) -> bytes: ...

_Quotes: TypeAlias = t.Literal["'", '"']  # NOQA: Y020
_ContextType: TypeAlias = t.Literal["ARG", "ENV", "LABEL"]  # NOQA: Y020

class WordSplitter:
    SQUOTE: _Quotes
    DQUOTE: _Quotes
    stream: t.IO[str]
    args: t.Mapping[str, str]
    envs: t.Mapping[str, str]
    quotes: _Quotes
    escaped: bool
    def __init__(self, s: str, args: t.Mapping[str, str] | None = ..., envs: t.Mapping[str, str] | None = ...) -> None: ...
    def dequote(self) -> str: ...
    def split(self, maxsplit: int | None = ..., dequote: bool = ...) -> Generator[str | None, None, None]: ...

def extract_key_values(env_replace: bool, args: t.Mapping[str, str], envs: t.Mapping[str, str], instruction_value: str): ...
def get_key_val_dictionary(
    instruction_value, env_replace: bool = ..., args: t.Mapping[str, str] | None = ..., envs: t.Mapping[str, str] | None = ...
): ...

class Context:
    args: t.Mapping[str, str]
    envs: t.Mapping[str, str]
    labels: t.Mapping[str, str]
    line_args: t.Mapping[str, str]
    line_envs: t.Mapping[str, str]
    line_labels: t.Mapping[str, str]
    def __init__(
        self,
        args: t.Mapping[str, str] | None = ...,
        envs: t.Mapping[str, str] | None = ...,
        labels: t.Mapping[str, str] | None = ...,
        line_args: t.Mapping[str, str] | None = ...,
        line_envs: t.Mapping[str, str] | None = ...,
        line_labels: t.Mapping[str, str] | None = ...,
    ) -> None: ...
    def set_line_value(self, context_type: _ContextType, value: t.Mapping[str, str]) -> None: ...
    def get_line_value(self, context_type: _ContextType) -> t.Mapping[str, str]: ...
    def get_values(self, context_type: _ContextType) -> t.Mapping[str, str]: ...
