from _typeshed import Incomplete
from collections.abc import Callable, Iterator
from pathlib import Path
from typing import Any, Literal, Self

# import numpy as np
# import numpy.typing as npt
import tensorflow
import tensorflow as tf
from tensorflow import Variable, _ShapeLike, _TensorCompatible
from tensorflow.keras.layers import Layer, _InputT, _OutputT

class Model(Layer[_InputT, _OutputT], tf.Module):
    def __new__(cls, *args, **kwargs) -> Model[_InputT, _OutputT]: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __setattr__(self, name, value) -> None: ...
    def __reduce__(self) -> Incomplete: ...
    def __deepcopy__(self, memo) -> Incomplete: ...
    def build(self, input_shape: _ShapeLike) -> None: ...
    def __call__(self, inputs: _InputT, *, training: bool = False, mask: _TensorCompatible | None = None) -> _OutputT: ...
    def call(self, inputs: _InputT, training: bool = False, mask: _TensorCompatible | None = None) -> _OutputT: ...
    def compile(
        self,
        optimizer="rmsprop",
        loss=None,
        metrics=None,
        loss_weights=None,
        weighted_metrics=None,
        run_eagerly=None,
        steps_per_execution=None,
        jit_compile=None,
        pss_evaluation_shards=0,
        **kwargs,
    ) -> Incomplete: ...
    @property
    def metrics(self) -> list[Incomplete]: ...
    @property
    def metrics_names(self) -> list[str]: ...
    @property
    def distribute_strategy(self) -> Incomplete: ...  # tf.distribute.Strategy
    @property
    def run_eagerly(self) -> bool: ...
    @property
    def autotune_steps_per_execution(self) -> Incomplete: ...
    @property
    def steps_per_execution(self) -> int: ...
    @property
    def jit_compile(self) -> bool: ...
    @property
    def distribute_reduction_method(self) -> Incomplete | Literal["auto"]: ...
    def train_step(self, data: _TensorCompatible) -> Incomplete: ...
    def compute_loss(
        self,
        x: _TensorCompatible | None = None,
        y: _TensorCompatible | None = None,
        y_pred: _TensorCompatible | None = None,
        sample_weight: Incomplete | None = None,
    ) -> tf.Tensor | None: ...
    def compute_metrics(
        self, x: _TensorCompatible, y: _TensorCompatible, y_pred: _TensorCompatible, sample_weight: Incomplete
    ) -> dict[str, float]: ...
    def get_metrics_result(self) -> dict[str, float]: ...
    def make_train_function(self, force: bool = False) -> Callable[[tf.data.Iterator[Incomplete]], dict[str, float]]: ...
    def fit(
        self,
        x=None,
        y=None,
        batch_size=None,
        epochs=1,
        verbose="auto",
        callbacks=None,
        validation_split=0.0,
        validation_data=None,
        shuffle=True,
        class_weight=None,
        sample_weight=None,
        initial_epoch=0,
        steps_per_epoch=None,
        validation_steps=None,
        validation_batch_size=None,
        validation_freq=1,
        max_queue_size=10,
        workers=1,
        use_multiprocessing=False,
    ): ...
    def test_step(self, data: _TensorCompatible) -> dict[str, float]: ...
    def make_test_function(self, force: bool = False) -> Callable[[tf.data.Iterator[Incomplete]], dict[str, float]]: ...
    def evaluate(
        self,
        x=None,
        y=None,
        batch_size=None,
        verbose="auto",
        sample_weight=None,
        steps=None,
        callbacks=None,
        max_queue_size=10,
        workers=1,
        use_multiprocessing=False,
        return_dict=False,
        **kwargs,
    ): ...
    def predict_step(self, data: _InputT) -> _OutputT: ...
    def make_predict_function(self, force: bool = False) -> Callable[[tf.data.Iterator[Incomplete]], _OutputT]: ...
    def predict(
        self,
        x,
        batch_size=None,
        verbose="auto",
        steps=None,
        callbacks=None,
        max_queue_size=10,
        workers=1,
        use_multiprocessing=False,
    ): ...
    def reset_metrics(self) -> None: ...
    def train_on_batch(
        self, x, y=None, sample_weight=None, class_weight=None, reset_metrics=True, return_dict=False
    ) -> float | list[float]: ...
    def test_on_batch(self, x, y=None, sample_weight=None, reset_metrics=True, return_dict=False) -> float | list[float]: ...
    def predict_on_batch(self, x: Iterator[_InputT]) -> Incomplete: ...  # npt.NDArray[_OutputT]
    def fit_generator(
        self,
        generator,
        steps_per_epoch=None,
        epochs=1,
        verbose=1,
        callbacks=None,
        validation_data=None,
        validation_steps=None,
        validation_freq=1,
        class_weight=None,
        max_queue_size=10,
        workers=1,
        use_multiprocessing=False,
        shuffle=True,
        initial_epoch=0,
    ): ...
    def evaluate_generator(
        self, generator, steps=None, callbacks=None, max_queue_size=10, workers=1, use_multiprocessing=False, verbose=0
    ): ...
    def predict_generator(
        self, generator, steps=None, callbacks=None, max_queue_size=10, workers=1, use_multiprocessing=False, verbose=0
    ): ...
    @property
    def trainable_weights(self) -> list[Variable]: ...
    @property
    def non_trainable_weights(self) -> list[Variable]: ...
    def get_weights(self): ...
    def save(self, filepath, overwrite=True, save_format=None, **kwargs): ...
    def save_weights(self, filepath, overwrite=True, save_format=None, options=None): ...
    def load_weights(
        self,
        filepath: str | Path,
        skip_mismatch: bool = False,
        by_name: bool = False,
        options: None | tensorflow.train.CheckpointOptions = None,
    ): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config: dict[str, Any], custom_objects=None) -> Self: ...
    def to_json(self, **kwargs) -> str: ...
    def to_yaml(self, **kwargs) -> str: ...
    def reset_states(self) -> None: ...
    @property
    def state_updates(self) -> list[Incomplete]: ...
    @property
    def weights(self) -> list[Variable]: ...
    def summary(
        self,
        line_length: None | int = None,
        positions: None | list[float] = None,
        print_fn: None | Callable[[str], None] = None,
        expand_nested: bool = False,
        show_trainable: bool = False,
        layer_range: None | list[str] | tuple[str, str] = None,
    ): ...
    @property
    def layers(self) -> list[Layer[Incomplete, Incomplete]]: ...
    def get_layer(self, name=None, index=None) -> Layer[Incomplete, Incomplete]: ...
    def get_weight_paths(self): ...
    def get_compile_config(self) -> dict[str, Any]: ...
    def compile_from_config(self, config: dict[str, Any]) -> Self: ...
    def export(self, filepath: str | Path) -> None: ...
    def save_spec(self, dynamic_batch: bool = True) -> tuple[tuple[tf.TensorSpec, ...], dict[str, tf.TensorSpec]] | None: ...
