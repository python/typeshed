from _typeshed import Incomplete

class CandidateEstimator:
    name: Incomplete
    containers: Incomplete
    steps: Incomplete
    sagemaker_session: Incomplete
    def __init__(self, candidate, sagemaker_session: Incomplete | None = None) -> None: ...
    def get_steps(self): ...
    def fit(
        self,
        inputs,
        candidate_name: Incomplete | None = None,
        volume_kms_key: Incomplete | None = None,
        encrypt_inter_container_traffic: Incomplete | None = None,
        vpc_config: Incomplete | None = None,
        wait: bool = True,
        logs: bool = True,
    ) -> None: ...

class CandidateStep:
    def __init__(self, name, inputs, step_type, description) -> None: ...
    @property
    def name(self): ...
    @property
    def inputs(self): ...
    @property
    def type(self): ...
    @property
    def description(self): ...
