"""Check that typing for the Macaroon object matches expected values.

Based on the values passed in with pymacaroons's tests:
https://github.com/ecordell/pymacaroons/tree/v0.13.0/tests
"""
from typing import Union
from typing_extensions import assert_type

from pymacaroons import MACAROON_V1, MACAROON_V2, Macaroon

# key_id, loc, and key can each be an ASCII string or ASCII bytes
macaroons = [
    Macaroon("str_loc", "str_id", "str_key", version=MACAROON_V1),
    Macaroon("str_loc", "str_id", b"bytes_key", version=MACAROON_V1),
    Macaroon("str_loc", b"bytes_id", "str_key", version=MACAROON_V1),
    Macaroon("str_loc", b"bytes_id", b"bytes_key", version=MACAROON_V1),
    Macaroon(b"bytes_loc", "str_id", "str_key", version=MACAROON_V1),
    Macaroon(b"bytes_loc", "str_id", b"bytes_key", version=MACAROON_V1),
    Macaroon(b"bytes_loc", b"bytes_id", "str_key", version=MACAROON_V1),
    Macaroon(b"bytes_loc", b"bytes_id", b"bytes_key", version=MACAROON_V1),
    Macaroon("str_loc", "str_id", "str_key", version=MACAROON_V2),
    Macaroon("str_loc", "str_id", b"bytes_key", version=MACAROON_V2),
    Macaroon("str_loc", b"bytes_id", "str_key", version=MACAROON_V2),
    Macaroon("str_loc", b"bytes_id", b"bytes_key", version=MACAROON_V2),
    Macaroon(b"bytes_loc", "str_id", "str_key", version=MACAROON_V2),
    Macaroon(b"bytes_loc", "str_id", b"bytes_key", version=MACAROON_V2),
    Macaroon(b"bytes_loc", b"bytes_id", "str_key", version=MACAROON_V2),
    Macaroon(b"bytes_loc", b"bytes_id", b"bytes_key", version=MACAROON_V2),
]

for macaroon in macaroons:
    assert_type(macaroon.serialize(), str)
    assert_type(macaroon.location, str)
    assert_type(macaroon.version, int)
    assert_type(macaroon.identifier, Union[str, bytes])
    assert_type(macaroon.identifier_bytes, bytes)
    assert_type(macaroon.signature, str)
    assert_type(macaroon.copy(), Macaroon)
