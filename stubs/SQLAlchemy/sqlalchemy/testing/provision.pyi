from _typeshed import Incomplete, Unused
from collections.abc import Callable
from logging import Logger
from typing import Any, Generic, NoReturn, TypeVar
from typing_extensions import Self

from ..engine.interfaces import Connectable
from ..engine.url import URL
from ..testing.config import Config

_S = TypeVar("_S", bound=str)
_U = TypeVar("_U", bound=URL)
_F = TypeVar("_F", bound=Callable[..., str | URL | None])

log: Logger
FOLLOWER_IDENT: Incomplete | None

def create_follower_db(follower_ident) -> None: ...
def setup_config(db_url, options, file_config, follower_ident) -> Config: ...
def drop_follower_db(follower_ident) -> None: ...
def generate_db_urls(db_urls, extra_drivers) -> None: ...
def drop_all_schema_objects(cfg, eng) -> None: ...
def reap_dbs(idents_file) -> None: ...

class register(Generic[_F]):
    fns: dict[str, _F]
    @classmethod
    def init(cls, fn: _F) -> Self: ...
    def for_db(self, *dbnames: str) -> Callable[[_F], Self]: ...
    # Impossible to specify the args from the generic Callable in the current type system
    def __call__(self, cfg: str | URL, *arg: Any) -> str | URL | None: ...  # AnyOf[str | URL | None]

@register.init
def generate_driver_url(url: _U, driver: str, query_str: str) -> _U | None: ...
@register.init
def drop_all_schema_objects_pre_tables(cfg: Unused, eng: Unused) -> None: ...
@register.init
def drop_all_schema_objects_post_tables(cfg: Unused, eng: Unused) -> None: ...
@register.init
def create_db(cfg: Unused, eng: Connectable, ident: Unused) -> NoReturn: ...
@register.init
def drop_db(cfg: Unused, eng: Connectable, ident: Unused) -> NoReturn: ...
@register.init
def update_db_opts(db_url: Unused, db_opts: Unused) -> None: ...
@register.init
def post_configure_engine(url: Unused, engine: Unused, follower_ident: Unused) -> None: ...
@register.init
def follower_url_from_main(url: _U, ident: str) -> _U: ...
@register.init
def configure_follower(cfg: Unused, ident: Unused) -> None: ...
@register.init
def run_reap_dbs(url: Unused, ident: Unused) -> None: ...
@register.init
def temp_table_keyword_args(cfg: Unused, eng: Connectable) -> NoReturn: ...
@register.init
def prepare_for_drop_tables(config: Unused, connection: Unused) -> None: ...
@register.init
def stop_test_class_outside_fixtures(config: Unused, db: Unused, testcls: Unused) -> None: ...
@register.init  # type: ignore[type-var]  # False-positive, _S is bound to str
def get_temp_table_name(cfg: Unused, eng: Unused, base_name: _S) -> _S: ...
@register.init
def set_default_schema_on_connection(cfg, dbapi_connection: Unused, schema_name: Unused) -> NoReturn: ...
