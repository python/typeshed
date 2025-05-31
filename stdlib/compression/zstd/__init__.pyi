import enum
from _typeshed import ReadableBuffer
from collections.abc import Iterable, Mapping
from compression.zstd._zstdfile import ZstdFile, open
from typing import Final, final

import _zstd
from _zstd import ZstdCompressor, ZstdDecompressor, ZstdDict, ZstdError, get_frame_size, zstd_version

__all__ = (
    # compression.zstd
    "COMPRESSION_LEVEL_DEFAULT",
    "compress",
    "CompressionParameter",
    "decompress",
    "DecompressionParameter",
    "finalize_dict",
    "get_frame_info",
    "Strategy",
    "train_dict",
    # compression.zstd._zstdfile
    "open",
    "ZstdFile",
    # _zstd
    "get_frame_size",
    "zstd_version",
    "zstd_version_info",
    "ZstdCompressor",
    "ZstdDecompressor",
    "ZstdDict",
    "ZstdError",
)

zstd_version_info: Final[tuple[int, int, int]]
COMPRESSION_LEVEL_DEFAULT: Final = _zstd.ZSTD_CLEVEL_DEFAULT

class FrameInfo:
    decompressed_size: int
    dictionary_id: int
    def __init__(self, decompressed_size: int, dictionary_id: int) -> None: ...

def get_frame_info(frame_buffer: ReadableBuffer) -> FrameInfo: ...
def train_dict(samples: Iterable[ReadableBuffer], dict_size: int) -> ZstdDict: ...
def finalize_dict(zstd_dict: ZstdDict, /, samples: Iterable[ReadableBuffer], dict_size: int, level: int) -> ZstdDict: ...
def compress(
    data: ReadableBuffer, level: int | None = None, options: Mapping[int, int] | None = None, zstd_dict: ZstdDict | None = None
) -> bytes: ...
def decompress(data: ReadableBuffer, zstd_dict: ZstdDict | None = None, options: Mapping[int, int] | None = None) -> bytes: ...
@final
class CompressionParameter(enum.IntEnum):
    compression_level: Final = _zstd.ZSTD_c_compressionLevel
    window_log: Final = _zstd.ZSTD_c_windowLog
    hash_log: Final = _zstd.ZSTD_c_hashLog
    chain_log: Final = _zstd.ZSTD_c_chainLog
    search_log: Final = _zstd.ZSTD_c_searchLog
    min_match: Final = _zstd.ZSTD_c_minMatch
    target_length: Final = _zstd.ZSTD_c_targetLength
    strategy: Final = _zstd.ZSTD_c_strategy
    enable_long_distance_matching: Final = _zstd.ZSTD_c_enableLongDistanceMatching
    ldm_hash_log: Final = _zstd.ZSTD_c_ldmHashLog
    ldm_min_match: Final = _zstd.ZSTD_c_ldmMinMatch
    ldm_bucket_size_log: Final = _zstd.ZSTD_c_ldmBucketSizeLog
    ldm_hash_rate_log: Final = _zstd.ZSTD_c_ldmHashRateLog
    content_size_flag: Final = _zstd.ZSTD_c_contentSizeFlag
    checksum_flag: Final = _zstd.ZSTD_c_checksumFlag
    dict_id_flag: Final = _zstd.ZSTD_c_dictIDFlag
    nb_workers: Final = _zstd.ZSTD_c_nbWorkers
    job_size: Final = _zstd.ZSTD_c_jobSize
    overlap_log: Final = _zstd.ZSTD_c_overlapLog
    def bounds(self) -> tuple[int, int]: ...

@final
class DecompressionParameter(enum.IntEnum):
    window_log_max: Final = _zstd.ZSTD_d_windowLogMax
    def bounds(self) -> tuple[int, int]: ...

@final
class Strategy(enum.IntEnum):
    fast: Final = _zstd.ZSTD_fast
    dfast: Final = _zstd.ZSTD_dfast
    greedy: Final = _zstd.ZSTD_greedy
    lazy: Final = _zstd.ZSTD_lazy
    lazy2: Final = _zstd.ZSTD_lazy2
    btlazy2: Final = _zstd.ZSTD_btlazy2
    btopt: Final = _zstd.ZSTD_btopt
    btultra: Final = _zstd.ZSTD_btultra
    btultra2: Final = _zstd.ZSTD_btultra2
