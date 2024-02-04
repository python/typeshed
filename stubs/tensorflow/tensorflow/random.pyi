from typing import Literal

import tensorflow as tf
from tensorflow._aliases import DTypeLike, ScalarTensorCompatible, ShapeLike

def uniform(
    shape: ShapeLike,
    minval: ScalarTensorCompatible = 0.0,
    maxval: ScalarTensorCompatible | None = None,
    dtype: DTypeLike = ...,
    seed: int | None = None,
    name: str | None = None,
) -> tf.Tensor: ...
def stateless_uniform(
    shape: ShapeLike,
    seed: tuple[int, int],
    minval: ScalarTensorCompatible = 0.0,
    maxval: ScalarTensorCompatible | None = None,
    dtype: DTypeLike = ...,
    name: str | None = None,
    alg: Literal["philox", "auto_select", "threefry"] = "auto_select",
) -> tf.Tensor: ...
def normal(
    shape: ShapeLike,
    mean: ScalarTensorCompatible = 0.0,
    stddev: ScalarTensorCompatible = 1.0,
    dtype: DTypeLike = ...,
    seed: int | None = None,
    name: str | None = None,
) -> tf.Tensor: ...
def truncated_normal(
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
def shuffle(value: tf.Tensor, seed: int | None = None, name: str | None = None) -> tf.Tensor: ...
def set_seed(seed: int) -> None: ...
