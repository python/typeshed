from _typeshed import StrPath

# Use aliases to avoid name conflicts with Path methods
from builtins import (
    bool as _bool,
    bytes as _bytes,
    dict as _dict,
    float as _float,
    int as _int,
    list as _list,
    str as _str,
    tuple as _tuple,
)
from collections.abc import Callable, Mapping, MutableMapping
from logging import Logger
from typing import IO, Any, ClassVar, Generic, SupportsIndex, TypedDict, TypeVar, overload, type_check_only
from typing_extensions import Required, TypeAlias, Unpack
from urllib.parse import ParseResult

from .fileaware_mapping import FileAwareMapping

Openable: tuple[type, ...]
logger: Logger

class NoValue: ...

_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")
_Cast: TypeAlias = Callable[[str], _T1]
_SchemeValue: TypeAlias = _Cast[Any] | tuple[_Cast[Any], Any]
_EmptyDict: TypeAlias = dict[object, object]  # stands for {}

@type_check_only
class CastDict(TypedDict, Generic[_T1, _T2], total=False):
    key: _Cast[_T1]
    value: _Cast[_T2]
    cast: dict[str, _Cast[Any]]  # value cast by key

@type_check_only
class PathKwargs(TypedDict, total=False):
    required: bool
    is_file: bool

# https://docs.djangoproject.com/en/5.2/ref/settings/#std-setting-DATABASES
@type_check_only
class MemoryDbConfig(TypedDict):
    ENGINE: str
    NAME: str

@type_check_only
class DbConfig(MemoryDbConfig, total=False):
    USER: Required[str]
    PASSWORD: Required[str]
    HOST: Required[str]
    PORT: Required[int | str]
    # Additional base options read from queryParams
    CONN_MAX_AGE: int
    CONN_HEALTH_CHECKS: bool
    ATOMIC_REQUESTS: bool
    AUTOCOMMIT: bool
    DISABLE_SERVER_SIDE_CURSORS: bool
    # Remaining options read from queryParams
    OPTIONS: dict[str, Any]

@type_check_only
class EmailConfig(TypedDict, total=False):
    EMAIL_FILE_PATH: Required[str]
    EMAIL_HOST_USER: Required[str]
    EMAIL_HOST_PASSWORD: Required[str]
    EMAIL_HOST: Required[str]
    EMAIL_PORT: Required[int]
    EMAIL_BACKEND: Required[str]
    # Additional base options read from queryParams
    EMAIL_USE_TLS: bool
    EMAIL_USE_SSL: bool
    # Remaining options read from queryParams
    OPTIONS: dict[str, Any]

# https://github.com/django/channels
@type_check_only
class ChannelsConfig(TypedDict, total=False):
    BACKEND: Required[str]
    CONFIG: dict[str, Any]

# https://github.com/django-haystack/django-haystack
@type_check_only
class SimpleSearchConfig(TypedDict, total=False):
    ENGINE: Required[str]
    # Common search params
    EXCLUDED_INDEXES: list[str]
    INCLUDE_SPELLING: bool
    BATCH_SIZE: int

@type_check_only
class SolrSearchConfig(SimpleSearchConfig, total=False):
    URL: Required[str]
    TIMEOUT: int
    KWARGS: dict[str, Any]

@type_check_only
class ElasticsearchSearchConfig(SimpleSearchConfig, total=False):
    URL: Required[str]
    TIMEOUT: int
    KWARGS: dict[str, Any]
    INDEX_NAME: str

@type_check_only
class WhooshSearchConfig(SimpleSearchConfig, total=False):
    PATH: Required[str]
    STORAGE: str
    POST_LIMIT: int

@type_check_only
class XapianSearchConfig(SimpleSearchConfig, total=False):
    PATH: Required[str]
    FLAGS: int

# https://docs.djangoproject.com/en/5.2/ref/settings/#std-setting-CACHES
@type_check_only
class CacheConfig(TypedDict, total=False):
    BACKEND: Required[str]
    LOCATION: Required[str]
    # Additional base options read from queryParams
    KEY_FUNCTION: str
    KEY_PREFIX: str
    BINARY: str
    TIMEOUT: int
    VERSION: int
    # Remaining options read from queryParams
    OPTIONS: dict[str, Any]

