from __future__ import annotations

import _hashlib
import hashlib
import sys
from _hashlib import HASH, HASHXOF
from io import BytesIO
from typing_extensions import assert_type


def check_new(name: str) -> None:
    for shake in (
        hashlib.new("shake_128"),
        hashlib.new("shake_256"),
        hashlib.new("SHAKE-128", b"data", usedforsecurity=False),
        hashlib.new("SHAKE-256"),
    ):
        assert_type(shake, HASHXOF)
        assert_type(shake.copy(), HASHXOF)
        assert_type(shake.digest(16), bytes)
        assert_type(shake.hexdigest(length=16), str)
        shake.digest()  # type: ignore
        shake.hexdigest()  # type: ignore

    fixed = hashlib.new("sha256")
    assert_type(fixed, HASH)
    assert_type(fixed.digest(), bytes)
    fixed.digest(16)  # type: ignore

    dynamic = hashlib.new(name)
    assert_type(dynamic.digest(), bytes)
    assert_type(dynamic.digest(16), bytes)
    assert_type(dynamic.copy().hexdigest(length=16), str)
    dynamic.digest("16")  # type: ignore

    assert_type(_hashlib.new("shake_128", string=b"data").digest(16), bytes)
    assert_type(_hashlib.new("SHAKE-256").hexdigest(16), str)
    assert_type(_hashlib.new("MD5"), HASH)
    assert_type(_hashlib.new(name).hexdigest(16), str)
    if sys.version_info >= (3, 13):
        assert_type(_hashlib.new("shake_256", data=b"data").copy(), HASHXOF)

    if sys.version_info >= (3, 11):
        hashlib.file_digest(BytesIO(b"data"), lambda: hashlib.new("sha256"))
