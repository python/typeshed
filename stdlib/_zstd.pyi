from _typeshed import ReadableBuffer
from compression.zstd import _OptionsCompress, _OptionsDecompress
from typing import Any, Final, Literal, final
from typing_extensions import Self

ZSTD_CLEVEL_DEFAULT: Final[int]
ZSTD_DStreamOutSize: Final[int]
ZSTD_btlazy2: Final[int]
ZSTD_btopt: Final[int]
ZSTD_btultra: Final[int]
ZSTD_btultra2: Final[int]
ZSTD_c_chainLog: Final[int]
ZSTD_c_checksumFlag: Final[int]
ZSTD_c_compressionLevel: Final[int]
ZSTD_c_contentSizeFlag: Final[int]
ZSTD_c_dictIDFlag: Final[int]
ZSTD_c_enableLongDistanceMatching: Final[int]
ZSTD_c_hashLog: Final[int]
ZSTD_c_jobSize: Final[int]
ZSTD_c_ldmBucketSizeLog: Final[int]
ZSTD_c_ldmHashLog: Final[int]
ZSTD_c_ldmHashRateLog: Final[int]
ZSTD_c_ldmMinMatch: Final[int]
ZSTD_c_minMatch: Final[int]
ZSTD_c_nbWorkers: Final[int]
ZSTD_c_overlapLog: Final[int]
ZSTD_c_searchLog: Final[int]
ZSTD_c_strategy: Final[int]
ZSTD_c_targetLength: Final[int]
ZSTD_c_windowLog: Final[int]
ZSTD_d_windowLogMax: Final[int]
ZSTD_dfast: Final[int]
ZSTD_fast: Final[int]
ZSTD_greedy: Final[int]
ZSTD_lazy: Final[int]
ZSTD_lazy2: Final[int]

@final
class ZstdCompressor:
    CONTINUE: Final = 0
    FLUSH_BLOCK: Final = 1
    FLUSH_FRAME: Final = 2
    def __init__(
        self, level: int | None = ..., options: _OptionsCompress | None = ..., zstd_dict: ZstdDict | None = ...
    ) -> None: ...
    def compress(self, /, data: ReadableBuffer, mode: Literal[0, 1, 2] = ...) -> bytes: ...
    def flush(self, /, mode: Literal[1, 2] = ...) -> bytes: ...
    @property
    def last_mode(self) -> Literal[0, 1, 2]: ...

@final
class ZstdDecompressor:
    def __init__(self, zstd_dict: ZstdDict | None = ..., options: _OptionsDecompress | None = ...) -> None: ...
    def decompress(self, /, data: ReadableBuffer, max_length: int = ...) -> bytes: ...
    @property
    def eof(self) -> bool: ...
    @property
    def needs_input(self) -> bool: ...
    @property
    def unused_data(self) -> bytes: ...

@final
class ZstdDict:
    def __init__(self, dict_content: bytes, /, *, is_raw: bool = ...) -> None: ...
    def __len__(self, /) -> int: ...
    @property
    def as_digested_dict(self) -> tuple[Self, int]: ...
    @property
    def as_prefix(self) -> tuple[Self, int]: ...
    @property
    def as_undigested_dict(self) -> tuple[Self, int]: ...
    @property
    def dict_content(self) -> bytes: ...
    @property
    def dict_id(self) -> int: ...

class ZstdError(Exception): ...

def finalize_dict(
    custom_dict_bytes: bytes, samples_bytes: bytes, samples_sizes: tuple[int, ...], dict_size: int, compression_level: int, /
) -> bytes: ...
def get_frame_info(frame_buffer: ReadableBuffer) -> tuple[int, int]: ...
def get_frame_size(frame_buffer: ReadableBuffer) -> int: ...
def get_param_bounds(parameter: int, is_compress: bool) -> tuple[int, int]: ...
def set_parameter_types(c_parameter_type: type[Any], d_parameter_type: type[Any]) -> None: ...
def train_dict(samples_bytes: bytes, samples_sizes: tuple[int, ...], dict_size: int, /) -> bytes: ...

zstd_version: Final[str]
zstd_version_number: Final[int]
