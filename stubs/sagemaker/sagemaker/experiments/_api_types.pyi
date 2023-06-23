import enum
from _typeshed import Incomplete

from sagemaker.apiutils import _base_types

class TrialComponentMetricSummary(_base_types.ApiObject):
    metric_name: Incomplete
    source_arn: Incomplete
    time_stamp: Incomplete
    max: Incomplete
    min: Incomplete
    last: Incomplete
    count: Incomplete
    avg: Incomplete
    std_dev: Incomplete
    def __init__(self, metric_name: Incomplete | None = None, source_arn: Incomplete | None = None, **kwargs) -> None: ...

class TrialComponentParameters(_base_types.ApiObject):
    @classmethod
    def from_boto(cls, boto_dict, **kwargs): ...
    @classmethod
    def to_boto(cls, parameters): ...

class TrialComponentArtifact(_base_types.ApiObject):
    value: Incomplete
    media_type: Incomplete
    def __init__(self, value: Incomplete | None = None, media_type: Incomplete | None = None, **kwargs) -> None: ...

class _TrialComponentStatusType(enum.Enum):
    InProgress: str
    Completed: str
    Failed: str

class TrialComponentStatus(_base_types.ApiObject):
    primary_status: Incomplete
    message: Incomplete
    def __init__(self, primary_status: Incomplete | None = None, message: Incomplete | None = None, **kwargs) -> None: ...

class TrialComponentSummary(_base_types.ApiObject):
    trial_component_name: Incomplete
    trial_component_arn: Incomplete
    display_name: Incomplete
    source_arn: Incomplete
    status: Incomplete
    start_time: Incomplete
    end_time: Incomplete
    creation_time: Incomplete
    created_by: Incomplete
    last_modified_time: Incomplete
    last_modified_by: Incomplete

class TrialComponentSource(_base_types.ApiObject):
    source_arn: Incomplete
    def __init__(self, source_arn: Incomplete | None = None, **kwargs) -> None: ...

class Parent(_base_types.ApiObject):
    trial_name: Incomplete
    experiment_name: Incomplete
    run_name: Incomplete

class TrialComponentSearchResult(_base_types.ApiObject):
    trial_component_arn: Incomplete
    trial_component_name: Incomplete
    display_name: Incomplete
    source: Incomplete
    status: Incomplete
    start_time: Incomplete
    end_time: Incomplete
    creation_time: Incomplete
    created_by: Incomplete
    last_modified_time: Incomplete
    last_modified_by: Incomplete
    parameters: Incomplete
    input_artifacts: Incomplete
    output_artifacts: Incomplete
    metrics: Incomplete
    source_detail: Incomplete
    tags: Incomplete
    parents: Incomplete

class TrialSummary(_base_types.ApiObject):
    trial_arn: Incomplete
    trial_name: Incomplete
    creation_time: Incomplete
    last_modified_time: Incomplete
