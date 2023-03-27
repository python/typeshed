from _typeshed import Incomplete, Unused
from collections.abc import Generator, Sequence
from types import TracebackType
from typing import NamedTuple
from typing_extensions import Self

from ..connection import Parameters
from ..data import _ArgumentMapping
from ..exchange_type import ExchangeType
from ..spec import BasicProperties

LOGGER: Incomplete

class _CallbackResult:
    def __init__(self, value_class: Incomplete | None = None) -> None: ...
    def reset(self) -> None: ...
    def __bool__(self) -> bool: ...
    __nonzero__: Incomplete
    def __enter__(self): ...
    def __exit__(self, *args: Unused, **kwargs: Unused) -> None: ...
    def is_ready(self): ...
    @property
    def ready(self): ...
    def signal_once(self, *_args, **_kwargs) -> None: ...
    def set_value_once(self, *args, **kwargs) -> None: ...
    def append_element(self, *args, **kwargs) -> None: ...
    @property
    def value(self): ...
    @property
    def elements(self): ...

class _IoloopTimerContext:
    def __init__(self, duration, connection) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *_args: Unused, **_kwargs: Unused) -> None: ...
    def is_ready(self): ...

class _TimerEvt:
    timer_id: Incomplete
    def __init__(self, callback) -> None: ...
    def dispatch(self) -> None: ...

class _ConnectionBlockedUnblockedEvtBase:
    def __init__(self, callback, method_frame) -> None: ...
    def dispatch(self) -> None: ...

class _ConnectionBlockedEvt(_ConnectionBlockedUnblockedEvtBase): ...
class _ConnectionUnblockedEvt(_ConnectionBlockedUnblockedEvtBase): ...

class BlockingConnection:
    class _OnClosedArgs(NamedTuple):
        connection: Incomplete
        error: Incomplete

    class _OnChannelOpenedArgs(NamedTuple):
        channel: Incomplete
    def __init__(
        self, parameters: Parameters | Sequence[Parameters] | None = None, _impl_class: Incomplete | None = None
    ) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, value: BaseException | None, traceback: TracebackType | None
    ) -> None: ...
    def add_on_connection_blocked_callback(self, callback) -> None: ...
    def add_on_connection_unblocked_callback(self, callback) -> None: ...
    def call_later(self, delay, callback): ...
    def add_callback_threadsafe(self, callback) -> None: ...
    def remove_timeout(self, timeout_id) -> None: ...
    def update_secret(self, new_secret, reason) -> None: ...
    def close(self, reply_code: int = 200, reply_text: str = 'Normal shutdown') -> None: ...
    def process_data_events(self, time_limit: int = 0): ...
    def sleep(self, duration: float) -> None: ...
    def channel(self, channel_number: int | None = None) -> BlockingChannel: ...
    @property
    def is_closed(self) -> bool: ...
    @property
    def is_open(self) -> bool: ...
    @property
    def basic_nack_supported(self) -> bool: ...
    @property
    def consumer_cancel_notify_supported(self) -> bool: ...
    @property
    def exchange_exchange_bindings_supported(self) -> bool: ...
    @property
    def publisher_confirms_supported(self) -> bool: ...
    basic_nack = basic_nack_supported
    consumer_cancel_notify = consumer_cancel_notify_supported
    exchange_exchange_bindings = exchange_exchange_bindings_supported
    publisher_confirms = publisher_confirms_supported

class _ChannelPendingEvt: ...

class _ConsumerDeliveryEvt(_ChannelPendingEvt):
    method: Incomplete
    properties: Incomplete
    body: Incomplete
    def __init__(self, method, properties, body) -> None: ...

class _ConsumerCancellationEvt(_ChannelPendingEvt):
    method_frame: Incomplete
    def __init__(self, method_frame) -> None: ...
    @property
    def method(self): ...

class _ReturnedMessageEvt(_ChannelPendingEvt):
    callback: Incomplete
    channel: Incomplete
    method: Incomplete
    properties: Incomplete
    body: Incomplete
    def __init__(self, callback, channel, method, properties, body) -> None: ...
    def dispatch(self) -> None: ...

class ReturnedMessage:
    method: Incomplete
    properties: Incomplete
    body: Incomplete
    def __init__(self, method, properties, body) -> None: ...

class _ConsumerInfo:
    SETTING_UP: int
    ACTIVE: int
    TEARING_DOWN: int
    CANCELLED_BY_BROKER: int
    consumer_tag: Incomplete
    auto_ack: Incomplete
    on_message_callback: Incomplete
    alternate_event_sink: Incomplete
    state: Incomplete
    def __init__(
        self, consumer_tag, auto_ack, on_message_callback: Incomplete | None = None, alternate_event_sink: Incomplete | None = None
    ) -> None: ...
    @property
    def setting_up(self): ...
    @property
    def active(self): ...
    @property
    def tearing_down(self): ...
    @property
    def cancelled_by_broker(self): ...

