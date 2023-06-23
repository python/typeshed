from _typeshed import Incomplete

from sagemaker.apiutils import _base_types

class _TrialComponent(_base_types.Record):
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
    def __init__(self, sagemaker_session: Incomplete | None = None, **kwargs) -> None: ...
    def save(self): ...
    def delete(self, force_disassociate: bool = False): ...
    @classmethod
    def load(cls, trial_component_name, sagemaker_session: Incomplete | None = None): ...
    @classmethod
    def create(
        cls,
        trial_component_name,
        display_name: Incomplete | None = None,
        tags: Incomplete | None = None,
        sagemaker_session: Incomplete | None = None,
    ): ...
    @classmethod
    def list(
        cls,
        source_arn: Incomplete | None = None,
        created_before: Incomplete | None = None,
        created_after: Incomplete | None = None,
        sort_by: Incomplete | None = None,
        sort_order: Incomplete | None = None,
        sagemaker_session: Incomplete | None = None,
        trial_name: Incomplete | None = None,
        experiment_name: Incomplete | None = None,
        max_results: Incomplete | None = None,
        next_token: Incomplete | None = None,
    ): ...
    @classmethod
    def search(
        cls,
        search_expression: Incomplete | None = None,
        sort_by: Incomplete | None = None,
        sort_order: Incomplete | None = None,
        max_results: Incomplete | None = None,
        sagemaker_session: Incomplete | None = None,
    ): ...
