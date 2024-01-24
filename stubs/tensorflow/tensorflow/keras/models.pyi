from collections.abc import Callable
from pathlib import Path

_ShapeLike: TypeAlias = TensorShape | Iterable[_ScalarTensorCompatible | None] | int | Tensor

# class Model(base_layer.Layer, version_utils.ModelVersionSelector):
class Model:
    def __init__(self, *args, **kwargs) -> None: ...
    def build(self, input_shape: _ShapeLike): ...
    def summary(
        self,
        line_length: None | int = None,
        positions: None | list[float] = None,
        print_fn: None | Callable[[str], None] = None,
        expand_nested: bool = False,
        show_trainable: bool = False,
        layer_range: None | list[str] | tuple[str, str] =None,
    ): ...
    def load_weights(
        self, filepath: str | Path, skip_mismatch: bool = False, by_name: bool = False, options: None | tensorflow.train.CheckpointOptions =None
    ): ...
