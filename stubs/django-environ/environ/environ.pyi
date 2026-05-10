from _typeshed import Incomplete, StrPath

# Use aliases to avoid name conflicts with Env methods.
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
from typing import IO, Any, ClassVar, SupportsIndex, TypeAlias, TypedDict, TypeVar, overload, type_check_only
from typing_extensions import Required, Unpack
from urllib.parse import ParseResult

from .compat import DJANGO_POSTGRES as DJANGO_POSTGRES, PYMEMCACHE_DRIVER as PYMEMCACHE_DRIVER, REDIS_DRIVER as REDIS_DRIVER
from .fileaware_mapping import FileAwareMapping

Openable: tuple[type, ...]
logger: Logger

class NoValue: ...

_T = TypeVar("_T")
_CastFunc: TypeAlias = Callable[[str], _T]
_SchemeValue: TypeAlias = _CastFunc[object] | tuple[_CastFunc[object], object]
_EmptyDict: TypeAlias = dict[object, object]  # stands for {}

@type_check_only
class _CastDict(TypedDict, total=False):
    key: _CastFunc[Any]
    value: _CastFunc[Any]
    # Key-specific value casts can make the value type depend on the input key.
    cast: dict[str, _CastFunc[Any]]

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
    OPTIONS: dict[str, Incomplete]

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
    OPTIONS: dict[str, Incomplete]

# https://github.com/django/channels
@type_check_only
class ChannelsConfig(TypedDict, total=False):
    BACKEND: Required[str]
    CONFIG: dict[str, Incomplete]

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
    KWARGS: dict[str, Incomplete]

@type_check_only
class ElasticsearchSearchConfig(SimpleSearchConfig, total=False):
    URL: Required[str]
    TIMEOUT: int
    KWARGS: dict[str, Incomplete]
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
    OPTIONS: dict[str, Incomplete]

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
        self, var: _str, cast: _CastFunc[_T] | None = None, default: _T | NoValue = ..., parse_default: _bool = False
    ) -> _T: ...
    @overload
    def __call__(
        self, var: _str, cast: _list[_CastFunc[_T]], default: _list[_T] | NoValue = ..., parse_default: _bool = False
    ) -> _list[_T]: ...
    @overload
    def __call__(
        self, var: _str, cast: _tuple[_CastFunc[_T], ...], default: _tuple[_T, ...] | NoValue = ..., parse_default: _bool = False
    ) -> _tuple[_T, ...]: ...
    @overload
    def __call__(
        self, var: _str, cast: _CastDict, default: _dict[Any, Any] | NoValue = ..., parse_default: _bool = False
    ) -> _dict[Any, Any]: ...
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
    @overload
    def str(self, var: _str, default: NoValue = ..., multiline: _bool = False) -> _str: ...
    @overload
    def str(self, var: _str, default: _T, multiline: _bool = False) -> _str | _T: ...
    @overload
    def bytes(self, var: _str, default: NoValue = ..., encoding: _str = "utf8") -> _bytes: ...
    @overload
    def bytes(self, var: _str, default: _T, encoding: _str = "utf8") -> _bytes | _T: ...
    @overload
    def bool(self, var: _str, default: NoValue = ...) -> _bool: ...
    @overload
    def bool(self, var: _str, default: _T) -> _bool | _T: ...
    @overload
    def int(self, var: _str, default: NoValue = ...) -> _int: ...
    @overload
    def int(self, var: _str, default: _T) -> _int | _T: ...
    @overload
    def float(self, var: _str, default: NoValue = ...) -> _float: ...
    @overload
    def float(self, var: _str, default: _T) -> _float | _T: ...
    @overload
    def json(self, var: _str, default: NoValue = ...) -> Any: ...
    @overload
    def json(self, var: _str, default: _T) -> _T: ...
    def list(self, var: _str, cast: _CastFunc[_T] | None = None, default: _list[_T] | NoValue = ...) -> _list[_T]: ...
    def tuple(
        self, var: _str, cast: _CastFunc[_T] | None = None, default: _tuple[_T, ...] | NoValue = ...
    ) -> _tuple[_T, ...]: ...
    @overload
    def dict(
        self, var: _str, cast: type[_dict[Any, Any]] = ..., default: _dict[_str, _str] | NoValue = ...
    ) -> _dict[_str, _str]: ...
    @overload
    def dict(self, var: _str, cast: _CastDict, default: _dict[Any, Any] | NoValue = ...) -> _dict[Any, Any]: ...
    @overload
    def dict(self, var: _str, cast: _CastFunc[_T], default: _T | NoValue = ...) -> _T: ...
    @overload
    def url(self, var: _str, default: NoValue = ...) -> ParseResult: ...
    @overload
    def url(self, var: _str, default: None) -> ParseResult | None: ...
    @overload
    def url(self, var: _str, default: _str) -> ParseResult: ...
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
        self, var: _str, cast: _CastFunc[_T] | None = None, default: _T | NoValue = ..., parse_default: _bool = False
    ) -> _T: ...
    @overload
    def get_value(
        self, var: _str, cast: _list[_CastFunc[_T]], default: _list[_T] | NoValue = ..., parse_default: _bool = False
    ) -> _list[_T]: ...
    @overload
    def get_value(
        self, var: _str, cast: _tuple[_CastFunc[_T], ...], default: _tuple[_T, ...] | NoValue = ..., parse_default: _bool = False
    ) -> _tuple[_T, ...]: ...
    @overload
    def get_value(
        self, var: _str, cast: _CastDict, default: _dict[Any, Any] | NoValue = ..., parse_default: _bool = False
    ) -> _dict[Any, Any]: ...
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
    def parse_value(cls, value: _str, cast: _CastFunc[_T]) -> _T: ...
    @classmethod
    @overload
    def parse_value(cls, value: _str, cast: _list[_CastFunc[_T]]) -> _list[_T]: ...
    @classmethod
    @overload
    def parse_value(cls, value: _str, cast: _tuple[_CastFunc[_T], ...]) -> _tuple[_T, ...]: ...
    @classmethod
    @overload
    def parse_value(cls, value: _str, cast: _CastDict) -> _dict[Any, Any]: ...
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
    def path(self, *paths: StrPath, **kwargs: Unpack[PathKwargs]) -> Path: ...
    # *args and **kwargs are passed to open().
    def file(self, name: str, *args: Any, **kwargs: Any) -> IO[Any]: ...
    @property
    def root(self) -> str: ...

    __root__: str

    def __init__(self, start: StrPath = "", *paths: StrPath, **kwargs: Unpack[PathKwargs]) -> None: ...
    def __call__(self, *paths: StrPath, **kwargs: Unpack[PathKwargs]) -> str: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __add__(self, other: object) -> Path: ...
    def __sub__(self, other: int | str) -> Path: ...
    def __invert__(self) -> Path: ...
    def __contains__(self, item: Path) -> bool: ...
    def __unicode__(self) -> str: ...
    @overload
    def __getitem__(self, key: SupportsIndex, /) -> str: ...
    @overload
    def __getitem__(self, key: slice, /) -> str: ...
    def __fspath__(self) -> str: ...
    def rfind(self, s: str, start: SupportsIndex | None = ..., end: SupportsIndex | None = ..., /) -> int: ...
    def find(self, s: str, start: SupportsIndex | None = ..., end: SupportsIndex | None = ..., /) -> int: ...
