from _typeshed import Incomplete
from collections.abc import Sequence
from typing import Literal, overload

from tensorflow import RaggedTensor, Tensor
from tensorflow._aliases import ScalarTensorCompatible, TensorCompatible
from tensorflow.math import l2_normalize as l2_normalize, sigmoid as sigmoid, tanh as tanh
from tensorflow.sparse import SparseTensor

def atrous_conv2d(
    value: Tensor, filters: Tensor, rate: int, padding: Literal["VALID", "SAME"], name: str | None = None
) -> Tensor: ...
def atrous_conv2d_transpose(
    value: Tensor, filters: Tensor, output_shape: Tensor, rate: int, padding: Literal["VALID", "SAME"], name: str | None = None
) -> Tensor: ...
def avg_pool(
    input: Tensor,
    ksize: int | Sequence[int],
    strides: int | Sequence[int],
    padding: Literal["VALID", "SAME"],
    data_format: Literal["NWC", "NCW", "NHWC", "NCHW", "NDHWC", "NCDHW"] | None = None,
    name: str | None = None,
) -> Tensor: ...
def avg_pool1d(
    input: Tensor,
    ksize: int | Sequence[int],
    strides: int | Sequence[int],
    padding: Literal["VALID", "SAME"],
    data_format: Literal["NWC", "NCW"] = "NWC",
    name: str | None = None,
) -> Tensor: ...
def avg_pool2d(
    input: Tensor,
    ksize: int | Sequence[int],
    strides: int | Sequence[int],
    padding: Literal["VALID", "SAME"],
    data_format: Literal["NHWC", "NCHW"] = "NHWC",
    name: str | None = None,
) -> Tensor: ...
def avg_pool3d(
    input: Tensor,
    ksize: int | Sequence[int],
    strides: int | Sequence[int],
    padding: Literal["VALID", "SAME"],
    data_format: Literal["NDHWC", "NCDHW"] = "NDHWC",
    name: str | None = None,
) -> Tensor: ...
def batch_normalization(
    x: Tensor, mean: Tensor, variance: Tensor, offset: Tensor, scale: Tensor, variance_epsilon: float, name: str | None = None
) -> Tensor: ...
def bias_add(
    value: Tensor, bias: Tensor, data_format: Literal["N...C", "NC..."] | None = None, name: str | None = None
) -> Tensor: ...
def collapse_repeated(labels: Tensor, seq_length: Tensor, name: str | None = None) -> tuple[Tensor, Tensor]: ...
def compute_accidental_hits(
    true_classes: Tensor, sampled_candidates: Tensor, num_true: int, seed: int | None = None, name: str | None = None
) -> tuple[Tensor, Tensor, Tensor]: ...
def compute_average_loss(
    per_example_loss: Tensor, sample_weight: Tensor | None = None, global_batch_size: int | None = None
) -> Tensor: ...
def conv1d(
    input: Tensor,
    filters: Tensor,
    stride: int | Sequence[int],
    padding: Literal["VALID", "SAME"],
    data_format: Literal["NWC", "NCW"] = "NWC",
    dilations: int | Sequence[int] | None = None,
    name: str | None = None,
) -> Tensor: ...
def conv1d_transpose(
    input: Tensor,
    filters: Tensor,
    output_shape: Tensor,
    strides: int | Sequence[int],
    padding: Literal["VALID", "SAME"] = "SAME",
    data_format: Literal["NWC", "NCW"] = "NWC",
    dilations: int | Sequence[int] | None = None,
    name: str | None = None,
) -> Tensor: ...
def conv2d(
    input: Tensor,
    filters: Tensor,
    strides: int | Sequence[int],
    padding: Literal["VALID", "SAME"],
    data_format: Literal["NHWC", "NCHW"] = "NHWC",
    dilations: int | Sequence[int] | None = None,
    name: str | None = None,
) -> Tensor: ...
def conv2d_transpose(
    input: Tensor,
    filters: Tensor,
    output_shape: Tensor,
    strides: int | Sequence[int],
    padding: Literal["VALID", "SAME"] = "SAME",
    data_format: Literal["NHWC", "NCHW"] = "NHWC",
    dilations: int | Sequence[int] | None = None,
    name: str | None = None,
) -> Tensor: ...
def conv3d(
    input: Tensor,
    filters: Tensor,
    strides: int | Sequence[int],
    padding: Literal["VALID", "SAME"],
    data_format: Literal["NDHWC", "NCDHW"] = "NDHWC",
    dilations: int | Sequence[int] | None = None,
    name: str | None = None,
) -> Tensor: ...
def conv3d_transpose(
    input: Tensor,
    filters: Tensor,
    output_shape: Tensor,
    strides: int | Sequence[int],
    padding: Literal["VALID", "SAME"] = "SAME",
    data_format: Literal["NDHWC", "NCDHW"] = "NDHWC",
    dilations: int | Sequence[int] | None = None,
    name: str | None = None,
) -> Tensor: ...
def conv_transpose(
    input: Tensor,
    filters: Tensor,
    output_shape: Tensor,
    strides: int | Sequence[int],
    padding: Literal["VALID", "SAME"] = "SAME",
    data_format: str | None = None,
    dilations: int | Sequence[int] | None = None,
    name: str | None = None,
) -> Tensor: ...
def convolution(
    input: Tensor,
    filters: Tensor,
    strides: int | Sequence[int] | None = None,
    padding: Literal["VALID", "SAME"] = "VALID",
    dilations: int | Sequence[int] | None = None,
    data_format: Literal["NC", "NWC", "NCW", "NHWC", "NCHW", "NDHWC", "NCDHW"] | None = None,
    name: str | None = None,
) -> Tensor: ...
def crelu(features: Tensor, axis: int = -1, name: str | None = None) -> Tensor: ...
def ctc_beam_search_decoder(
    inputs: Tensor, sequence_length: Tensor | Sequence[int], beam_width: int = 100, top_paths: int = 1
) -> tuple[list[SparseTensor], Tensor]: ...
def ctc_greedy_decoder(
    inputs: Tensor, sequence_length: Tensor | Sequence[int], merge_repeated: bool = True, blank_index: int | None = None
) -> tuple[list[SparseTensor], Tensor]: ...
def ctc_loss(
    labels: Tensor,
    logits: Tensor,
    label_length: Tensor,
    logit_length: Tensor,
    logits_time_major: bool = True,
    unique: int | None = None,
    blank_index: int | None = None,
    name: str | None = "ctc_loss_dense",
) -> Tensor: ...
def ctc_unique_labels(labels: Tensor, name: str | None = None) -> tuple[Tensor, Tensor]: ...
@overload
def embedding_lookup(
    params: TensorCompatible, ids: TensorCompatible, max_norm: float | None = None, name: str | None = None
) -> Tensor: ...
@overload
def embedding_lookup(
    params: TensorCompatible, ids: RaggedTensor, max_norm: float | None = None, name: str | None = None
) -> RaggedTensor: ...
def leaky_relu(features: TensorCompatible, alpha: float = 0.2, name: str | None = None) -> Tensor: ...
def log_poisson_loss(
    targets: TensorCompatible, log_input: TensorCompatible, compute_full_loss: bool = False, name: str | None = None
) -> Tensor: ...
def moments(
    x: TensorCompatible | RaggedTensor, axes: TensorCompatible, keepdims: bool = False, name: str | None = None
) -> tuple[Tensor, Tensor]: ...
def relu(features: TensorCompatible, name: str | None = None) -> Tensor: ...
def sigmoid_cross_entropy_with_logits(labels: TensorCompatible, logits: TensorCompatible, name: str | None = None) -> Tensor: ...
def softmax(logits: TensorCompatible, axis: ScalarTensorCompatible | None = None, name: str | None = None) -> Tensor: ...
def selu(features: TensorCompatible, name: str | None = None) -> Tensor: ...
def safe_embedding_lookup_sparse(
    embedding_weights: Tensor | list[Tensor],
    sparse_ids: SparseTensor,
    sparse_weights: SparseTensor | None = None,
    combiner: str = "mean",
    default_id: ScalarTensorCompatible | None = None,
    max_norm: float | None = None,
    name: str | None = None,
) -> Tensor: ...
def __getattr__(name: str) -> Incomplete: ...
