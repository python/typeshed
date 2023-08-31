from _typeshed import Incomplete

ALL_METRIC_CONFIGS: Incomplete

class FrameworkProfile:
    profiling_parameters: Incomplete
    def __init__(
        self,
        local_path="/opt/ml/output/profiler",
        file_max_size=10485760,
        file_close_interval=60,
        file_open_fail_threshold=50,
        detailed_profiling_config: Incomplete | None = None,
        dataloader_profiling_config: Incomplete | None = None,
        python_profiling_config: Incomplete | None = None,
        horovod_profiling_config: Incomplete | None = None,
        smdataparallel_profiling_config: Incomplete | None = None,
        start_step: Incomplete | None = None,
        num_steps: Incomplete | None = None,
        start_unix_time: Incomplete | None = None,
        duration: Incomplete | None = None,
    ) -> None: ...
