from __future__ import annotations

import io
from _compression import DecompressReader as DecompressReader_other, _Reader as _Reader_other
from _typeshed import ReadableBuffer
from bz2 import BZ2Decompressor
from compression._common._streams import DecompressReader, _Decompressor, _Reader
from compression.zstd import ZstdDecompressor
from lzma import LZMADecompressor
from typing import cast
from typing_extensions import assert_type
from zlib import decompressobj

###
# Tests for DecompressReader/_Decompressor
###


class CustomDecompressor:
    def decompress(self, data: ReadableBuffer, max_length: int = -1) -> bytes:
        return b""

    @property
    def unused_data(self) -> bytes:
        return b""

    @property
    def eof(self) -> bool:
        return False

    @property
    def needs_input(self) -> bool:
        return False


def accept_decompressor(d: _Decompressor) -> None:
    d.decompress(b"random bytes", 0)
    assert_type(d.eof, bool)
    assert_type(d.unused_data, bytes)


# Test objects from compression._common._streams
fp = cast(_Reader, io.BytesIO(b"hello world"))
DecompressReader(fp, decompressobj)
DecompressReader(fp, BZ2Decompressor)
DecompressReader(fp, LZMADecompressor)
DecompressReader(fp, ZstdDecompressor)
DecompressReader(fp, CustomDecompressor)
accept_decompressor(decompressobj())
accept_decompressor(BZ2Decompressor())
accept_decompressor(LZMADecompressor())
accept_decompressor(ZstdDecompressor())
accept_decompressor(CustomDecompressor())

# Test objects from _compression
fp = cast(_Reader_other, io.BytesIO(b"hello world"))
DecompressReader_other(fp, decompressobj)
DecompressReader_other(fp, BZ2Decompressor)
DecompressReader_other(fp, LZMADecompressor)
DecompressReader_other(fp, ZstdDecompressor)
DecompressReader_other(fp, CustomDecompressor)