class Env:
    ENVIRON: MutableMapping[_str, _str]
    NOTSET: ClassVar[NoValue]
    BOOLEAN_TRUE_STRINGS: ClassVar[_tuple[str, ...]]
    URL_CLASS: ClassVar[type[ParseResult]]
    POSTGRES_FAMILY: ClassVar[_list[_str]]
    DEFAULT_DATABASE_ENV: ClassVar[_str] = "DATABASE_URL"
    DB_SCHEMES: ClassVar[_dict[_str, _str]]
    DEFAULT_CACHE_ENV: ClassVar[_str] = "CACHE_URL"
    CACHE_SCHEMES: ClassVar[_dict[_str, _str]]
    DEFAULT_EMAIL_ENV: ClassVar[_str] = "EMAIL_URL"
    EMAIL_SCHEMES: ClassVar[_dict[_str, _str]]
    DEFAULT_SEARCH_ENV: ClassVar[_str] = "SEARCH_URL"
    SEARCH_SCHEMES: ClassVar[_dict[_str, _str]]
    ELASTICSEARCH_FAMILY: ClassVar[_list[_str]]
    CLOUDSQL: ClassVar[_str]
    DEFAULT_CHANNELS_ENV: ClassVar[_str] = "CHANNELS_URL"
    CHANNELS_SCHEMES: ClassVar[_dict[_str, _str]]
    smart_cast: _bool
    escape_proxy: _bool
    prefix: _str
    scheme: Mapping[_str, _SchemeValue]

    def __init__(self, **scheme: _SchemeValue) -> None: ...
    @overload
    def __call__(
        self, var: _str, cast: _Cast[_T1] | None = None, default: _T1 | NoValue = ..., parse_default: _bool = False
    ) -> _T1: ...
    @overload
    def __call__(
        self, var: _str, cast: _list[_Cast[_T1]], default: _list[_T1] | NoValue = ..., parse_default: _bool = False
    ) -> _list[_T1]: ...
    @overload
    def __call__(
        self, var: _str, cast: _tuple[_Cast[_T1]], default: _tuple[_T1] | NoValue = ..., parse_default: _bool = False
    ) -> _tuple[_T1]: ...
    @overload
    def __call__(
        self, var: _str, cast: CastDict[_T1, _T2], default: _dict[_T1, _T2] | NoValue = ..., parse_default: _bool = False
    ) -> _dict[_T1, _T2]: ...
    @overload
    # Any (subclass of) list/tuple/dict builtin types are valid for cast.
    def __call__(
        self, var: _str, cast: type[_list[Any]], default: _list[_str] | NoValue = ..., parse_default: _bool = False
    ) -> _list[_str]: ...
    @overload
    def __call__(
        self, var: _str, cast: type[_tuple[Any, ...]], default: _tuple[_str, ...] | NoValue = ..., parse_default: _bool = False
    ) -> _tuple[_str, ...]: ...
    @overload
    def __call__(
        self, var: _str, cast: type[_dict[Any, Any]], default: _dict[_str, _str] | NoValue = ..., parse_default: _bool = False
    ) -> _dict[_str, _str]: ...
    def __contains__(self, var: _str) -> _bool: ...
    def str(self, var: _str, default: _str | NoValue = ..., multiline: _bool = False) -> _str: ...
    def bytes(self, var: _str, default: _bytes | NoValue = ..., encoding: _str = "utf8") -> _bytes: ...
    def bool(self, var: _str, default: _bool | NoValue = ...) -> _bool: ...
    def int(self, var: _str, default: _int | NoValue = ...) -> _int: ...
    def float(self, var: _str, default: _float | NoValue = ...) -> _float: ...
    def json(self, var: _str, default: Any | NoValue = ...) -> Any: ...
    def list(self, var: _str, cast: _Cast[_T1] | None = None, default: _list[_T1] | NoValue = ...) -> _list[_T1]: ...
    def tuple(self, var: _str, cast: _Cast[_T1] | None = None, default: _tuple[_T1] | NoValue = ...) -> _tuple[_T1]: ...
    @overload
    def dict(self, var: _str, cast: None = ..., default: _dict[_str, Any] | NoValue = ...) -> _dict[_str, Any]: ...
    @overload
    def dict(self, var: _str, cast: _Cast[_T1], default: _dict[Any, _T1] | NoValue = ...) -> _dict[Any, _T1]: ...
    def url(self, var: _str, default: _str | NoValue = ...) -> _str: ...
    def db_url(
        self, var: _str = ..., default: _str | NoValue = ..., engine: _str | None = None
    ) -> MemoryDbConfig | DbConfig | _EmptyDict: ...

    db = db_url

    def cache_url(
        self, var: _str = ..., default: _str | NoValue = ..., backend: _str | None = None
    ) -> CacheConfig | _EmptyDict: ...

    cache = cache_url

    def email_url(self, var: _str = ..., default: _str | NoValue = ..., backend: _str | None = None) -> EmailConfig: ...

    email = email_url

    def search_url(
        self, var: _str = ..., default: _str | NoValue = ..., engine: _str | None = None
    ) -> SimpleSearchConfig | SolrSearchConfig | ElasticsearchSearchConfig | WhooshSearchConfig | XapianSearchConfig: ...
    def channels_url(self, var: _str = ..., default: _str | NoValue = ..., backend: _str | None = None) -> ChannelsConfig: ...

    channels = channels_url

    def path(self, var: _str, default: _str | NoValue = ..., **kwargs: Unpack[PathKwargs]) -> Path: ...
    @overload
    def get_value(
        self, var: _str, cast: _Cast[_T1] | None = None, default: _T1 | NoValue = ..., parse_default: _bool = False
    ) -> _T1: ...
    @overload
    def get_value(
        self, var: _str, cast: _list[_Cast[_T1]], default: _list[_T1] | NoValue = ..., parse_default: _bool = False
    ) -> _list[_T1]: ...
    @overload
    def get_value(
        self, var: _str, cast: _tuple[_Cast[_T1]], default: _tuple[_T1] | NoValue = ..., parse_default: _bool = False
    ) -> _tuple[_T1]: ...
    @overload
    def get_value(
        self, var: _str, cast: CastDict[_T1, _T2], default: _dict[_T1, _T2] | NoValue = ..., parse_default: _bool = False
    ) -> _dict[_T1, _T2]: ...
    @overload
    # Any (subclass of) list/tuple/dict builtin types are valid for cast.
    def get_value(
        self, var: _str, cast: type[_list[Any]], default: _list[_str] | NoValue = ..., parse_default: _bool = False
    ) -> _list[_str]: ...
    @overload
    def get_value(
        self, var: _str, cast: type[_tuple[Any, ...]], default: _tuple[_str, ...] | NoValue = ..., parse_default: _bool = False
    ) -> _tuple[_str, ...]: ...
    @overload
    def get_value(
        self, var: _str, cast: type[_dict[Any, Any]], default: _dict[_str, _str] | NoValue = ..., parse_default: _bool = False
    ) -> _dict[_str, _str]: ...
    @classmethod
    @overload
    def parse_value(cls, value: _str, cast: None) -> _str: ...
    @classmethod
    @overload
    def parse_value(cls, value: _str, cast: _Cast[_T1]) -> _T1: ...
    @classmethod
    @overload
    def parse_value(cls, value: _str, cast: _list[_Cast[_T1]]) -> _list[_T1]: ...
    @classmethod
    @overload
    def parse_value(cls, value: _str, cast: _tuple[_Cast[_T1], ...]) -> _tuple[_T1]: ...
    @classmethod
    @overload
    def parse_value(cls, value: _str, cast: CastDict[_T1, _T2]) -> _dict[_T1, _T2]: ...
    @classmethod
    @overload
    # Any (subclass of) list/tuple/dict builtin types are valid for cast.
    def parse_value(cls, value: _str, cast: type[_list[Any]]) -> _list[_str]: ...
    @classmethod
    @overload
    def parse_value(cls, value: _str, cast: type[_tuple[Any, ...]]) -> _tuple[_str, ...]: ...
    @classmethod
    @overload
    def parse_value(cls, value: _str, cast: type[_dict[Any, Any]]) -> _dict[_str, _str]: ...
    @classmethod
    def db_url_config(cls, url: _str | ParseResult, engine: _str | None = None) -> MemoryDbConfig | DbConfig | _EmptyDict: ...
    @classmethod
    def cache_url_config(cls, url: _str | ParseResult, backend: _str | None = None) -> CacheConfig | _EmptyDict: ...
    @classmethod
    def email_url_config(cls, url: _str | ParseResult, backend: _str | None = None) -> EmailConfig: ...
    @classmethod
    def channels_url_config(cls, url: _str | ParseResult, backend: _str | None = None) -> ChannelsConfig: ...
    @classmethod
    def search_url_config(
        cls, url: _str | ParseResult, engine: _str | None = None
    ) -> SimpleSearchConfig | SolrSearchConfig | ElasticsearchSearchConfig | WhooshSearchConfig | XapianSearchConfig: ...
    @classmethod
    def read_env(
        cls,
        env_file: StrPath | None = None,
        overwrite: _bool = False,
        parse_comments: _bool = False,
        encoding: _str = "utf8",
        **overrides: _dict[_str, _str],
    ) -> None: ...

