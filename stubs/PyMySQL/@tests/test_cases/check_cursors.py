from typing import Any
from typing_extensions import assert_type

from pymysql.cursors import Cursor, DictCursor, SSCursor, SSDictCursor


def check_fetch_results(cursor: Cursor, dictionary: DictCursor, streaming: SSCursor, stream_dictionary: SSDictCursor) -> None:
    # Mixin and streaming overrides must preserve both the row type and container.
    assert_type(cursor.fetchall(), tuple[tuple[Any, ...], ...] | list[tuple[Any, ...]])
    assert_type(dictionary.fetchall(), list[dict[str, Any]] | tuple[()])
    assert_type(dictionary.fetchmany(), list[dict[str, Any]] | tuple[()])
    assert_type(streaming.fetchmany(), list[tuple[Any, ...]] | tuple[()])
    assert_type(stream_dictionary.fetchmany(), list[dict[str, Any]] | tuple[()])
    assert_type(stream_dictionary.fetchall(), list[dict[str, Any]])
