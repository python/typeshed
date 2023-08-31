from _typeshed import Incomplete

from sagemaker.apiutils import _base_types

class Experiment(_base_types.Record):
    experiment_name: Incomplete
    display_name: Incomplete
    description: Incomplete
    tags: Incomplete
    def save(self): ...
    def delete(self): ...
    @classmethod
    def load(cls, experiment_name, sagemaker_session: Incomplete | None = None): ...
    @classmethod
    def create(
        cls,
        experiment_name,
        display_name: Incomplete | None = None,
        description: Incomplete | None = None,
        tags: Incomplete | None = None,
        sagemaker_session: Incomplete | None = None,
    ): ...
    def list_trials(
        self,
        created_before: Incomplete | None = None,
        created_after: Incomplete | None = None,
        sort_by: Incomplete | None = None,
        sort_order: Incomplete | None = None,
    ): ...
