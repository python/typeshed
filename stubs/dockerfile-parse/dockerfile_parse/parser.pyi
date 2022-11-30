import logging
import typing as t
from contextlib import contextmanager

logger: logging.Logger

class KeyValues(dict[str, str]):
    parser_attr: str
    parser: DockerfileParser
    def __init__(self, key_values: dict[str, str], parser: DockerfileParser) -> None: ...
    def __delitem__(self, key: str) -> None: ...
    def __setitem__(self, key: str, value: str) -> None: ...
    def __eq__(self, other) -> bool: ...
    def __hash__(self) -> int: ...  # type: ignore

class Labels(KeyValues):
    parser_attr: str

class Envs(KeyValues):
    parser_attr: str

class Args(KeyValues):
    parser_attr: str

class DockerfileParser:
    fileobj: t.IO[str]
    dockerfile_path: str | None
    cache_content: bool
    cached_content: str
    env_replace: bool
    parent_env: t.Mapping[str, str]
    build_args: t.Mapping[str, str]
    def __init__(
        self,
        path: str | None = ...,
        cache_content: bool = ...,
        env_replace: bool = ...,
        parent_env: t.Mapping[str, str] | None = ...,
        fileobj: t.IO[str] | None = ...,
        build_args: t.Mapping[str, str] | None = ...,
    ) -> None: ...
    @contextmanager
    def _open_dockerfile(self, mode: str) -> t.IO: ...
    lines: t.Sequence[str]
    content: str
    @property
    def structure(self) -> list[dict[str, t.Any]]: ...
    @property
    def json(self) -> str: ...
    parent_images: t.Sequence[str]
    @property
    def is_multistage(self) -> bool: ...
    baseimage: str
    cmd: str
    labels: t.Mapping[str, str]
    envs: t.Mapping[str, str]
    args: t.Mapping[str, str]
    def add_lines(
        self, *lines: list[str], all_stages: bool | None = ..., at_start: bool | None = ..., skip_scratch: bool | None = ...
    ) -> None: ...
    def add_lines_at(
        self, anchor: str | int | dict[str, int], *lines: list[str], replace: bool | None = ..., after: bool | None = ...
    ) -> None: ...
    @property
    def context_structure(self) -> list[str]: ...

def image_from(from_value: str) -> tuple[str, str | None]: ...
