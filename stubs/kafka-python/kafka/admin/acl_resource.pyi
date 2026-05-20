from _typeshed import Incomplete
from enum import IntEnum

class ResourceType(IntEnum):
    UNKNOWN = 0
    ANY = 1
    CLUSTER = 4
    DELEGATION_TOKEN = 6
    GROUP = 3
    TOPIC = 2
    TRANSACTIONAL_ID = 5

class ACLOperation(IntEnum):
    UNKNOWN = 0
    ANY = 1
    ALL = 2
    READ = 3
    WRITE = 4
    CREATE = 5
    DELETE = 6
    ALTER = 7
    DESCRIBE = 8
    CLUSTER_ACTION = 9
    DESCRIBE_CONFIGS = 10
    ALTER_CONFIGS = 11
    IDEMPOTENT_WRITE = 12
    CREATE_TOKENS = 13
    DESCRIBE_TOKENS = 13

class ACLPermissionType(IntEnum):
    UNKNOWN = 0
    ANY = 1
    DENY = 2
    ALLOW = 3

class ACLResourcePatternType(IntEnum):
    UNKNOWN = 0
    ANY = 1
    MATCH = 2
    LITERAL = 3
    PREFIXED = 4

class ACLFilter:
    principal: Incomplete
    host: Incomplete
    operation: Incomplete
    permission_type: Incomplete
    resource_pattern: Incomplete
    def __init__(self, principal, host, operation, permission_type, resource_pattern) -> None: ...
    def validate(self) -> None: ...
    def __eq__(self, other): ...
    def __hash__(self): ...

class ACL(ACLFilter):
    def __init__(self, principal, host, operation, permission_type, resource_pattern) -> None: ...
    def validate(self) -> None: ...

class ResourcePatternFilter:
    resource_type: Incomplete
    resource_name: Incomplete
    pattern_type: Incomplete
    def __init__(self, resource_type, resource_name, pattern_type) -> None: ...
    def validate(self) -> None: ...
    def __eq__(self, other): ...
    def __hash__(self): ...

class ResourcePattern(ResourcePatternFilter):
    def __init__(self, resource_type, resource_name, pattern_type=...) -> None: ...
    def validate(self) -> None: ...

def valid_acl_operations(int_vals): ...
