from _typeshed import Incomplete
from collections.abc import Callable, Iterable, Mapping, Sequence
from typing import Any, Literal
from typing_extensions import TypeAlias

import tensorflow as tf
from tensorflow.keras import Model
from tensorflow.keras.optimizers.schedules import LearningRateSchedule

_Logs: TypeAlias = Mapping[str, Any] | None | Any

class Callback:
    model: Model  # Model[Any, object]
    params: dict[str, Any]
    # def set_model(self, model: Model[Any, object]) -> None: ...
    def set_model(self, model: Model) -> None: ...
    def set_params(self, params: dict[str, Any]) -> None: ...
    def on_batch_begin(self, batch: int, logs: _Logs = None) -> None: ...
    def on_batch_end(self, batch: int, logs: _Logs = None) -> None: ...
    def on_epoch_begin(self, epoch: int, logs: _Logs = None) -> None: ...
    def on_epoch_end(self, epoch: int, logs: _Logs = None) -> None: ...
    def on_predict_batch_begin(self, batch: int, logs: _Logs = None) -> None: ...
    def on_predict_batch_end(self, batch: int, logs: _Logs = None) -> None: ...
    def on_predict_begin(self, logs: _Logs = None) -> None: ...
    def on_predict_end(self, logs: _Logs = None) -> None: ...
    def on_test_batch_begin(self, batch: int, logs: _Logs = None) -> None: ...
    def on_test_batch_end(self, batch: int, logs: _Logs = None) -> None: ...
    def on_test_begin(self, logs: _Logs = None) -> None: ...
    def on_test_end(self, logs: _Logs = None) -> None: ...
    def on_train_batch_begin(self, batch: int, logs: _Logs = None) -> None: ...
    def on_train_batch_end(self, batch: int, logs: _Logs = None) -> None: ...
    def on_train_begin(self, logs: _Logs = None) -> None: ...
    def on_train_end(self, logs: _Logs = None) -> None: ...

# A CallbackList has exact same api as a callback,
# but does not actually subclass it.
class CallbackList:
    def __init__(
        self,
        callbacks: Sequence[Callback] | None = None,
        add_history: bool = False,
        add_progbar: bool = False,
        # model: Model[Any, object] | None = None,
        model: Model | None = None,
        **params: Any,
    ) -> None: ...
    # def set_model(self, model: Model[Any, object]) -> None: ...
    def set_model(self, model: Model) -> None: ...
    def set_params(self, params: dict[str, Any]) -> None: ...
    def on_batch_begin(self, batch: int, logs: Mapping[str, object] | None = None) -> None: ...
    def on_batch_end(self, batch: int, logs: Mapping[str, object] | None = None) -> None: ...
    def on_epoch_begin(self, epoch: int, logs: Mapping[str, object] | None = None) -> None: ...
    def on_epoch_end(self, epoch: int, logs: Mapping[str, object] | None = None) -> None: ...
    def on_predict_batch_begin(self, batch: int, logs: Mapping[str, object] | None = None) -> None: ...
    def on_predict_batch_end(self, batch: int, logs: Mapping[str, object] | None = None) -> None: ...
    def on_predict_begin(self, logs: Mapping[str, object] | None = None) -> None: ...
    def on_predict_end(self, logs: Mapping[str, object] | None = None) -> None: ...
    def on_test_batch_begin(self, batch: int, logs: Mapping[str, object] | None = None) -> None: ...
    def on_test_batch_end(self, batch: int, logs: Mapping[str, object] | None = None) -> None: ...
    def on_test_begin(self, logs: Mapping[str, object] | None = None) -> None: ...
    def on_test_end(self, logs: Mapping[str, object] | None = None) -> None: ...
    def on_train_batch_begin(self, batch: int, logs: Mapping[str, object] | None = None) -> None: ...
    def on_train_batch_end(self, batch: int, logs: Mapping[str, object] | None = None) -> None: ...
    def on_train_begin(self, logs: Mapping[str, object] | None = None) -> None: ...
    def on_train_end(self, logs: Mapping[str, object] | None = None) -> None: ...

class History(Callback):
    history: dict[str, list[Any]]

