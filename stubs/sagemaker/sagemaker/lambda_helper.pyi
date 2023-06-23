from _typeshed import Incomplete

from sagemaker.session import Session

class Lambda:
    function_arn: Incomplete
    function_name: Incomplete
    zipped_code_dir: Incomplete
    s3_bucket: Incomplete
    script: Incomplete
    handler: Incomplete
    execution_role_arn: Incomplete
    session: Incomplete
    timeout: Incomplete
    memory_size: Incomplete
    runtime: Incomplete
    vpc_config: Incomplete
    environment: Incomplete
    layers: Incomplete
    def __init__(
        self,
        function_arn: str = None,
        function_name: str = None,
        execution_role_arn: str = None,
        zipped_code_dir: str = None,
        s3_bucket: str = None,
        script: str = None,
        handler: str = None,
        session: Session = None,
        timeout: int = 120,
        memory_size: int = 128,
        runtime: str = "python3.8",
        vpc_config: dict = None,
        environment: dict = None,
        layers: list = None,
    ) -> None: ...
    def create(self): ...
    def update(self): ...
    def upsert(self): ...
    def invoke(self): ...
    def delete(self): ...
