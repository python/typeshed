# The types here are all undocumented, but all feature columns are return types of the
# public functions in tf.feature_column. As they are undocumented internals while some
# common methods are included, they are incomplete and do not have getattr Incomplete fallback.
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from collections.abc import Callable, Sequence
from typing_extensions import Literal, Self, TypeAlias

import tensorflow as tf
from tensorflow import _ShapeLike

_Combiners: TypeAlias = Literal["mean", "sqrtn", "sum"]
_ExampleSpec: TypeAlias = dict[str, tf.io.FixedLenFeature | tf.io.VarLenFeature]

class FeatureColumn(ABC):
    @property
    @abstractmethod
    def name(self) -> str: ...
    @property
    @abstractmethod
    def parse_example_spec(self) -> _ExampleSpec: ...
    def __lt__(self, other: FeatureColumn) -> bool: ...
    def __gt__(self, other: FeatureColumn) -> bool: ...
    @property
    @abstractmethod
    def parents(self) -> list[FeatureColumn | str]: ...

class DenseColumn(FeatureColumn): ...
class SequenceDenseColumn(FeatureColumn): ...

# These classes are mostly subclasses of collections.namedtuple but we can't use
# typing.NamedTuple because they use multiple inheritance with other non namedtuple classes.
class NumericColumn(DenseColumn):
    key: str
    shape: _ShapeLike
    default_value: float
    dtype: tf.DType
    normalizer_fn: Callable[[tf.Tensor], tf.Tensor] | None

    def __init__(
        self,
        key: str,
        shape: _ShapeLike,
        default_value: float,
        dtype: tf.DType,
        normalizer_fn: Callable[[tf.Tensor], tf.Tensor] | None,
    ) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def parse_example_spec(self) -> _ExampleSpec: ...
    @property
    def parents(self) -> list[FeatureColumn | str]: ...

class SequenceNumericColumn(SequenceDenseColumn):
    key: str
    shape: _ShapeLike
    default_value: float
    dtype: tf.DType
    normalizer_fn: Callable[[tf.Tensor], tf.Tensor] | None

    def __init__(
        self,
        key: str,
        shape: _ShapeLike,
        default_value: float,
        dtype: tf.DType,
        normalizer_fn: Callable[[tf.Tensor], tf.Tensor] | None,
    ) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def parse_example_spec(self) -> _ExampleSpec: ...
    @property
    def parents(self) -> list[FeatureColumn | str]: ...

class CategoricalColumn(FeatureColumn):
    @property
    @abstractmethod
    def num_buckets(self) -> int: ...

class BucketizedColumn(DenseColumn, CategoricalColumn):
    source_column: NumericColumn
    boundaries: list[float] | tuple[float, ...]

    def __init__(self, source_column: NumericColumn, boundaries: list[float] | tuple[float, ...]) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def num_buckets(self) -> int: ...
    @property
    def parse_example_spec(self) -> _ExampleSpec: ...
    @property
    def parents(self) -> list[FeatureColumn | str]: ...

class EmbeddingColumn(DenseColumn, SequenceDenseColumn):
    categorical_column: CategoricalColumn
    dimension: int
    combiner: _Combiners
    initializer: Callable[[_ShapeLike], tf.Tensor] | None
    ckpt_to_load_from: str | None
    tensor_name_in_ckpt: str | None
    max_norm: float | None
    trainable: bool
    use_safe_embedding_lookup: bool

    def __init__(
        self,
        categorical_column: CategoricalColumn,
        dimension: int,
        combiner: _Combiners,
        initializer: Callable[[_ShapeLike], tf.Tensor] | None,
        ckpt_to_load_from: str | None,
        tensor_name_in_ckpt: str | None,
        max_norm: float | None,
        trainable: bool,
        use_safe_embedding_lookup: bool,
    ) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def parse_example_spec(self) -> _ExampleSpec: ...
    @property
    def parents(self) -> list[FeatureColumn | str]: ...

class SharedEmbeddingColumnCreator:
    def __getattr__(self, name: str) -> Incomplete: ...