class ModelCheckpoint(Callback):
    monitor_op: Any
    filepath: str
    _options: tf.train.CheckpointOptions | tf.saved_model.SaveOptions | None
    def __init__(
        self,
        filepath: str,
        monitor: str = "val_loss",
        verbose: Literal[0, 1] = 0,
        save_best_only: bool = False,
        save_weights_only: bool = False,
        mode: Literal["auto", "min", "max"] = "auto",
        save_freq: str | int = "epoch",
        options: tf.train.CheckpointOptions | tf.saved_model.SaveOptions | None = None,
        initial_value_threshold: float | None = None,
    ) -> None: ...
    def _save_model(self, epoch: int, batch: int | None, logs: _Logs): ...

class TensorBoard(Callback):
    _start_batch: int
    _stop_batch: int
    _should_write_train_graph: bool
    write_steps_per_second: bool
    _batch_start_time: float
    _train_step: tf.Variable
    _should_trace: bool
    _is_tracing: bool
    _global_train_batch: int
    update_freq: int | Literal["epoch"]

    def __init__(
        self,
        log_dir: str = "logs",
        histogram_freq: int = 0,
        write_graph: bool = True,
        write_images: bool = False,
        write_steps_per_second: bool = False,
        update_freq: int | Literal["epoch"] = "epoch",
        profile_batch: int | tuple[int, int] = 0,
        embeddings_freq: int = 0,
        embeddings_metadata: dict[str, None] | None = None,
    ) -> None: ...
    def _write_keras_model_train_graph(self) -> None: ...
    def _stop_trace(self, batch: int | None = None) -> None: ...

class BackupAndRestore(Callback):
    def __init__(
        self, backup_dir: str, save_freq: str = "epoch", delete_checkpoint: bool = True, save_before_preemption: bool = False
    ) -> None: ...

class BackupAndRestoreExperimental(BackupAndRestore):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class RemoteMonitor(Callback):
    def __init__(
        self,
        root: str = "http://localhost:9000",
        path: str = "/publish/epoch/end/",
        field: str = "data",
        headers: dict[Incomplete, Incomplete] | None = None,
        send_as_json: bool = False,
    ): ...

class ReduceLROnPlateau(Callback):
    def __init__(
        self,
        monitor: str = "val_loss",
        factor: float = 0.1,
        patience: int = 10,
        verbose: Literal[0, 1] = 0,
        mode: Literal["auto", "min", "max"] = "auto",
        min_delta: float = 1e-4,
        cooldown: int = 0,
        min_lr: float = 0,
        **kwargs,
    ): ...

class BaseLogger(Callback):
    def __init__(self, stateful_metrics: Iterable[str] | None = None) -> None: ...

class CSVLogger(Callback):
    def __init__(self, filename: str, separator: str = ",", append: bool = False) -> None: ...

class EarlyStopping(Callback):
    monitor_op: Any
    def __init__(
        self,
        monitor: str = "val_loss",
        min_delta: float = 0,
        patience: float = 0,
        verbose: Literal[0, 1] = 0,
        mode: Literal["auto", "min", "max"] = "auto",
        baseline: float | None = None,
        restore_best_weights: bool = False,
        start_from_epoch: int = 0,
    ) -> None: ...

class LearningRateScheduler(Callback):
    def __init__(self, schedule: LearningRateSchedule, verbose: Literal[0, 1] = 0) -> None: ...

class ProgbarLogger(Callback):
    use_steps: bool
    def __init__(
        self, count_mode: Literal["steps", "samples"] = "samples", stateful_metrics: Iterable[str] | None = None
    ) -> None: ...

class TerminateOnNaN(Callback): ...

class LambdaCallback(Callback):
    def __init__(
        self,
        on_epoch_begin: Callable[[int, Incomplete], Incomplete] | None = None,
        on_epoch_end: Callable[[int, Incomplete], Incomplete] | None = None,
        on_batch_begin: Callable[[int, Incomplete], Incomplete] | None = None,
        on_batch_end: Callable[[int, Incomplete], Incomplete] | None = None,
        on_train_begin: Callable[[Incomplete], Incomplete] | None = None,
        on_train_end: Callable[[Incomplete], Incomplete] | None = None,
        **kwargs,
    ): ...
