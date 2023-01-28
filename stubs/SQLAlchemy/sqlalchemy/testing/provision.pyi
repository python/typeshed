from _typeshed import Incomplete, Self
from collections.abc import Callable
from logging import Logger
from typing import Generic, Protocol, TypeVar

from ..engine.url import URL
from ..testing.config import Config

log: Logger
FOLLOWER_IDENT: Incomplete | None

def create_follower_db(follower_ident) -> None: ...
def setup_config(db_url, options, file_config, follower_ident) -> Config: ...
def drop_follower_db(follower_ident) -> None: ...
def generate_db_urls(db_urls, extra_drivers) -> None: ...
def drop_all_schema_objects(cfg, eng) -> None: ...
def reap_dbs(idents_file) -> None: ...

###
# The methods below are decorated with the method register.init
# They dynamically become instances of register,
# wich is callable with their original parameters.
#
# While both mypy and pyright's validation work, Pylance is unable to
# show the parameters and return types.
#
# There is a workaround (define the method for Pylance, then reassign
# an instance of register to it for mypy, and add pyright+Flake8
# suppressions), but it is too hacky and relies on some unsupported quirks.
#
# Asking Pylance to add support for these generic callables might be preferable.
###

_F = TypeVar("_F", bound=Callable[..., str | URL | None])
_S = TypeVar("_S", bound=str)

class register(Generic[_F]):
    fns: dict[str, _F]
    @classmethod
    def init(cls: type[Self], fn: _F) -> Self: ...
    def for_db(self: Self, *dbnames: str) -> Callable[[_F], Self]: ...
    __call__: _F

class _generate_driver_url(Protocol):
    def __call__(self, url: URL, driver, query_str) -> URL | None: ...

generate_driver_url: register[_generate_driver_url]

class _drop_all_schema_objects_pre_tables(Protocol):
    def __call__(self, cfg, eng) -> None: ...

drop_all_schema_objects_pre_tables: register[_drop_all_schema_objects_pre_tables]

class _drop_all_schema_objects_post_tables(Protocol):
    def __call__(self, cfg, eng) -> None: ...

drop_all_schema_objects_post_tables: register[_drop_all_schema_objects_post_tables]

class _create_db(Protocol):
    def __call__(self, cfg, eng, ident) -> None: ...

create_db: register[_create_db]

class _drop_db(Protocol):
    def __call__(self, cfg, eng, ident) -> None: ...

drop_db: register[_drop_db]

class _update_db_opts(Protocol):
    def __call__(self, cfg, db_opts) -> None: ...

update_db_opts: register[_update_db_opts]

class _post_configure_engine(Protocol):
    def __call__(self, url: URL, engine, follower_ident) -> None: ...

post_configure_engine: register[_post_configure_engine]

class _follower_url_from_main(Protocol):
    def __call__(self, url: URL, ident) -> URL: ...

follower_url_from_main: register[_follower_url_from_main]

class _configure_follower(Protocol):
    def __call__(self, cfg, ident) -> None: ...

configure_follower: register[_configure_follower]

class _run_reap_dbs(Protocol):
    def __call__(self, url: URL, ident) -> None: ...

run_reap_dbs: register[_run_reap_dbs]

class _temp_table_keyword_args(Protocol):
    def __call__(self, cfg, eng) -> None: ...

temp_table_keyword_args: register[_temp_table_keyword_args]

class _prepare_for_drop_tables(Protocol):
    def __call__(self, config, connection) -> None: ...

prepare_for_drop_tables: register[_prepare_for_drop_tables]

class _stop_test_class_outside_fixtures(Protocol):
    def __call__(self, config, db, testcls) -> None: ...

stop_test_class_outside_fixtures: register[_stop_test_class_outside_fixtures]

class _get_temp_table_name(Protocol):
    def __call__(self, cfg, eng, base_name: _S) -> _S: ...

get_temp_table_name: register[_get_temp_table_name]  # type: ignore[type-var]  # _S is bound to string

class _set_default_schema_on_connection(Protocol):
    def __call__(self, cfg, dbapi_connection, schema_name) -> None: ...

set_default_schema_on_connection: register[_set_default_schema_on_connection]
