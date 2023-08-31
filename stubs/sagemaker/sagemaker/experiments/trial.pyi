from _typeshed import Incomplete

from sagemaker.apiutils import _base_types

class _Trial(_base_types.Record):
    trial_name: Incomplete
    experiment_name: Incomplete
    display_name: Incomplete
    tags: Incomplete
    def save(self): ...
    def delete(self): ...
    @classmethod
    def load(cls, trial_name, sagemaker_session: Incomplete | None = None): ...
    @classmethod
    def create(
        cls,
        experiment_name,
        trial_name,
        display_name: Incomplete | None = None,
        tags: Incomplete | None = None,
        sagemaker_session: Incomplete | None = None,
    ): ...
    @classmethod
    def list(
        cls,
        experiment_name: Incomplete | None = None,
        trial_component_name: Incomplete | None = None,
        created_before: Incomplete | None = None,
        created_after: Incomplete | None = None,
        sort_by: Incomplete | None = None,
        sort_order: Incomplete | None = None,
        sagemaker_session: Incomplete | None = None,
    ): ...
    def add_trial_component(self, trial_component) -> None: ...
    def remove_trial_component(self, trial_component) -> None: ...
    def list_trial_components(
        self,
        created_before: Incomplete | None = None,
        created_after: Incomplete | None = None,
        sort_by: Incomplete | None = None,
        sort_order: Incomplete | None = None,
        max_results: Incomplete | None = None,
        next_token: Incomplete | None = None,
    ): ...
