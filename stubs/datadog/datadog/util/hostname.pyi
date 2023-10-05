from _typeshed import Incomplete

VALID_HOSTNAME_RFC_1123_PATTERN: Incomplete
MAX_HOSTNAME_LEN: int
log: Incomplete

def is_valid_hostname(hostname): ...
def get_hostname(hostname_from_config: bool) -> str | None: ...
def get_ec2_instance_id(): ...

class GCE:
    URL: str
    TIMEOUT: float
    SOURCE_TYPE_NAME: str
    metadata: Incomplete
    @staticmethod
    def get_hostname(agentConfig): ...

class EC2:
    URL: str
    TIMEOUT: float
    metadata: dict[str, str]
    @staticmethod
    def get_tags(agentConfig): ...
    @staticmethod
    def get_metadata(agentConfig): ...
    @staticmethod
    def get_instance_id(agentConfig): ...
