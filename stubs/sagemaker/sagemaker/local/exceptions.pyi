from _typeshed import Incomplete

class StepExecutionException(Exception):
    message: Incomplete
    step_name: Incomplete
    def __init__(self, step_name, message) -> None: ...