class SharedEmbeddingColumn(DenseColumn, SequenceDenseColumn):
    categorical_column: CategoricalColumn
    shared_embedding_column_creator: SharedEmbeddingColumnCreator
    combiner: _Combiners
    max_norm: float | None
    use_safe_embedding_lookup: bool

    def __new__(
        cls,
        categorical_column: CategoricalColumn,
        shared_embedding_column_creator: SharedEmbeddingColumnCreator,
        combiner: _Combiners,
        max_norm: float | None,
        use_safe_embedding_lookup: bool = True,
    ) -> Self: ...
    @property
    def name(self) -> str: ...
    @property
    def parse_example_spec(self) -> _ExampleSpec: ...
    @property
    def parents(self) -> list[FeatureColumn | str]: ...

class CrossedColumn(CategoricalColumn):
    keys: tuple[str, ...]
    hash_bucket_size: int
    hash_key: int | None

    def __init__(self, keys: tuple[str, ...], hash_bucket_size: int, hash_key: int | None) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def num_buckets(self) -> int: ...
    @property
    def parse_example_spec(self) -> _ExampleSpec: ...
    @property
    def parents(self) -> list[FeatureColumn | str]: ...

class IdentityCategoricalColumn(CategoricalColumn):
    key: str
    number_buckets: int
    default_value: int | None

    def __init__(self, key: str, number_buckets: int, default_value: int | None) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def num_buckets(self) -> int: ...
    @property
    def parse_example_spec(self) -> _ExampleSpec: ...
    @property
    def parents(self) -> list[FeatureColumn | str]: ...

class HashedCategoricalColumn(CategoricalColumn):
    key: str
    hash_bucket_size: int
    dtype: tf.DType

    def __init__(self, key: str, hash_bucket_size: int, dtype: tf.DType) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def num_buckets(self) -> int: ...
    @property
    def parse_example_spec(self) -> _ExampleSpec: ...
    @property
    def parents(self) -> list[FeatureColumn | str]: ...

class VocabularyFileCategoricalColumn(CategoricalColumn):
    key: str
    vocabulary_file: str
    vocabulary_size: int | None
    num_oov_buckets: int
    dtype: tf.DType
    default_value: str | int | None
    file_format: str | None

    def __init__(
        self,
        key: str,
        vocabulary_file: str,
        vocabulary_size: int | None,
        num_oov_buckets: int,
        dtype: tf.DType,
        default_value: str | int | None,
        file_format: str | None,
    ) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def num_buckets(self) -> int: ...
    @property
    def parse_example_spec(self) -> _ExampleSpec: ...
    @property
    def parents(self) -> list[FeatureColumn | str]: ...

class VocabularyListCategoricalColumn(CategoricalColumn):
    key: str
    vocabulary_list: Sequence[str] | Sequence[int]
    dtype: tf.DType
    default_value: str | int | None
    num_oov_buckets: int

    def __init__(self, key: str, vocabulary_list: Sequence[str], num_oov_buckets: int, dtype: tf.DType) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def num_buckets(self) -> int: ...
    @property
    def parse_example_spec(self) -> _ExampleSpec: ...
    @property
    def parents(self) -> list[FeatureColumn | str]: ...

class WeightedCategoricalColumn(CategoricalColumn):
    categorical_column: CategoricalColumn
    weight_feature_key: str
    dtype: tf.DType

    def __init__(self, categorical_column: CategoricalColumn, weight_feature_key: str, dtype: tf.DType) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def num_buckets(self) -> int: ...
    @property
    def parse_example_spec(self) -> _ExampleSpec: ...
    @property
    def parents(self) -> list[FeatureColumn | str]: ...

class IndicatorColumn(DenseColumn, SequenceDenseColumn):
    categorical_column: CategoricalColumn

    def __init__(self, categorical_column: CategoricalColumn) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def parse_example_spec(self) -> _ExampleSpec: ...
    @property
    def parents(self) -> list[FeatureColumn | str]: ...

class SequenceCategoricalColumn(CategoricalColumn):
    categorical_column: CategoricalColumn

    def __init__(self, categorical_column: CategoricalColumn) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def num_buckets(self) -> int: ...
    @property
    def parse_example_spec(self) -> _ExampleSpec: ...
    @property
    def parents(self) -> list[FeatureColumn | str]: ...
