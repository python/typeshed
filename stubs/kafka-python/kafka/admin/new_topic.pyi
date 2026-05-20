from _typeshed import Incomplete

class NewTopic:
    name: Incomplete
    num_partitions: Incomplete
    replication_factor: Incomplete
    replica_assignments: Incomplete
    topic_configs: Incomplete
    def __init__(
        self, name, num_partitions: int = -1, replication_factor: int = -1, replica_assignments=None, topic_configs=None
    ) -> None: ...
