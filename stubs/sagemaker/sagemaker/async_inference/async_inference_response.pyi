from _typeshed import Incomplete

class AsyncInferenceResponse:
    predictor_async: Incomplete
    output_path: Incomplete
    failure_path: Incomplete
    def __init__(self, predictor_async, output_path, failure_path) -> None: ...
    def get_result(self, waiter_config: Incomplete | None = None): ...
