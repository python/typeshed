from _typeshed import Incomplete
from typing import Union

from sagemaker.workflow.entities import PipelineVariable

class ParameterRange:
    __all_types__: Incomplete
    min_value: Incomplete
    max_value: Incomplete
    scaling_type: Incomplete
    def __init__(
        self,
        min_value: Union[int, float, PipelineVariable],
        max_value: Union[int, float, PipelineVariable],
        scaling_type: Union[str, PipelineVariable] = "Auto",
    ) -> None: ...
    def is_valid(self, value): ...
    @classmethod
    def cast_to_type(cls, value): ...
    def as_tuning_range(self, name): ...

class ContinuousParameter(ParameterRange):
    __name__: str
    @classmethod
    def cast_to_type(cls, value): ...

class CategoricalParameter(ParameterRange):
    __name__: str
    values: Incomplete
    def __init__(self, values) -> None: ...
    def as_tuning_range(self, name): ...
    def as_json_range(self, name): ...
    def is_valid(self, value): ...
    @classmethod
    def cast_to_type(cls, value): ...

class IntegerParameter(ParameterRange):
    __name__: str
    @classmethod
    def cast_to_type(cls, value): ...
