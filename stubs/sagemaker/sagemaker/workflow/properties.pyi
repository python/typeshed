from _typeshed import Incomplete
from abc import ABCMeta
from typing import Dict, List, Union

from sagemaker.workflow.entities import Expression, PipelineVariable

class PropertiesMeta(ABCMeta):
    def __new__(mcs, *args, **kwargs): ...

class Properties(PipelineVariable, metaclass=PropertiesMeta):
    step_name: Incomplete
    path: Incomplete
    def __init__(
        self,
        step_name: str,
        path: str = None,
        shape_name: str = None,
        shape_names: List[str] = None,
        service_name: str = "sagemaker",
    ) -> None: ...
    @property
    def expr(self): ...

class PropertiesList(Properties):
    shape_name: Incomplete
    service_name: Incomplete
    def __init__(self, step_name: str, path: str, shape_name: str = None, service_name: str = "sagemaker") -> None: ...
    def __getitem__(self, item: int | str): ...

class PropertiesMap(Properties):
    shape_name: Incomplete
    service_name: Incomplete
    def __init__(self, step_name: str, path: str, shape_name: str = None, service_name: str = "sagemaker") -> None: ...
    def __getitem__(self, item: int | str): ...

class PropertyFile(Expression):
    name: str
    output_name: str
    path: str
    @property
    def expr(self) -> Dict[str, str]: ...
    def __init__(self, name, output_name, path) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
