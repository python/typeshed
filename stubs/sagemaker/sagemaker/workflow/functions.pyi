from sagemaker.workflow.entities import PipelineVariable
from sagemaker.workflow.properties import PropertyFile

class Join(PipelineVariable):
    on: str
    values: list
    def to_string(self) -> PipelineVariable: ...
    @property
    def expr(self): ...
    def __init__(self, on, values) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class JsonGet(PipelineVariable):
    step_name: str
    property_file: PropertyFile | str
    json_path: str
    @property
    def expr(self): ...
    def __init__(self, step_name, property_file, json_path) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
