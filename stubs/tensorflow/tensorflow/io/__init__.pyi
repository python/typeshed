from _typeshed import Incomplete
from collections.abc import Iterable, Mapping
from types import TracebackType
from typing import NamedTuple
from typing_extensions import Literal, Self, TypeAlias

from tensorflow import _DTypeLike, _ShapeLike, _TensorCompatible
from tensorflow._aliases import TensorLike
from tensorflow.io import gfile as gfile

_FeatureSpecs: TypeAlias = Mapping[str, FixedLenFeature | FixedLenSequenceFeature | VarLenFeature | RaggedFeature | SparseFeature]

_CompressionTypes: TypeAlias = Literal["ZLIB", "GZIP", "", 0, 1, 2] | None
_CompressionLevels: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] | None
_MemoryLevels: TypeAlias = Literal[1, 2, 3, 4, 5, 6, 7, 8, 9] | None

class TFRecordOptions:
    compression_type: _CompressionTypes | TFRecordOptions
    flush_mode: int | None  # The exact values allowed comes from zlib
    input_buffer_size: int | None
    output_buffer_size: int | None
    window_bits: int | None
    compression_level: _CompressionLevels
    compression_method: str | None
    mem_level: _MemoryLevels
    compression_strategy: int | None  # The exact values allowed comes from zlib

    def __init__(
        self,
        compression_type: _CompressionTypes | TFRecordOptions = None,
        flush_mode: int | None = None,
        input_buffer_size: int | None = None,
        output_buffer_size: int | None = None,
        window_bits: int | None = None,
        compression_level: _CompressionLevels = None,
        compression_method: str | None = None,
        mem_level: _MemoryLevels = None,
        compression_strategy: int | None = None,
    ) -> None: ...
    @classmethod
    def get_compression_type_string(cls, options: _CompressionTypes | TFRecordOptions) -> str: ...

class TFRecordWriter:
    def __init__(self, path: str, options: _CompressionTypes | TFRecordOptions | None = None) -> None: ...
    def write(self, record: bytes) -> None: ...
    def flush(self) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...

class FixedLenFeature(NamedTuple):
    shape: _ShapeLike
    dtype: _DTypeLike
    default_value: _TensorCompatible | None = None

class FixedLenSequenceFeature(NamedTuple):
    shape: _ShapeLike
    dtype: _DTypeLike
    allow_missing: bool = False
    default_value: _TensorCompatible | None = None

class VarLenFeature(NamedTuple):
    dtype: _DTypeLike

class SparseFeature(NamedTuple):
    index_key: str | list[str]
    value_key: str
    dtype: _DTypeLike
    size: int | list[int]
    already_sorted: bool = False

class RaggedFeature(NamedTuple):
    class RowSplits(NamedTuple):
        key: str

    class RowLengths(NamedTuple):
        key: str

    class RowStarts(NamedTuple):
        key: str

    class RowLimits(NamedTuple):
        key: str

    class ValueRowIds(NamedTuple):
        key: str

    class UniformRowLength(NamedTuple):
        length: int
    dtype: _DTypeLike
    value_key: str | None = None
    partitions: tuple[RowSplits | RowLengths | RowStarts | RowLimits | ValueRowIds | UniformRowLength, ...] = ()
    row_splits_dtype: _DTypeLike = ...
    validate: bool = False

def parse_example(
    serialized: _TensorCompatible, features: _FeatureSpecs, example_names: Iterable[str] | None = None, name: str | None = None
) -> dict[str, TensorLike]: ...
def __getattr__(name: str) -> Incomplete: ...
