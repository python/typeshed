from _typeshed import Incomplete
from typing import NamedTuple

class TopicPartition(NamedTuple):
    topic: Incomplete
    partition: Incomplete

class BrokerMetadata(NamedTuple):
    nodeId: Incomplete
    host: Incomplete
    port: Incomplete
    rack: Incomplete

class PartitionMetadata(NamedTuple):
    topic: Incomplete
    partition: Incomplete
    leader: Incomplete
    leader_epoch: Incomplete
    replicas: Incomplete
    isr: Incomplete
    offline_replicas: Incomplete
    error: Incomplete

class OffsetAndMetadata(NamedTuple):
    offset: Incomplete
    metadata: Incomplete
    leader_epoch: Incomplete

class OffsetAndTimestamp(NamedTuple):
    offset: Incomplete
    timestamp: Incomplete
    leader_epoch: Incomplete

class MemberInformation(NamedTuple):
    member_id: Incomplete
    client_id: Incomplete
    client_host: Incomplete
    member_metadata: Incomplete
    member_assignment: Incomplete

class GroupInformation(NamedTuple):
    error_code: Incomplete
    group: Incomplete
    state: Incomplete
    protocol_type: Incomplete
    protocol: Incomplete
    members: Incomplete
    authorized_operations: Incomplete

class RetryOptions(NamedTuple):
    limit: Incomplete
    backoff_ms: Incomplete
    retry_on_timeouts: Incomplete
