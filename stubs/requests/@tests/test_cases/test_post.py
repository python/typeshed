from __future__ import annotations

from collections.abc import Iterable

import requests

# =================================================================================
# Tests for various different types being passed into the "data" parameter
# (These all return "Any", so there's not much value in using assert_type here.)
# (Just test that type checkers don't emit an error if it doesn't fail at runtime.)
# =================================================================================

# Arbitrary iterable
def gen() -> Iterable[bytes]:
    yield b"foo"
    yield b"bar"

requests.post("http://httpbin.org/anything", data=gen()).json()["data"]

# bytes
requests.post("http://httpbin.org/anything", data=b"foobar").json()["data"]

# str
requests.post("http://httpbin.org/anything", data="foobar").json()["data"]

# Files
requests.post("http://httpbin.org/anything", data=open("/tmp/foobar", "rb")).json()["data"]
requests.post("http://httpbin.org/anything", data=open("/tmp/foobar", "r")).json()["data"]

# Mappings
requests.post("http://httpbin.org/anything", data={b"foo": b"bar"}).json()["form"]
requests.post("http://httpbin.org/anything", data={"foo": "bar"}).json()["form"]

# mappings represented by an list/tuple of key-values pairs
requests.post("http://httpbin.org/anything", data=[(b"foo", b"bar")]).json()["form"]
requests.post("http://httpbin.org/anything", data=[("foo", "bar")]).json()["form"]
requests.post("http://httpbin.org/anything", data=((b"foo", b"bar"),)).json()["form"]
requests.post("http://httpbin.org/anything", data=(("foo", "bar"),)).json()["form"]
