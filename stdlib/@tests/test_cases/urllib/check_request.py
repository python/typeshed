from __future__ import annotations

from _typeshed import ReadableBuffer, SupportsRead
from collections.abc import Iterable
from typing_extensions import assert_type
from urllib.request import Request, urlopen

# The type of `data` is inferred from the constructor argument.
req = Request("http://example.com", data=b"body")
assert_type(req, Request[bytes])
assert_type(req.data, bytes)
req.data.decode()
req.data = b"other"
req.data = [b"a", b"b"]  # type: ignore


def iterable_data(it: Iterable[bytes]) -> None:
    assert_type(Request("http://example.com", it).data, Iterable[bytes])


# Without `data`, any data type can be assigned later.
req2 = Request("http://example.com")
assert_type(req2.data, ReadableBuffer | SupportsRead[bytes] | Iterable[bytes] | None)
req2.data = b"body"
del req2.data

# A plain `Request` annotation means `Request[Any]`, so specialized requests
# are accepted by functions taking a plain `Request`.
urlopen(req)
