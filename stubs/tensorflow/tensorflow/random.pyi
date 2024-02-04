from collections.abc import Sequence
from enum import Enum
from typing import Any, Generic, Literal, TypeAlias, TypeVar

import numpy as np
import numpy.typing as npt
import tensorflow as tf
from tensorflow._aliases import DTypeFloat, DTypeInt, DTypeLike, ScalarTensorCompatible, ShapeLike
from tensorflow.python.trackable import autotrackable

_STATE_TYPE = TypeVar("_STATE_TYPE")
_State: TypeAlias = Sequence[_STATE_TYPE]

class Algorithm(Enum):
    PHILOX = 1
    THREEFRY = 2
    AUTO_SELECT = 3

_Alg: TypeAlias = Literal[Algorithm.PHILOX, Algorithm.THREEFRY, Algorithm.AUTO_SELECT, "philox", "threefry", "auto_select"]

class Generator(autotrackable.AutoTrackable, Generic[_STATE_TYPE]):
    @classmethod
    def from_state(
        cls, state: _State[_STATE_TYPE], alg: Literal[Algorithm.PHILOX, Algorithm.THREEFRY, "philox", "threefry"] | None
    ) -> Generator[_STATE_TYPE]: ...
    @classmethod
    def from_seed(
        cls, seed: int, alg: Literal[Algorithm.PHILOX, Algorithm.THREEFRY, "philox", "threefry"] | None = None
    ) -> Generator[_STATE_TYPE]: ...
    @classmethod
    def from_non_deterministic_state(
        cls, alg: Literal[Algorithm.PHILOX, Algorithm.THREEFRY, "philox", "threefry"] | None = None
    ) -> Generator[_STATE_TYPE]: ...
    @classmethod
    def from_key_counter(
        cls,
        key: _STATE_TYPE,
        counter: Sequence[_STATE_TYPE],
        alg: Literal[Algorithm.PHILOX, Algorithm.THREEFRY, "philox", "threefry"] | None,
    ) -> Generator[_STATE_TYPE]: ...
    def __init__(
        self,
        copy_from: Generator[_STATE_TYPE] | None = None,
        state: _State[_STATE_TYPE] | None = None,
        alg: Literal[Algorithm.PHILOX, Algorithm.THREEFRY, "philox", "threefry"] | None = None,
    ) -> None: ...
    def reset(self, state: _State[_STATE_TYPE]) -> None: ...
    def reset_from_seed(self, seed: int) -> None: ...
    def reset_from_key_counter(self, key: _STATE_TYPE, counter: Sequence[_STATE_TYPE]) -> None: ...
    @property
    def state(self) -> _State[_STATE_TYPE]: ...
    @property
    def algorithm(self) -> int: ...
    @property
    def key(self) -> _STATE_TYPE: ...
    def skip(self, delta: int) -> tf.Tensor: ...
    def normal(
        self,
        mean: ScalarTensorCompatible = 0.0,
        stddev: ScalarTensorCompatible = 1.0,
        dtype: DTypeLike = ...,
        name: str | None = None,
    ) -> tf.Tensor: ...
    def truncated_normal(
        self,
        shape: ShapeLike,
        mean: ScalarTensorCompatible = 0.0,
        stddev: ScalarTensorCompatible = 1.0,
        dtype: DTypeLike = ...,
        name: str | None = None,
    ) -> tf.Tensor: ...
    def uniform(
        self,
        shape: ShapeLike,
        minval: ScalarTensorCompatible = 0.0,
        maxval: ScalarTensorCompatible | None = None,
        dtype: DTypeLike = ...,
        name: str | None = None,
    ) -> tf.Tensor: ...
    def uniform_full_int(self, shape: ShapeLike, dtype: DTypeLike = ..., name: str | None = None) -> tf.Tensor: ...
    def binomial(self, shape: ShapeLike, counts, probs, dtype: DTypeLike = ..., name: str | None = None) -> tf.Tensor: ...
    def make_seeds(self, count: int = 1) -> tf.Tensor: ...
    def split(self, count: int = 1) -> list[Generator[_STATE_TYPE]]: ...