class FileAwareEnv(Env):
    ENVIRON: FileAwareMapping

class Path:
    def path(self, *paths: str, **kwargs: Unpack[PathKwargs]) -> Path: ...
    def file(self, name: str, *args, **kwargs) -> IO[str]: ...
    @property
    def root(self) -> str: ...

    __root__: str

    def __init__(self, start: str = "", *paths: str, **kwargs: Unpack[PathKwargs]) -> None: ...
    def __call__(self, *paths: str, **kwargs: Unpack[PathKwargs]) -> str: ...
    def __eq__(self, other: object | Path) -> bool: ...
    def __ne__(self, other: object | Path) -> bool: ...
    def __add__(self, other: object | Path) -> Path: ...
    def __sub__(self, other: int | str) -> Path: ...
    def __invert__(self) -> Path: ...
    def __contains__(self, item: Path) -> bool: ...
    def __unicode__(self) -> str: ...
    @overload
    def __getitem__(self, key: SupportsIndex, /) -> str: ...
    @overload
    def __getitem__(self, key: slice, /) -> str: ...
    def __fspath__(self) -> str: ...
    def rfind(self, s: str, sub: str, start: int = 0, end: int = ...) -> int: ...
    def find(self, s: str, sub: str, start: int = 0, end: int = ...) -> int: ...
