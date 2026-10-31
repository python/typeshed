from __future__ import annotations

from typing import Any
from typing_extensions import assert_type

from simplejson import JSONDecoder, JSONEncoder, dumps


class CustomEncoder(JSONEncoder):  # eventhough it does not have `extra_kw` arg.
    ...


# We are only testing `dumps` here, because they are all the same:
dumps([], extra_kw=True)  # type: ignore

# Ok:
assert_type(dumps([], cls=CustomEncoder, extra_kw=True), str)

decoder = JSONDecoder()
assert_type(decoder.scan_once("{}", 0), tuple[Any, int])
assert_type(decoder.parse_string('"hello"', 1), tuple[str, int])
assert_type(decoder.parse_array(("[]", 1), decoder.scan_once), tuple[Any, int])
assert_type(
    decoder.parse_object(
        ("{}", 1),
        decoder.encoding,
        decoder.strict,
        decoder.scan_once,
        decoder.object_hook,
        decoder.object_pairs_hook,
    ),
    tuple[Any, int],
)
