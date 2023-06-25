from _typeshed import Incomplete
from typing import List

from sagemaker.apiutils import _base_types
from sagemaker.lineage.artifact import Artifact
from sagemaker.lineage.query import LineageQueryDirectionEnum

LOGGER: Incomplete

class LineageTrialComponent(_base_types.Record):
    trial_component_name: Incomplete
    trial_component_arn: Incomplete
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
    parameters_to_remove: Incomplete
    input_artifacts_to_remove: Incomplete
    output_artifacts_to_remove: Incomplete
    tags: Incomplete
    @classmethod
    def load(cls, trial_component_name: str, sagemaker_session: Incomplete | None = None) -> LineageTrialComponent: ...
    def pipeline_execution_arn(self) -> str: ...
    def dataset_artifacts(self, direction: LineageQueryDirectionEnum = ...) -> list[Artifact]: ...
    def models(self, direction: LineageQueryDirectionEnum = ...) -> list[Artifact]: ...
