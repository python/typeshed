from _typeshed import Incomplete
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

class LineageEntityEnum(Enum):
    TRIAL: str
    ACTION: str
    ARTIFACT: str
    CONTEXT: str
    TRIAL_COMPONENT: str

class LineageSourceEnum(Enum):
    CHECKPOINT: str
    DATASET: str
    ENDPOINT: str
    IMAGE: str
    MODEL: str
    MODEL_DATA: str
    MODEL_DEPLOYMENT: str
    MODEL_GROUP: str
    MODEL_REPLACE: str
    TENSORBOARD: str
    TRAINING_JOB: str
    APPROVAL: str
    PROCESSING_JOB: str
    TRANSFORM_JOB: str

class LineageQueryDirectionEnum(Enum):
    BOTH: str
    ASCENDANTS: str
    DESCENDANTS: str

class Edge:
    source_arn: Incomplete
    destination_arn: Incomplete
    association_type: Incomplete
    def __init__(self, source_arn: str, destination_arn: str, association_type: str) -> None: ...
    def __hash__(self): ...
    def __eq__(self, other): ...

class Vertex:
    arn: Incomplete
    lineage_entity: Incomplete
    lineage_source: Incomplete
    def __init__(self, arn: str, lineage_entity: str, lineage_source: str, sagemaker_session) -> None: ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def to_lineage_object(self): ...

class PyvisVisualizer:
    graph_styles: Incomplete
    def __init__(self, graph_styles, pyvis_options: Optional[Dict[str, Any]] = None) -> None: ...
    def render(self, elements, path: str = "lineage_graph_pyvis.html"): ...

class LineageQueryResult:
    edges: Incomplete
    vertices: Incomplete
    startarn: Incomplete
    def __init__(self, edges: List[Edge] = None, vertices: List[Vertex] = None, startarn: List[str] = None) -> None: ...
    def visualize(self, path: Optional[str] = "lineage_graph_pyvis.html", pyvis_options: Optional[Dict[str, Any]] = None): ...

class LineageFilter:
    entities: Incomplete
    sources: Incomplete
    created_before: Incomplete
    created_after: Incomplete
    modified_before: Incomplete
    modified_after: Incomplete
    properties: Incomplete
    def __init__(
        self,
        entities: Optional[List[LineageEntityEnum | str]] = None,
        sources: Optional[List[LineageSourceEnum | str]] = None,
        created_before: Optional[datetime] = None,
        created_after: Optional[datetime] = None,
        modified_before: Optional[datetime] = None,
        modified_after: Optional[datetime] = None,
        properties: Optional[Dict[str, str]] = None,
    ) -> None: ...

class LineageQuery:
    def __init__(self, sagemaker_session) -> None: ...
    def query(
        self,
        start_arns: List[str],
        direction: LineageQueryDirectionEnum = ...,
        include_edges: bool = True,
        query_filter: LineageFilter = None,
        max_depth: int = 10,
    ) -> LineageQueryResult: ...
