from _typeshed import Incomplete

class UnresolvableContainerID(Exception): ...

class ContainerID:
    CGROUP_PATH: str
    UUID_SOURCE: str
    CONTAINER_SOURCE: str
    TASK_SOURCE: str
    LINE_RE: Incomplete
    CONTAINER_RE: Incomplete
    container_id: Incomplete
    def __init__(self) -> None: ...
