from __future__ import annotations

from collections import Callable
from typing import NoReturn, Optional, Union
from typing_extensions import assert_type

from sqlalchemy.engine.base import Connection
from sqlalchemy.engine.interfaces import Connectable
from sqlalchemy.engine.url import URL
from sqlalchemy.testing.config import Config
from sqlalchemy.testing.provision import (
    _S,
    _U,
    configure_follower,
    create_db,
    drop_all_schema_objects_post_tables,
    drop_all_schema_objects_pre_tables,
    drop_db,
    follower_url_from_main,
    generate_driver_url,
    get_temp_table_name,
    post_configure_engine,
    prepare_for_drop_tables,
    register,
    run_reap_dbs,
    set_default_schema_on_connection,
    stop_test_class_outside_fixtures,
    temp_table_keyword_args,
    update_db_opts,
)

config: Config
url: URL
engine: Connectable
connection: Connection

# # Expression is of type "register[Callable[[object, object], None]]", not "register[Callable[[object, object], None]]"  [assert-type]

# Testing that the functions are actually all instances of "register"
assert_type(generate_driver_url, register[Callable[[_U, str, str], Optional[_U]]])
assert_type(drop_all_schema_objects_pre_tables, register[Callable[[object, object], None]])
assert_type(drop_all_schema_objects_post_tables, register[Callable[[object, object], None]])
assert_type(create_db, register[Callable[[object, Connectable, object], NoReturn]])
assert_type(drop_db, register[Callable[[object, Connectable, object], NoReturn]])
assert_type(update_db_opts, register)
assert_type(post_configure_engine, register)
assert_type(follower_url_from_main, register)
assert_type(configure_follower, register)
assert_type(run_reap_dbs, register)
assert_type(temp_table_keyword_args, register)
assert_type(prepare_for_drop_tables, register)
assert_type(stop_test_class_outside_fixtures, register)
assert_type(get_temp_table_name, register)
assert_type(set_default_schema_on_connection, register)

# Because it's impossible to define register.__call__ return type through the use of a decorator,
# we can't use assert_type to test that teh right type would be returned, (it always expects Union[str, URL, None])

assert_type(generate_driver_url(url, ""), Optional[URL])  # type: ignore[assert-type]
assert_type(drop_all_schema_objects_pre_tables(url, engine), None)
assert_type(drop_all_schema_objects_post_tables(url, engine), None)
assert_type(create_db(url, engine, ""), NoReturn)
assert_type(drop_db(url, engine, ""), NoReturn)
assert_type(update_db_opts(url, {}), None)
assert_type(post_configure_engine(url, engine, ""), None)
assert_type(follower_url_from_main(url, ""), URL)
assert_type(configure_follower(url, ""), None)
assert_type(run_reap_dbs(url, ""), None)
assert_type(temp_table_keyword_args(url, engine), NoReturn)
assert_type(prepare_for_drop_tables(url, connection), None)
assert_type(stop_test_class_outside_fixtures(url, connection, type), None)
assert_type(get_temp_table_name(url, engine, ""), str)
assert_type(set_default_schema_on_connection(url, connection, ""), NoReturn)

# The decorator changes the first parameter to "cfg: str | URL"
@register.init
def no_args(foo: int) -> None:
    pass


no_args(cfg=url)
generate_driver_url(url, "")
drop_all_schema_objects_pre_tables(url, engine)
drop_all_schema_objects_post_tables(url, engine)
create_db(url, engine, "")
drop_db(url, engine, "")
update_db_opts(url, {})
post_configure_engine(url, engine, "")
follower_url_from_main(url, "")
configure_follower(url, "")
run_reap_dbs(url, "")
temp_table_keyword_args(url, engine)
prepare_for_drop_tables(url, connection)
stop_test_class_outside_fixtures(url, connection, type)
get_temp_table_name(url, engine, "")
set_default_schema_on_connection(url, connection, "")