def all_candidate_sampler(
    true_classes: tf.Tensor, num_true: int, num_sampled: int, unique: bool, seed: int | None = None, name: str | None = None
) -> tuple[tf.Tensor, tf.Tensor, tf.Tensor]: ...
def categorical(
    logits: tf.Tensor,
    num_samples: int | tf.Tensor,
    dtype: DTypeLike | None = None,
    seed: int | None = None,
    name: str | None = None,
) -> tf.Tensor: ...
def create_rng_state(
    seed: int, alg: Literal[Algorithm.PHILOX, Algorithm.THREEFRY, Algorithm.AUTO_SELECT, "philox", "threefry", "auto_select"]
) -> npt.NDArray[np.int64]: ...
def fixed_unigram_candidate_sampler(
    true_classes: tf.Tensor,
    num_true: int,
    num_sampled: int,
    unique: bool,
    range_max: int,
    vocab_file: str = "",
    distortion: float = 1.0,
    num_reserved_ids: int = 0,
    num_shards: int = 1,
    shard: int = 0,
    unigrams: Sequence[float] = (),
    seed: int | None = None,
    name: str | None = None,
) -> tuple[tf.Tensor, tf.Tensor, tf.Tensor]: ...
def fold_in(
    seed: tf.Tensor | Sequence[int],
    data: int,
    alg: Literal[
        Algorithm.PHILOX, Algorithm.THREEFRY, Algorithm.AUTO_SELECT, "philox", "threefry", "auto_select"
    ] = "auto_select",
) -> int: ...
def gamma(
    shape: tf.Tensor | Sequence[int],
    alpha: tf.Tensor | float | Sequence[float],
    beta: tf.Tensor | float | Sequence[float] | None = None,
    dtype: tf.dtypes.float16 | tf.dtypes.float32 | tf.dtypes.float64 = ...,
    seed: int | None = None,
    name: str | None = None,
) -> tf.Tensor: ...
def get_global_generator() -> Generator[Any]: ...
def learned_unigram_candidate_sampler(
    true_classes: tf.Tensor,
    num_true: int,
    num_sampled: int,
    unique: bool,
    range_max: int,
    seed: int | None = None,
    name: str | None = None,
) -> tuple[tf.Tensor, tf.Tensor, tf.Tensor]: ...
def log_uniform_candidate_sampler(
    true_classes: tf.Tensor,
    num_true: int,
    num_sampled: int,
    unique: bool,
    range_max: int,
    seed: int | None = None,
    name: str | None = None,
) -> tuple[tf.Tensor, tf.Tensor, tf.Tensor]: ...
def normal(
    shape: ShapeLike,
    mean: ScalarTensorCompatible = 0.0,
    stddev: ScalarTensorCompatible = 1.0,
    dtype: DTypeLike = ...,
    seed: int | None = None,
    name: str | None = None,
) -> tf.Tensor: ...
def poisson(
    shape: ShapeLike, lam: ScalarTensorCompatible = 1.0, dtype: DTypeLike = ..., seed: int | None = None, name: str | None = None
) -> tf.Tensor: ...
def set_global_generator(generator: Generator[Any]) -> None: ...
def set_seed(seed: int) -> None: ...
def shuffle(value: tf.Tensor, seed: int | None = None, name: str | None = None) -> tf.Tensor: ...
def split(seed: tf.Tensor | Sequence[int], data: int = 2, alg: _Alg = "auto_select") -> tf.Tensor: ...
def stateless_binomial(
    shape: ShapeLike,
    seed: tuple[int, int] | tf.Tensor,
    counts: tf.Tensor,
    probs: tf.Tensor,
    output_dtype: DTypeLike = ...,
    name: str | None = None,
) -> tf.Tensor: ...
def stateless_categorical(
    logits: tf.Tensor,
    num_samples: int | tf.Tensor,
    seed: tuple[int, int] | tf.Tensor,
    dtype: tf.dtypes.int32 | tf.dtypes.int64 = ...,
    name: str | None = None,
) -> tf.Tensor: ...
def stateless_gamma(
    shape: ShapeLike,
    seed: tuple[int, int] | tf.Tensor,
    alpha: tf.Tensor,
    beta: tf.Tensor | None = None,
    dtype: tf.dtypes.float16 | tf.dtypes.float32 | tf.dtypes.float64 = ...,
    name: str | None = None,
) -> tf.Tensor: ...
def stateless_normal(
    shape: tf.Tensor | Sequence[int],
    seed: tuple[int, int] | tf.Tensor,
    mean: float | tf.Tensor = 0.0,
    stddev: float | tf.Tensor = 1.0,
    dtype: tf.dtypes.float16 | tf.dtypes.bfloat16 | tf.dtypes.float32 | tf.dtypes.float64 = ...,
    name: str | None = None,
    alg: _Alg = "auto_select",
) -> tf.Tensor: ...
def stateless_parameterized_truncated_normal(
    shape: tf.Tensor | Sequence[int],
    seed: tuple[int, int] | tf.Tensor,
    mean: float | tf.Tensor = 0.0,
    stddev: float | tf.Tensor = 1.0,
    minvals: tf.Tensor | float = -2.0,
    maxvals: tf.Tensor | float = 2.0,
    name: str | None = None,
) -> tf.Tensor: ...
def stateless_poisson(
    shape: tf.Tensor | Sequence[int],
    seed: tuple[int, int] | tf.Tensor,
    lam: tf.Tensor,
    dtype: DTypeInt | DTypeFloat = ...,
    name: str | None = None,
) -> tf.Tensor: ...
def stateless_truncated_normal(
    shape: tf.Tensor | Sequence[int],
    seed: tuple[int, int] | tf.Tensor,
    mean: float | tf.Tensor = 0.0,
    stddev: float | tf.Tensor = 1.0,
    dtype: DTypeFloat = ...,
    name: str | None = None,
    alg: _Alg = "auto_select",
) -> tf.Tensor: ...
def stateless_uniform(
    shape: tf.Tensor | Sequence[int],
    seed: tuple[int, int] | tf.Tensor,
    minval: float | tf.Tensor = 0.0,
    maxval: float | tf.Tensor | None = None,
    dtype: tf.dtypes.float16
    | tf.dtypes.bfloat16
    | tf.dtypes.float32
    | tf.dtypes.float64
    | tf.dtypes.int32
    | tf.dtypes.int64
    | tf.dtypes.uint32
    | tf.dtypes.uint64 = ...,
    name: str | None = None,
    alg: _Alg = "auto_select",
) -> tf.Tensor: ...
def truncated_normal(
    shape: tf.Tensor | Sequence[int],
    mean: float | tf.Tensor = 0.0,
    stddev: float | tf.Tensor = 1.0,
    dtype: DTypeFloat = ...,
    seed: int | None = None,
    name: str | None = None,
) -> tf.Tensor: ...
def uniform(
    shape: tf.Tensor | Sequence[int],
    minval: float | tf.Tensor = 0.0,
    maxval: float | tf.Tensor | None = None,
    dtype: tf.dtypes.float16
    | tf.dtypes.bfloat16
    | tf.dtypes.float32
    | tf.dtypes.float64
    | tf.dtypes.int32
    | tf.dtypes.int64 = ...,
    seed: int | None = None,
    name: str | None = None,
) -> tf.Tensor: ...
def uniform_candidate_sampler(
    true_classes: tf.Tensor,
    num_true: int,
    num_sampled: int,
    unique: bool,
    range_max: int,
    seed: int | None = None,
    name: str | None = None,
) -> tuple[tf.Tensor, tf.Tensor, tf.Tensor]: ...
