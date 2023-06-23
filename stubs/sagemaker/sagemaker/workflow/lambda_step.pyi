from _typeshed import Incomplete
from enum import Enum
from typing import Dict, List, Optional, Union

from sagemaker.lambda_helper import Lambda
from sagemaker.workflow.entities import DefaultEnumMeta, RequestType as RequestType
from sagemaker.workflow.step_collections import StepCollection
from sagemaker.workflow.steps import CacheConfig, Step

class LambdaOutputTypeEnum(Enum, metaclass=DefaultEnumMeta):
    String: str
    Integer: str
    Boolean: str
    Float: str

class LambdaOutput:
    output_name: str
    output_type: LambdaOutputTypeEnum
    def to_request(self) -> RequestType: ...
    def expr(self, step_name) -> Dict[str, str]: ...
    def __init__(self, output_name, output_type) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class LambdaStep(Step):
    lambda_func: Incomplete
    outputs: Incomplete
    cache_config: Incomplete
    inputs: Incomplete
    def __init__(
        self,
        name: str,
        lambda_func: Lambda,
        display_name: str = None,
        description: str = None,
        inputs: dict = None,
        outputs: List[LambdaOutput] = None,
        cache_config: CacheConfig = None,
        depends_on: Optional[List[Union[str, Step, StepCollection]]] = None,
    ) -> None: ...
    @property
    def arguments(self) -> RequestType: ...
    @property
    def properties(self): ...
    def to_request(self) -> RequestType: ...
