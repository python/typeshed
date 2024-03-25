from typing import Literal

from tensorflow._aliases import TensorCompatible
from tensorflow.keras.layers.preprocessing.index_lookup import _IndexLookup

class StringLookup(_IndexLookup):
    def __init__(
        self,
        max_tokens: int | None = None,
        num_oov_indices: int = 1,
        mask_token: str | None = None,
        oov_token: str = "[UNK]",
        vocabulary: str | None | TensorCompatible = None,
        idf_weights: TensorCompatible | None = None,
        encoding: str = "utf-8",
        invert: bool = False,
        output_mode: Literal["int", "count", "multi_hot", "one_hot", "tf_idf"] = "int",
        sparse: bool = False,
        pad_to_max_tokens: bool = False,
    ) -> None: ...

class IntegerLookup(_IndexLookup):
    def __init__(
        self,
        max_tokens: int | None = None,
        num_oov_indices: int = 1,
        mask_token: int | None = None,
        oov_token: int = -1,
        vocabulary: str | None | TensorCompatible = None,
        vocabulary_dtype: Literal["int64", "int32"] = "int64",
        idf_weights: TensorCompatible | None = None,
        invert: bool = False,
        output_mode: Literal["int", "count", "multi_hot", "one_hot", "tf_idf"] = "int",
        sparse: bool = False,
        pad_to_max_tokens: bool = False,
    ) -> None: ...
