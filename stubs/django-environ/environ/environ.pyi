from _typeshed import StrPath
from collections.abc import Callable, Mapping, MutableMapping
from logging import Logger
from typing import IO, Any, ClassVar, SupportsIndex, TypedDict, TypeVar, overload, type_check_only
from typing_extensions import Required, TypeAlias, Unpack
from urllib.parse import ParseResult

from .fileaware_mapping import FileAwareMapping

Openable: tuple[type, ...]
logger: Logger

class NoValue: ...

# Some type aliases to make our life easier
_Str = str
_Bytes = bytes
_Bool = bool
_Int = int
_Float = float
_List = list
_Tuple = tuple
_Dict = dict

_T = TypeVar("_T")
_Cast: TypeAlias = Callable[[_Str], _T]
_SchemeValue: TypeAlias = _Cast[Any] | tuple[_Cast[Any], Any]
_BooleanTrueStrings: TypeAlias = tuple[str, ...]

_EmptyDict: TypeAlias = dict[object, object]  # stands for {}

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
    ENVIRON: MutableMapping[_Str, _Str]
    NOTSET: ClassVar[NoValue]
    BOOLEAN_TRUE_STRINGS: ClassVar[_BooleanTrueStrings]
    URL_CLASS: ClassVar[type[ParseResult]]
    POSTGRES_FAMILY: ClassVar[_List[_Str]]
    DEFAULT_DATABASE_ENV: ClassVar[_Str] = "DATABASE_URL"
    DB_SCHEMES: ClassVar[_Dict[_Str, _Str]]
    DEFAULT_CACHE_ENV: ClassVar[_Str] = "CACHE_URL"
    CACHE_SCHEMES: ClassVar[_Dict[_Str, _Str]]
    DEFAULT_EMAIL_ENV: ClassVar[_Str] = "EMAIL_URL"
    EMAIL_SCHEMES: ClassVar[_Dict[_Str, _Str]]
    DEFAULT_SEARCH_ENV: ClassVar[_Str] = "SEARCH_URL"
    SEARCH_SCHEMES: ClassVar[_Dict[_Str, _Str]]
    ELASTICSEARCH_FAMILY: ClassVar[_List[_Str]]
    CLOUDSQL: ClassVar[_Str]
    DEFAULT_CHANNELS_ENV: ClassVar[_Str] = "CHANNELS_URL"
    CHANNELS_SCHEMES: ClassVar[_Dict[_Str, _Str]]
    smart_cast: _Bool
    escape_proxy: _Bool
    prefix: _Str
    scheme: Mapping[_Str, _SchemeValue]

    def __init__(self, **scheme: _SchemeValue) -> None: ...
    def __call__(
        self, var: _Str, cast: _Cast[_T] | None = None, default: _T | NoValue = ..., parse_default: _Bool = False
    ) -> _T: ...
    def __contains__(self, var: _Str) -> _Bool: ...
    def str(self, var: _Str, default: _Str | NoValue = ..., multiline: _Bool = False) -> _Str: ...
    def bytes(self, var: _Str, default: _Bytes | NoValue = ..., encoding: _Str = "utf8") -> _Bytes: ...
    def bool(self, var: _Str, default: _Bool | NoValue = ...) -> _Bool: ...
    def int(self, var: _Str, default: _Int | NoValue = ...) -> _Int: ...
    def float(self, var: _Str, default: _Float | NoValue = ...) -> _Float: ...
    def json(self, var: _Str, default: Any | NoValue = ...) -> Any: ...
    def list(self, var: _Str, cast: _Cast[_List] | None = None, default: _List | NoValue = ...) -> _List: ...
    def tuple(self, var: _Str, cast: _Cast[_Tuple] | None = None, default: _Tuple | NoValue = ...) -> _Tuple: ...
    def dict(self, var: _Str, cast: _Cast[_Dict] | None = ..., default: _Dict | NoValue = ...) -> _Dict: ...
    def url(self, var: _Str, default: _Str | NoValue = ...) -> _Str: ...
    def db_url(
        self, var: _Str = ..., default: _Str | NoValue = ..., engine: _Str | None = None
    ) -> MemoryDbConfig | DbConfig | _EmptyDict: ...

    db = db_url

    def cache_url(
        self, var: _Str = ..., default: _Str | NoValue = ..., backend: _Str | None = None
    ) -> CacheConfig | _EmptyDict: ...

    cache = cache_url

    def email_url(self, var: _Str = ..., default: _Str | NoValue = ..., backend: _Str | None = None) -> EmailConfig: ...

    email = email_url

    def search_url(
        self, var: _Str = ..., default: _Str | NoValue = ..., engine: _Str | None = None
    ) -> SimpleSearchConfig | SolrSearchConfig | ElasticsearchSearchConfig | WhooshSearchConfig | XapianSearchConfig: ...
    def channels_url(self, var: _Str = ..., default: _Str | NoValue = ..., backend: _Str | None = None) -> ChannelsConfig: ...

    channels = channels_url

    def path(self, var: _Str, default: _Str | NoValue = ..., **kwargs: Unpack[PathKwargs]) -> Path: ...
    def get_value(
        self, var: _Str, cast: _Cast[_T] | None = None, default: _T | NoValue = ..., parse_default: _Bool = False
    ) -> _T: ...
    @classmethod
    def parse_value(cls, value: _Str, cast: _Cast[_T]) -> _T: ...
    @classmethod
    def db_url_config(cls, url: _Str | ParseResult, engine: _Str | None = None) -> _Dict: ...
    @classmethod
    def cache_url_config(cls, url: _Str | ParseResult, backend: _Str | None = None) -> _Dict: ...
    @classmethod
    def email_url_config(cls, url: _Str | ParseResult, backend: _Str | None = None) -> _Dict: ...
    @classmethod
    def channels_url_config(cls, url: _Str | ParseResult, backend: _Str | None = None) -> _Dict: ...
    @classmethod
    def search_url_config(cls, url: _Str | ParseResult, engine: _Str | None = None) -> _Dict: ...
    @classmethod
    def read_env(
        cls,
        env_file: StrPath | None = None,
        overwrite: _Bool = False,
        parse_comments: _Bool = False,
        encoding: _Str = "utf8",
        **overrides: _Dict[_Str, _Str],
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
