from _typeshed import Incomplete

class Context:
    name: Incomplete
    context_type: Incomplete
    orchestrator: Incomplete
    endpoints: Incomplete
    tls_cfg: Incomplete
    meta_path: str
    tls_path: str
    def __init__(
        self,
        name,
        orchestrator: Incomplete | None = None,
        host: Incomplete | None = None,
        endpoints: Incomplete | None = None,
        tls: bool = False,
    ) -> None: ...
    def set_endpoint(
        self,
        name: str = "docker",
        host: Incomplete | None = None,
        tls_cfg: Incomplete | None = None,
        skip_tls_verify: bool = False,
        def_namespace: Incomplete | None = None,
    ) -> None: ...
    def inspect(self): ...
    @classmethod
    def load_context(cls, name): ...
    def save(self) -> None: ...
    def remove(self) -> None: ...
    def __call__(self): ...
    def is_docker_host(self): ...
    @property
    def Name(self): ...
    @property
    def Host(self): ...
    @property
    def Orchestrator(self): ...
    @property
    def Metadata(self): ...
    @property
    def TLSConfig(self): ...
    @property
    def TLSMaterial(self): ...
    @property
    def Storage(self): ...