class _QueueConsumerGeneratorInfo:
    params: Incomplete
    consumer_tag: Incomplete
    pending_events: Incomplete
    def __init__(self, params, consumer_tag) -> None: ...

class BlockingChannel:
    class _RxMessageArgs(NamedTuple):
        channel: Incomplete
        method: Incomplete
        properties: Incomplete
        body: Incomplete

    class _MethodFrameCallbackResultArgs(NamedTuple):
        method_frame: Incomplete

    class _OnMessageConfirmationReportArgs(NamedTuple):
        method_frame: Incomplete

    class _FlowOkCallbackResultArgs(NamedTuple):
        active: Incomplete
    def __init__(self, channel_impl, connection) -> None: ...
    def __int__(self) -> int: ...
    def __enter__(self): ...
    def __exit__(
        self, exc_type: type[BaseException] | None, value: BaseException | None, traceback: TracebackType | None
    ) -> None: ...
    @property
    def channel_number(self): ...
    @property
    def connection(self): ...
    @property
    def is_closed(self): ...
    @property
    def is_open(self): ...
    @property
    def consumer_tags(self): ...
    def close(self, reply_code: int = 0, reply_text: str = 'Normal shutdown'): ...
    def flow(self, active): ...
    def add_on_cancel_callback(self, callback) -> None: ...
    def add_on_return_callback(self, callback): ...
    def basic_consume(
        self,
        queue,
        on_message_callback,
        auto_ack: bool = False,
        exclusive: bool = False,
        consumer_tag: Incomplete | None = None,
        arguments: Incomplete | None = None,
    ): ...
    def basic_cancel(self, consumer_tag): ...
    def start_consuming(self) -> None: ...
    def stop_consuming(self, consumer_tag: Incomplete | None = None) -> None: ...
    def consume(
        self,
        queue,
        auto_ack: bool = False,
        exclusive: bool = False,
        arguments: Incomplete | None = None,
        inactivity_timeout: Incomplete | None = None,
    ) -> Generator[Incomplete, None, None]: ...
    def get_waiting_message_count(self): ...
    def cancel(self): ...
    def basic_ack(self, delivery_tag: int = 0, multiple: bool = False) -> None: ...
    def basic_nack(self, delivery_tag: int = 0, multiple: bool = False, requeue: bool = True) -> None: ...
    def basic_get(self, queue, auto_ack: bool = False): ...
    def basic_publish(
        self, exchange: str, routing_key: str, body: str | bytes, properties: BasicProperties | None = None, mandatory: bool = False
    ) -> None: ...
    def basic_qos(self, prefetch_size: int = 0, prefetch_count: int = 0, global_qos: bool = False) -> None: ...
    def basic_recover(self, requeue: bool = False) -> None: ...
    def basic_reject(self, delivery_tag: int = 0, requeue: bool = True) -> None: ...
    def confirm_delivery(self) -> None: ...
    def exchange_declare(
        self,
        exchange: str,
        exchange_type: ExchangeType | str = ...,
        passive: bool = False,
        durable: bool = False,
        auto_delete: bool = False,
        internal: bool = False,
        arguments: _ArgumentMapping | None = None,
    ): ...
    def exchange_delete(self, exchange: str | None = None, if_unused: bool = False): ...
    def exchange_bind(self, destination, source, routing_key: str = '', arguments: Incomplete | None = None): ...
    def exchange_unbind(
        self,
        destination: Incomplete | None = None,
        source: Incomplete | None = None,
        routing_key: str = '',
        arguments: Incomplete | None = None,
    ): ...
    def queue_declare(
        self,
        queue,
        passive: bool = False,
        durable: bool = False,
        exclusive: bool = False,
        auto_delete: bool = False,
        arguments: Incomplete | None = None,
    ): ...
    def queue_delete(self, queue, if_unused: bool = False, if_empty: bool = False): ...
    def queue_purge(self, queue): ...
    def queue_bind(self, queue, exchange, routing_key: Incomplete | None = None, arguments: Incomplete | None = None): ...
    def queue_unbind(
        self, queue, exchange: Incomplete | None = None, routing_key: Incomplete | None = None, arguments: Incomplete | None = None
    ): ...
    def tx_select(self): ...
    def tx_commit(self): ...
    def tx_rollback(self): ...
