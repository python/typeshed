from _typeshed import Incomplete

class StepRange:
    start_step: Incomplete
    num_steps: Incomplete
    def __init__(self, start_step, num_steps) -> None: ...
    def to_json(self): ...

class TimeRange:
    start_unix_time: Incomplete
    duration: Incomplete
    def __init__(self, start_unix_time, duration) -> None: ...
    def to_json(self): ...

class MetricsConfigBase:
    name: Incomplete
    range: Incomplete
    def __init__(self, name, start_step, num_steps, start_unix_time, duration) -> None: ...
    def to_json_string(self): ...

class DetailedProfilingConfig(MetricsConfigBase):
    def __init__(
        self,
        start_step: Incomplete | None = None,
        num_steps: Incomplete | None = None,
        start_unix_time: Incomplete | None = None,
        duration: Incomplete | None = None,
        profile_default_steps: bool = False,
    ) -> None: ...

class DataloaderProfilingConfig(MetricsConfigBase):
    metrics_regex: Incomplete
    def __init__(
        self,
        start_step: Incomplete | None = None,
        num_steps: Incomplete | None = None,
        start_unix_time: Incomplete | None = None,
        duration: Incomplete | None = None,
        profile_default_steps: bool = False,
        metrics_regex: str = ".*",
    ) -> None: ...

class PythonProfilingConfig(MetricsConfigBase):
    python_profiler: Incomplete
    cprofile_timer: Incomplete
    def __init__(
        self,
        start_step: Incomplete | None = None,
        num_steps: Incomplete | None = None,
        start_unix_time: Incomplete | None = None,
        duration: Incomplete | None = None,
        profile_default_steps: bool = False,
        python_profiler=...,
        cprofile_timer=...,
    ) -> None: ...

class HorovodProfilingConfig(MetricsConfigBase):
    def __init__(
        self,
        start_step: Incomplete | None = None,
        num_steps: Incomplete | None = None,
        start_unix_time: Incomplete | None = None,
        duration: Incomplete | None = None,
        profile_default_steps: bool = False,
    ) -> None: ...

class SMDataParallelProfilingConfig(MetricsConfigBase):
    def __init__(
        self,
        start_step: Incomplete | None = None,
        num_steps: Incomplete | None = None,
        start_unix_time: Incomplete | None = None,
        duration: Incomplete | None = None,
        profile_default_steps: bool = False,
    ) -> None: ...
