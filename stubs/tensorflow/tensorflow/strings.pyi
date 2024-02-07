from collections.abc import Sequence
from typing import Any, Literal, overload

from tensorflow import RaggedTensor, Tensor, TensorCompatible

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
def bytes_split(input: TensorCompatible | RaggedTensor, name: str | None = None) -> RaggedTensor: ...
def format(
    template: str, inputs: TensorCompatible, placeholder: str = "{}", summarize: int = 3, name: str | None = None
) -> Tensor: ...
def join(inputs: Sequence[TensorCompatible | RaggedTensor], separator: str = "", name: str | None = None) -> Tensor: ...
@overload
def length(input: TensorCompatible, unit: Literal["BYTE", "UTF8_CHAR"] = "BYTE", name: str | None = None) -> Tensor: ...
@overload
def length(input: RaggedTensor, unit: Literal["BYTE", "UTF8_CHAR"] = "BYTE", name: str | None = None) -> RaggedTensor: ...
@overload
def lower(input: TensorCompatible, encoding: Literal["utf-8", "", " "] = "", name: str | None = None) -> Tensor: ...
@overload
def lower(input: RaggedTensor, encoding: Literal["utf-8", "", " "] = "", name: str | None = None) -> RaggedTensor: ...
def ngrams(
    data: TensorCompatible | RaggedTensor,
    ngram_width: int | Sequence[int],
    separator: str = " ",
    pad_values: tuple[int, int] | str | None = None,
    padding_width: int | None = None,
    preserve_short_sequences: bool = False,
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
