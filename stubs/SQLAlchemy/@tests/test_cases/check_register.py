from sqlalchemy.engine.base import Connection
from sqlalchemy.engine.interfaces import Connectable
from sqlalchemy.engine.url import URL
from sqlalchemy.testing.provision import (
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

url: URL
engine: Connectable
connection: Connection

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
