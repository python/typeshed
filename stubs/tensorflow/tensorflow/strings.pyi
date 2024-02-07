from collections.abc import Sequence
from typing import Any, Literal, overload

from tensorflow import RaggedTensor, Tensor, TensorCompatible

def join(inputs: Sequence[TensorCompatible | RaggedTensor], separator: str = "", name: str | None = None) -> Tensor: ...

# None corresponds to "" for split.
def split(
    input: TensorCompatible | RaggedTensor, sep: str | None = None, maxsplit: int = -1, name: str | None = None
) -> RaggedTensor: ...
@overload
def as_string(
    input: TensorCompatible,
    precision: int = -1,
    scientific: bool = False,
    shortest: bool = False,
    width: int = -1,
    fill: str = "",
    name: str | None = None,
) -> Tensor: ...
@overload
def as_string(
    input: RaggedTensor,
    precision: int = -1,
    scientific: bool = False,
    shortest: bool = False,
    width: int = -1,
    fill: str = "",
    name: str | None = None,
) -> RaggedTensor: ...
@overload
def unicode_decode(
    input: TensorCompatible,
    input_encoding: str,
    errors: Literal["replace", "strict", "ignore"] = "replace",
    replacement_char: int = 65533,
    replace_control_characters: bool = False,
    name: str | None = None,
) -> Tensor | RaggedTensor: ...
@overload
def unicode_decode(
    input: RaggedTensor,
    input_encoding: str,
    errors: Literal["replace", "strict", "ignore"] = "replace",
    replacement_char: int = 65533,
    replace_control_characters: bool = False,
    name: str | None = None,
) -> RaggedTensor: ...
def __getattr__(name: str) -> Any: ...
