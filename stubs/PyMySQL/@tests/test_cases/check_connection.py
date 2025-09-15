from pymysql.connections import Connection
from pymysql.cursors import Cursor
from typing_extensions import assert_type


class MyCursor(Cursor):
    pass


assert_type(Connection(), Connection[Cursor])
assert_type(Connection(cursorclass=Cursor), Connection[Cursor])
assert_type(Connection(cursorclass=MyCursor), Connection[MyCursor])

Connection(cursorclass=None)  # type: ignore
