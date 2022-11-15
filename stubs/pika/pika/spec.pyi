from _typeshed import Incomplete

from pika import amqp_object

str = bytes
PROTOCOL_VERSION: Incomplete
PORT: int
ACCESS_REFUSED: int
CHANNEL_ERROR: int
COMMAND_INVALID: int
CONNECTION_FORCED: int
CONTENT_TOO_LARGE: int
FRAME_BODY: int
FRAME_END: int
FRAME_END_SIZE: int
FRAME_ERROR: int
FRAME_HEADER: int
FRAME_HEADER_SIZE: int
FRAME_HEARTBEAT: int
FRAME_MAX_SIZE: int
FRAME_METHOD: int
FRAME_MIN_SIZE: int
INTERNAL_ERROR: int
INVALID_PATH: int
NOT_ALLOWED: int
NOT_FOUND: int
NOT_IMPLEMENTED: int
NO_CONSUMERS: int
NO_ROUTE: int
PERSISTENT_DELIVERY_MODE: int
PRECONDITION_FAILED: int
REPLY_SUCCESS: int
RESOURCE_ERROR: int
RESOURCE_LOCKED: int
SYNTAX_ERROR: int
TRANSIENT_DELIVERY_MODE: int
UNEXPECTED_FRAME: int

class Connection(amqp_object.Class):
    INDEX: int
    NAME: str

    class Start(amqp_object.Method):
        INDEX: int
        NAME: str
        version_major: Incomplete
        version_minor: Incomplete
        server_properties: Incomplete
        mechanisms: Incomplete
        locales: Incomplete
        def __init__(
            self,
            version_major: int = ...,
            version_minor: int = ...,
            server_properties: Incomplete | None = ...,
            mechanisms: str = ...,
            locales: str = ...,
        ) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class StartOk(amqp_object.Method):
        INDEX: int
        NAME: str
        client_properties: Incomplete
        mechanism: Incomplete
        response: Incomplete
        locale: Incomplete
        def __init__(
            self,
            client_properties: Incomplete | None = ...,
            mechanism: str = ...,
            response: Incomplete | None = ...,
            locale: str = ...,
        ) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class Secure(amqp_object.Method):
        INDEX: int
        NAME: str
        challenge: Incomplete
        def __init__(self, challenge: Incomplete | None = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class SecureOk(amqp_object.Method):
        INDEX: int
        NAME: str
        response: Incomplete
        def __init__(self, response: Incomplete | None = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class Tune(amqp_object.Method):
        INDEX: int
        NAME: str
        channel_max: Incomplete
        frame_max: Incomplete
        heartbeat: Incomplete
        def __init__(self, channel_max: int = ..., frame_max: int = ..., heartbeat: int = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class TuneOk(amqp_object.Method):
        INDEX: int
        NAME: str
        channel_max: Incomplete
        frame_max: Incomplete
        heartbeat: Incomplete
        def __init__(self, channel_max: int = ..., frame_max: int = ..., heartbeat: int = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class Open(amqp_object.Method):
        INDEX: int
        NAME: str
        virtual_host: Incomplete
        capabilities: Incomplete
        insist: Incomplete
        def __init__(self, virtual_host: str = ..., capabilities: str = ..., insist: bool = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class OpenOk(amqp_object.Method):
        INDEX: int
        NAME: str
        known_hosts: Incomplete
        def __init__(self, known_hosts: str = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class Close(amqp_object.Method):
        INDEX: int
        NAME: str
        reply_code: Incomplete
        reply_text: Incomplete
        class_id: Incomplete
        method_id: Incomplete
        def __init__(
            self,
            reply_code: Incomplete | None = ...,
            reply_text: str = ...,
            class_id: Incomplete | None = ...,
            method_id: Incomplete | None = ...,
        ) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class CloseOk(amqp_object.Method):
        INDEX: int
        NAME: str
        def __init__(self) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class Blocked(amqp_object.Method):
        INDEX: int
        NAME: str
        reason: Incomplete
        def __init__(self, reason: str = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class Unblocked(amqp_object.Method):
        INDEX: int
        NAME: str
        def __init__(self) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class UpdateSecret(amqp_object.Method):
        INDEX: int
        NAME: str
        new_secret: Incomplete
        reason: Incomplete
        def __init__(self, new_secret, reason) -> None: ...
        @property
        def synchronous(self): ...
        mechanisms: Incomplete
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class UpdateSecretOk(amqp_object.Method):
        INDEX: int
        NAME: str
        def __init__(self) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

class Channel(amqp_object.Class):
    INDEX: int
    NAME: str

    class Open(amqp_object.Method):
        INDEX: int
        NAME: str
        out_of_band: Incomplete
        def __init__(self, out_of_band: str = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class OpenOk(amqp_object.Method):
        INDEX: int
        NAME: str
        channel_id: Incomplete
        def __init__(self, channel_id: str = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class Flow(amqp_object.Method):
        INDEX: int
        NAME: str
        active: Incomplete
        def __init__(self, active: Incomplete | None = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class FlowOk(amqp_object.Method):
        INDEX: int
        NAME: str
        active: Incomplete
        def __init__(self, active: Incomplete | None = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class Close(amqp_object.Method):
        INDEX: int
        NAME: str
        reply_code: Incomplete
        reply_text: Incomplete
        class_id: Incomplete
        method_id: Incomplete
        def __init__(
            self,
            reply_code: Incomplete | None = ...,
            reply_text: str = ...,
            class_id: Incomplete | None = ...,
            method_id: Incomplete | None = ...,
        ) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class CloseOk(amqp_object.Method):
        INDEX: int
        NAME: str
        def __init__(self) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

class Access(amqp_object.Class):
    INDEX: int
    NAME: str

    class Request(amqp_object.Method):
        INDEX: int
        NAME: str
        realm: Incomplete
        exclusive: Incomplete
        passive: Incomplete
        active: Incomplete
        write: Incomplete
        read: Incomplete
        def __init__(
            self,
            realm: str = ...,
            exclusive: bool = ...,
            passive: bool = ...,
            active: bool = ...,
            write: bool = ...,
            read: bool = ...,
        ) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class RequestOk(amqp_object.Method):
        INDEX: int
        NAME: str
        ticket: Incomplete
        def __init__(self, ticket: int = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

class Exchange(amqp_object.Class):
    INDEX: int
    NAME: str

    class Declare(amqp_object.Method):
        INDEX: int
        NAME: str
        ticket: Incomplete
        exchange: Incomplete
        type: Incomplete
        passive: Incomplete
        durable: Incomplete
        auto_delete: Incomplete
        internal: Incomplete
        nowait: Incomplete
        arguments: Incomplete
        def __init__(
            self,
            ticket: int = ...,
            exchange: Incomplete | None = ...,
            type=...,
            passive: bool = ...,
            durable: bool = ...,
            auto_delete: bool = ...,
            internal: bool = ...,
            nowait: bool = ...,
            arguments: Incomplete | None = ...,
        ) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class DeclareOk(amqp_object.Method):
        INDEX: int
        NAME: str
        def __init__(self) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class Delete(amqp_object.Method):
        INDEX: int
        NAME: str
        ticket: Incomplete
        exchange: Incomplete
        if_unused: Incomplete
        nowait: Incomplete
        def __init__(
            self, ticket: int = ..., exchange: Incomplete | None = ..., if_unused: bool = ..., nowait: bool = ...
        ) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class DeleteOk(amqp_object.Method):
        INDEX: int
        NAME: str
        def __init__(self) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class Bind(amqp_object.Method):
        INDEX: int
        NAME: str
        ticket: Incomplete
        destination: Incomplete
        source: Incomplete
        routing_key: Incomplete
        nowait: Incomplete
        arguments: Incomplete
        def __init__(
            self,
            ticket: int = ...,
            destination: Incomplete | None = ...,
            source: Incomplete | None = ...,
            routing_key: str = ...,
            nowait: bool = ...,
            arguments: Incomplete | None = ...,
        ) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class BindOk(amqp_object.Method):
        INDEX: int
        NAME: str
        def __init__(self) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class Unbind(amqp_object.Method):
        INDEX: int
        NAME: str
        ticket: Incomplete
        destination: Incomplete
        source: Incomplete
        routing_key: Incomplete
        nowait: Incomplete
        arguments: Incomplete
        def __init__(
            self,
            ticket: int = ...,
            destination: Incomplete | None = ...,
            source: Incomplete | None = ...,
            routing_key: str = ...,
            nowait: bool = ...,
            arguments: Incomplete | None = ...,
        ) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class UnbindOk(amqp_object.Method):
        INDEX: int
        NAME: str
        def __init__(self) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

class Queue(amqp_object.Class):
    INDEX: int
    NAME: str

    class Declare(amqp_object.Method):
        INDEX: int
        NAME: str
        ticket: Incomplete
        queue: Incomplete
        passive: Incomplete
        durable: Incomplete
        exclusive: Incomplete
        auto_delete: Incomplete
        nowait: Incomplete
        arguments: Incomplete
        def __init__(
            self,
            ticket: int = ...,
            queue: str = ...,
            passive: bool = ...,
            durable: bool = ...,
            exclusive: bool = ...,
            auto_delete: bool = ...,
            nowait: bool = ...,
            arguments: Incomplete | None = ...,
        ) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class DeclareOk(amqp_object.Method):
        INDEX: int
        NAME: str
        queue: Incomplete
        message_count: Incomplete
        consumer_count: Incomplete
        def __init__(
            self, queue: Incomplete | None = ..., message_count: Incomplete | None = ..., consumer_count: Incomplete | None = ...
        ) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class Bind(amqp_object.Method):
        INDEX: int
        NAME: str
        ticket: Incomplete
        queue: Incomplete
        exchange: Incomplete
        routing_key: Incomplete
        nowait: Incomplete
        arguments: Incomplete
        def __init__(
            self,
            ticket: int = ...,
            queue: str = ...,
            exchange: Incomplete | None = ...,
            routing_key: str = ...,
            nowait: bool = ...,
            arguments: Incomplete | None = ...,
        ) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class BindOk(amqp_object.Method):
        INDEX: int
        NAME: str
        def __init__(self) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class Purge(amqp_object.Method):
        INDEX: int
        NAME: str
        ticket: Incomplete
        queue: Incomplete
        nowait: Incomplete
        def __init__(self, ticket: int = ..., queue: str = ..., nowait: bool = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class PurgeOk(amqp_object.Method):
        INDEX: int
        NAME: str
        message_count: Incomplete
        def __init__(self, message_count: Incomplete | None = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class Delete(amqp_object.Method):
        INDEX: int
        NAME: str
        ticket: Incomplete
        queue: Incomplete
        if_unused: Incomplete
        if_empty: Incomplete
        nowait: Incomplete
        def __init__(
            self, ticket: int = ..., queue: str = ..., if_unused: bool = ..., if_empty: bool = ..., nowait: bool = ...
        ) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class DeleteOk(amqp_object.Method):
        INDEX: int
        NAME: str
        message_count: Incomplete
        def __init__(self, message_count: Incomplete | None = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class Unbind(amqp_object.Method):
        INDEX: int
        NAME: str
        ticket: Incomplete
        queue: Incomplete
        exchange: Incomplete
        routing_key: Incomplete
        arguments: Incomplete
        def __init__(
            self,
            ticket: int = ...,
            queue: str = ...,
            exchange: Incomplete | None = ...,
            routing_key: str = ...,
            arguments: Incomplete | None = ...,
        ) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class UnbindOk(amqp_object.Method):
        INDEX: int
        NAME: str
        def __init__(self) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

class Basic(amqp_object.Class):
    INDEX: int
    NAME: str

    class Qos(amqp_object.Method):
        INDEX: int
        NAME: str
        prefetch_size: Incomplete
        prefetch_count: Incomplete
        global_qos: Incomplete
        def __init__(self, prefetch_size: int = ..., prefetch_count: int = ..., global_qos: bool = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class QosOk(amqp_object.Method):
        INDEX: int
        NAME: str
        def __init__(self) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class Consume(amqp_object.Method):
        INDEX: int
        NAME: str
        ticket: Incomplete
        queue: Incomplete
        consumer_tag: Incomplete
        no_local: Incomplete
        no_ack: Incomplete
        exclusive: Incomplete
        nowait: Incomplete
        arguments: Incomplete
        def __init__(
            self,
            ticket: int = ...,
            queue: str = ...,
            consumer_tag: str = ...,
            no_local: bool = ...,
            no_ack: bool = ...,
            exclusive: bool = ...,
            nowait: bool = ...,
            arguments: Incomplete | None = ...,
        ) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class ConsumeOk(amqp_object.Method):
        INDEX: int
        NAME: str
        consumer_tag: Incomplete
        def __init__(self, consumer_tag: Incomplete | None = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class Cancel(amqp_object.Method):
        INDEX: int
        NAME: str
        consumer_tag: Incomplete
        nowait: Incomplete
        def __init__(self, consumer_tag: Incomplete | None = ..., nowait: bool = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class CancelOk(amqp_object.Method):
        INDEX: int
        NAME: str
        consumer_tag: Incomplete
        def __init__(self, consumer_tag: Incomplete | None = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class Publish(amqp_object.Method):
        INDEX: int
        NAME: str
        ticket: Incomplete
        exchange: Incomplete
        routing_key: Incomplete
        mandatory: Incomplete
        immediate: Incomplete
        def __init__(
            self, ticket: int = ..., exchange: str = ..., routing_key: str = ..., mandatory: bool = ..., immediate: bool = ...
        ) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class Return(amqp_object.Method):
        INDEX: int
        NAME: str
        reply_code: Incomplete
        reply_text: Incomplete
        exchange: Incomplete
        routing_key: Incomplete
        def __init__(
            self,
            reply_code: Incomplete | None = ...,
            reply_text: str = ...,
            exchange: Incomplete | None = ...,
            routing_key: Incomplete | None = ...,
        ) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class Deliver(amqp_object.Method):
        INDEX: int
        NAME: str
        consumer_tag: Incomplete
        delivery_tag: Incomplete
        redelivered: Incomplete
        exchange: Incomplete
        routing_key: Incomplete
        def __init__(
            self,
            consumer_tag: Incomplete | None = ...,
            delivery_tag: Incomplete | None = ...,
            redelivered: bool = ...,
            exchange: Incomplete | None = ...,
            routing_key: Incomplete | None = ...,
        ) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class Get(amqp_object.Method):
        INDEX: int
        NAME: str
        ticket: Incomplete
        queue: Incomplete
        no_ack: Incomplete
        def __init__(self, ticket: int = ..., queue: str = ..., no_ack: bool = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class GetOk(amqp_object.Method):
        INDEX: int
        NAME: str
        delivery_tag: Incomplete
        redelivered: Incomplete
        exchange: Incomplete
        routing_key: Incomplete
        message_count: Incomplete
        def __init__(
            self,
            delivery_tag: Incomplete | None = ...,
            redelivered: bool = ...,
            exchange: Incomplete | None = ...,
            routing_key: Incomplete | None = ...,
            message_count: Incomplete | None = ...,
        ) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class GetEmpty(amqp_object.Method):
        INDEX: int
        NAME: str
        cluster_id: Incomplete
        def __init__(self, cluster_id: str = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class Ack(amqp_object.Method):
        INDEX: int
        NAME: str
        delivery_tag: Incomplete
        multiple: Incomplete
        def __init__(self, delivery_tag: int = ..., multiple: bool = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class Reject(amqp_object.Method):
        INDEX: int
        NAME: str
        delivery_tag: Incomplete
        requeue: Incomplete
        def __init__(self, delivery_tag: Incomplete | None = ..., requeue: bool = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class RecoverAsync(amqp_object.Method):
        INDEX: int
        NAME: str
        requeue: Incomplete
        def __init__(self, requeue: bool = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class Recover(amqp_object.Method):
        INDEX: int
        NAME: str
        requeue: Incomplete
        def __init__(self, requeue: bool = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class RecoverOk(amqp_object.Method):
        INDEX: int
        NAME: str
        def __init__(self) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class Nack(amqp_object.Method):
        INDEX: int
        NAME: str
        delivery_tag: Incomplete
        multiple: Incomplete
        requeue: Incomplete
        def __init__(self, delivery_tag: int = ..., multiple: bool = ..., requeue: bool = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

class Tx(amqp_object.Class):
    INDEX: int
    NAME: str

    class Select(amqp_object.Method):
        INDEX: int
        NAME: str
        def __init__(self) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class SelectOk(amqp_object.Method):
        INDEX: int
        NAME: str
        def __init__(self) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class Commit(amqp_object.Method):
        INDEX: int
        NAME: str
        def __init__(self) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class CommitOk(amqp_object.Method):
        INDEX: int
        NAME: str
        def __init__(self) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class Rollback(amqp_object.Method):
        INDEX: int
        NAME: str
        def __init__(self) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class RollbackOk(amqp_object.Method):
        INDEX: int
        NAME: str
        def __init__(self) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

class Confirm(amqp_object.Class):
    INDEX: int
    NAME: str

    class Select(amqp_object.Method):
        INDEX: int
        NAME: str
        nowait: Incomplete
        def __init__(self, nowait: bool = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

    class SelectOk(amqp_object.Method):
        INDEX: int
        NAME: str
        def __init__(self) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded, offset: int = ...): ...
        def encode(self): ...

class BasicProperties(amqp_object.Properties):
    CLASS: Incomplete
    INDEX: int
    NAME: str
    FLAG_CONTENT_TYPE: Incomplete
    FLAG_CONTENT_ENCODING: Incomplete
    FLAG_HEADERS: Incomplete
    FLAG_DELIVERY_MODE: Incomplete
    FLAG_PRIORITY: Incomplete
    FLAG_CORRELATION_ID: Incomplete
    FLAG_REPLY_TO: Incomplete
    FLAG_EXPIRATION: Incomplete
    FLAG_MESSAGE_ID: Incomplete
    FLAG_TIMESTAMP: Incomplete
    FLAG_TYPE: Incomplete
    FLAG_USER_ID: Incomplete
    FLAG_APP_ID: Incomplete
    FLAG_CLUSTER_ID: Incomplete
    content_type: Incomplete
    content_encoding: Incomplete
    headers: Incomplete
    delivery_mode: Incomplete
    priority: Incomplete
    correlation_id: Incomplete
    reply_to: Incomplete
    expiration: Incomplete
    message_id: Incomplete
    timestamp: Incomplete
    type: Incomplete
    user_id: Incomplete
    app_id: Incomplete
    cluster_id: Incomplete
    def __init__(
        self,
        content_type: Incomplete | None = ...,
        content_encoding: Incomplete | None = ...,
        headers: Incomplete | None = ...,
        delivery_mode: Incomplete | None = ...,
        priority: Incomplete | None = ...,
        correlation_id: Incomplete | None = ...,
        reply_to: Incomplete | None = ...,
        expiration: Incomplete | None = ...,
        message_id: Incomplete | None = ...,
        timestamp: Incomplete | None = ...,
        type: Incomplete | None = ...,
        user_id: Incomplete | None = ...,
        app_id: Incomplete | None = ...,
        cluster_id: Incomplete | None = ...,
    ) -> None: ...
    def decode(self, encoded, offset: int = ...): ...
    def encode(self): ...

methods: Incomplete
props: Incomplete

def has_content(methodNumber): ...
