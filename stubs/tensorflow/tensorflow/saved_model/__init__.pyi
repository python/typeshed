from typing import Any, Generic, Mapping, Sequence, TypeVar
from typing_extensions import ParamSpec

import tensorflow as tf
from tensorflow.compat.v1.saved_model.signature_constants import *
from tensorflow.python.training.tracking.autotrackable import AutoTrackable
from tensorflow.saved_model.experimental import VariablePolicy
from tensorflow.types.experimental import ConcreteFunction, GenericFunction

_P = ParamSpec("_P")
_R = TypeVar("_R", covariant=True)

class SaveOptions:
    __slots__ = (
        "namespace_whitelist",
        "save_debug_info",
        "function_aliases",
        "experimental_io_device",
        "experimental_variable_policy",
        "experimental_custom_gradients",
    )
    namespace_whitelist: list[str]
    save_debug_info: bool
    function_aliases: dict[str, tf.types.experimental.GenericFunction[..., object]]
    experimental_io_device: str
    experimental_variable_policy: VariablePolicy
    experimental_custom_gradients: bool
    def __init__(
        self,
        namespace_whitelist: list[str] | None = None,
        save_debug_info: bool = False,
        function_aliases: dict[str, tf.types.experimental.GenericFunction[..., object]] | None = None,
        experimental_io_device: str | None = None,
        experimental_variable_policy: str | VariablePolicy | None = None,
        experimental_custom_gradients: bool = True,
    ): ...

class LoadOptions:
    def __init__(
        self,
        allow_partial_checkpoint: bool = False,
        experimental_io_device: str | None = None,
        experimental_skip_checkpoint: bool = False,
    ) -> None: ...

class _LoadedAttributes(Generic[_P, _R]):
    signatures: Mapping[str, ConcreteFunction[_P, _R]]

class _LoadedModel(AutoTrackable, _LoadedAttributes[_P, _R]):
    variables: list[tf.Variable]
    trainable_variables: list[tf.Variable]
    # TF1 model artifact specific
    graph: tf.Graph

def load(
    export_dir: str, tags: str | Sequence[str] | None = None, options: LoadOptions | None = None
) -> _LoadedModel[..., Any]: ...

_TF_Function = ConcreteFunction[..., object] | GenericFunction[..., object]

def save(
    obj: tf.Module,
    export_dir: str,
    signatures: _TF_Function | Mapping[str, _TF_Function] | None = None,
    options: SaveOptions | None = None,
) -> None: ...

SERVING = "serve"
TRAINING = "train"
EVAL = "eval"
GPU = "gpu"
TPU = "tpu"
