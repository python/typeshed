from collections.abc import Iterable, Mapping
from typing import ClassVar

from google.protobuf import any_pb2, descriptor, duration_pb2, message as message, timestamp_pb2, wrappers_pb2
from google.protobuf.internal import containers, enum_type_wrapper

DESCRIPTOR: descriptor.FileDescriptor

class Channel(message.Message):
    __slots__ = ("ref", "data", "channel_ref", "subchannel_ref", "socket_ref")
    REF_FIELD_NUMBER: ClassVar[int]
    DATA_FIELD_NUMBER: ClassVar[int]
    CHANNEL_REF_FIELD_NUMBER: ClassVar[int]
    SUBCHANNEL_REF_FIELD_NUMBER: ClassVar[int]
    SOCKET_REF_FIELD_NUMBER: ClassVar[int]
    ref: ChannelRef
    data: ChannelData
    channel_ref: containers.RepeatedCompositeFieldContainer[ChannelRef]
    subchannel_ref: containers.RepeatedCompositeFieldContainer[SubchannelRef]
    socket_ref: containers.RepeatedCompositeFieldContainer[SocketRef]
    def __init__(self, ref: ChannelRef | Mapping | None = ..., data: ChannelData | Mapping | None = ..., channel_ref: Iterable[ChannelRef | Mapping] | None = ..., subchannel_ref: Iterable[SubchannelRef | Mapping] | None = ..., socket_ref: Iterable[SocketRef | Mapping] | None = ...) -> None: ...

class Subchannel(message.Message):
    __slots__ = ("ref", "data", "channel_ref", "subchannel_ref", "socket_ref")
    REF_FIELD_NUMBER: ClassVar[int]
    DATA_FIELD_NUMBER: ClassVar[int]
    CHANNEL_REF_FIELD_NUMBER: ClassVar[int]
    SUBCHANNEL_REF_FIELD_NUMBER: ClassVar[int]
    SOCKET_REF_FIELD_NUMBER: ClassVar[int]
    ref: SubchannelRef
    data: ChannelData
    channel_ref: containers.RepeatedCompositeFieldContainer[ChannelRef]
    subchannel_ref: containers.RepeatedCompositeFieldContainer[SubchannelRef]
    socket_ref: containers.RepeatedCompositeFieldContainer[SocketRef]
    def __init__(self, ref: SubchannelRef | Mapping | None = ..., data: ChannelData | Mapping | None = ..., channel_ref: Iterable[ChannelRef | Mapping] | None = ..., subchannel_ref: Iterable[SubchannelRef | Mapping] | None = ..., socket_ref: Iterable[SocketRef | Mapping] | None = ...) -> None: ...

class ChannelConnectivityState(message.Message):
    __slots__ = ("state",)
    class State(int, metaclass=enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: ClassVar[ChannelConnectivityState.State]
        IDLE: ClassVar[ChannelConnectivityState.State]
        CONNECTING: ClassVar[ChannelConnectivityState.State]
        READY: ClassVar[ChannelConnectivityState.State]
        TRANSIENT_FAILURE: ClassVar[ChannelConnectivityState.State]
        SHUTDOWN: ClassVar[ChannelConnectivityState.State]
    UNKNOWN: ChannelConnectivityState.State
    IDLE: ChannelConnectivityState.State
    CONNECTING: ChannelConnectivityState.State
    READY: ChannelConnectivityState.State
    TRANSIENT_FAILURE: ChannelConnectivityState.State
    SHUTDOWN: ChannelConnectivityState.State
    STATE_FIELD_NUMBER: ClassVar[int]
    state: ChannelConnectivityState.State
    def __init__(self, state: ChannelConnectivityState.State | str | None = ...) -> None: ...

class ChannelData(message.Message):
    __slots__ = ("state", "target", "trace", "calls_started", "calls_succeeded", "calls_failed", "last_call_started_timestamp")
    STATE_FIELD_NUMBER: ClassVar[int]
    TARGET_FIELD_NUMBER: ClassVar[int]
    TRACE_FIELD_NUMBER: ClassVar[int]
    CALLS_STARTED_FIELD_NUMBER: ClassVar[int]
    CALLS_SUCCEEDED_FIELD_NUMBER: ClassVar[int]
    CALLS_FAILED_FIELD_NUMBER: ClassVar[int]
    LAST_CALL_STARTED_TIMESTAMP_FIELD_NUMBER: ClassVar[int]
    state: ChannelConnectivityState
    target: str
    trace: ChannelTrace
    calls_started: int
    calls_succeeded: int
    calls_failed: int
    last_call_started_timestamp: timestamp_pb2.Timestamp
    def __init__(self, state: ChannelConnectivityState | Mapping | None = ..., target: str | None = ..., trace: ChannelTrace | Mapping | None = ..., calls_started: int | None = ..., calls_succeeded: int | None = ..., calls_failed: int | None = ..., last_call_started_timestamp: timestamp_pb2.Timestamp | Mapping | None = ...) -> None: ...

class ChannelTraceEvent(message.Message):
    __slots__ = ("description", "severity", "timestamp", "channel_ref", "subchannel_ref")
    class Severity(int, metaclass=enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CT_UNKNOWN: ClassVar[ChannelTraceEvent.Severity]
        CT_INFO: ClassVar[ChannelTraceEvent.Severity]
        CT_WARNING: ClassVar[ChannelTraceEvent.Severity]
        CT_ERROR: ClassVar[ChannelTraceEvent.Severity]
    CT_UNKNOWN: ChannelTraceEvent.Severity
    CT_INFO: ChannelTraceEvent.Severity
    CT_WARNING: ChannelTraceEvent.Severity
    CT_ERROR: ChannelTraceEvent.Severity
    DESCRIPTION_FIELD_NUMBER: ClassVar[int]
    SEVERITY_FIELD_NUMBER: ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: ClassVar[int]
    CHANNEL_REF_FIELD_NUMBER: ClassVar[int]
    SUBCHANNEL_REF_FIELD_NUMBER: ClassVar[int]
    description: str
    severity: ChannelTraceEvent.Severity
    timestamp: timestamp_pb2.Timestamp
    channel_ref: ChannelRef
    subchannel_ref: SubchannelRef
    def __init__(self, description: str | None = ..., severity: ChannelTraceEvent.Severity | str | None = ..., timestamp: timestamp_pb2.Timestamp | Mapping | None = ..., channel_ref: ChannelRef | Mapping | None = ..., subchannel_ref: SubchannelRef | Mapping | None = ...) -> None: ...

class ChannelTrace(message.Message):
    __slots__ = ("num_events_logged", "creation_timestamp", "events")
    NUM_EVENTS_LOGGED_FIELD_NUMBER: ClassVar[int]
    CREATION_TIMESTAMP_FIELD_NUMBER: ClassVar[int]
    EVENTS_FIELD_NUMBER: ClassVar[int]
    num_events_logged: int
    creation_timestamp: timestamp_pb2.Timestamp
    events: containers.RepeatedCompositeFieldContainer[ChannelTraceEvent]
    def __init__(self, num_events_logged: int | None = ..., creation_timestamp: timestamp_pb2.Timestamp | Mapping | None = ..., events: Iterable[ChannelTraceEvent | Mapping] | None = ...) -> None: ...

class ChannelRef(message.Message):
    __slots__ = ("channel_id", "name")
    CHANNEL_ID_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    channel_id: int
    name: str
    def __init__(self, channel_id: int | None = ..., name: str | None = ...) -> None: ...

class SubchannelRef(message.Message):
    __slots__ = ("subchannel_id", "name")
    SUBCHANNEL_ID_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    subchannel_id: int
    name: str
    def __init__(self, subchannel_id: int | None = ..., name: str | None = ...) -> None: ...

class SocketRef(message.Message):
    __slots__ = ("socket_id", "name")
    SOCKET_ID_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    socket_id: int
    name: str
    def __init__(self, socket_id: int | None = ..., name: str | None = ...) -> None: ...

class ServerRef(message.Message):
    __slots__ = ("server_id", "name")
    SERVER_ID_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    server_id: int
    name: str
    def __init__(self, server_id: int | None = ..., name: str | None = ...) -> None: ...

class Server(message.Message):
    __slots__ = ("ref", "data", "listen_socket")
    REF_FIELD_NUMBER: ClassVar[int]
    DATA_FIELD_NUMBER: ClassVar[int]
    LISTEN_SOCKET_FIELD_NUMBER: ClassVar[int]
    ref: ServerRef
    data: ServerData
    listen_socket: containers.RepeatedCompositeFieldContainer[SocketRef]
    def __init__(self, ref: ServerRef | Mapping | None = ..., data: ServerData | Mapping | None = ..., listen_socket: Iterable[SocketRef | Mapping] | None = ...) -> None: ...

class ServerData(message.Message):
    __slots__ = ("trace", "calls_started", "calls_succeeded", "calls_failed", "last_call_started_timestamp")
    TRACE_FIELD_NUMBER: ClassVar[int]
    CALLS_STARTED_FIELD_NUMBER: ClassVar[int]
    CALLS_SUCCEEDED_FIELD_NUMBER: ClassVar[int]
    CALLS_FAILED_FIELD_NUMBER: ClassVar[int]
    LAST_CALL_STARTED_TIMESTAMP_FIELD_NUMBER: ClassVar[int]
    trace: ChannelTrace
    calls_started: int
    calls_succeeded: int
    calls_failed: int
    last_call_started_timestamp: timestamp_pb2.Timestamp
    def __init__(self, trace: ChannelTrace | Mapping | None = ..., calls_started: int | None = ..., calls_succeeded: int | None = ..., calls_failed: int | None = ..., last_call_started_timestamp: timestamp_pb2.Timestamp | Mapping | None = ...) -> None: ...

class Socket(message.Message):
    __slots__ = ("ref", "data", "local", "remote", "security", "remote_name")
    REF_FIELD_NUMBER: ClassVar[int]
    DATA_FIELD_NUMBER: ClassVar[int]
    LOCAL_FIELD_NUMBER: ClassVar[int]
    REMOTE_FIELD_NUMBER: ClassVar[int]
    SECURITY_FIELD_NUMBER: ClassVar[int]
    REMOTE_NAME_FIELD_NUMBER: ClassVar[int]
    ref: SocketRef
    data: SocketData
    local: Address
    remote: Address
    security: Security
    remote_name: str
    def __init__(self, ref: SocketRef | Mapping | None = ..., data: SocketData | Mapping | None = ..., local: Address | Mapping | None = ..., remote: Address | Mapping | None = ..., security: Security | Mapping | None = ..., remote_name: str | None = ...) -> None: ...

class SocketData(message.Message):
    __slots__ = ("streams_started", "streams_succeeded", "streams_failed", "messages_sent", "messages_received", "keep_alives_sent", "last_local_stream_created_timestamp", "last_remote_stream_created_timestamp", "last_message_sent_timestamp", "last_message_received_timestamp", "local_flow_control_window", "remote_flow_control_window", "option")
    STREAMS_STARTED_FIELD_NUMBER: ClassVar[int]
    STREAMS_SUCCEEDED_FIELD_NUMBER: ClassVar[int]
    STREAMS_FAILED_FIELD_NUMBER: ClassVar[int]
    MESSAGES_SENT_FIELD_NUMBER: ClassVar[int]
    MESSAGES_RECEIVED_FIELD_NUMBER: ClassVar[int]
    KEEP_ALIVES_SENT_FIELD_NUMBER: ClassVar[int]
    LAST_LOCAL_STREAM_CREATED_TIMESTAMP_FIELD_NUMBER: ClassVar[int]
    LAST_REMOTE_STREAM_CREATED_TIMESTAMP_FIELD_NUMBER: ClassVar[int]
    LAST_MESSAGE_SENT_TIMESTAMP_FIELD_NUMBER: ClassVar[int]
    LAST_MESSAGE_RECEIVED_TIMESTAMP_FIELD_NUMBER: ClassVar[int]
    LOCAL_FLOW_CONTROL_WINDOW_FIELD_NUMBER: ClassVar[int]
    REMOTE_FLOW_CONTROL_WINDOW_FIELD_NUMBER: ClassVar[int]
    OPTION_FIELD_NUMBER: ClassVar[int]
    streams_started: int
    streams_succeeded: int
    streams_failed: int
    messages_sent: int
    messages_received: int
    keep_alives_sent: int
    last_local_stream_created_timestamp: timestamp_pb2.Timestamp
    last_remote_stream_created_timestamp: timestamp_pb2.Timestamp
    last_message_sent_timestamp: timestamp_pb2.Timestamp
    last_message_received_timestamp: timestamp_pb2.Timestamp
    local_flow_control_window: wrappers_pb2.Int64Value
    remote_flow_control_window: wrappers_pb2.Int64Value
    option: containers.RepeatedCompositeFieldContainer[SocketOption]
    def __init__(self, streams_started: int | None = ..., streams_succeeded: int | None = ..., streams_failed: int | None = ..., messages_sent: int | None = ..., messages_received: int | None = ..., keep_alives_sent: int | None = ..., last_local_stream_created_timestamp: timestamp_pb2.Timestamp | Mapping | None = ..., last_remote_stream_created_timestamp: timestamp_pb2.Timestamp | Mapping | None = ..., last_message_sent_timestamp: timestamp_pb2.Timestamp | Mapping | None = ..., last_message_received_timestamp: timestamp_pb2.Timestamp | Mapping | None = ..., local_flow_control_window: wrappers_pb2.Int64Value | Mapping | None = ..., remote_flow_control_window: wrappers_pb2.Int64Value | Mapping | None = ..., option: Iterable[SocketOption | Mapping] | None = ...) -> None: ...

class Address(message.Message):
    __slots__ = ("tcpip_address", "uds_address", "other_address")
    class TcpIpAddress(message.Message):
        __slots__ = ("ip_address", "port")
        IP_ADDRESS_FIELD_NUMBER: ClassVar[int]
        PORT_FIELD_NUMBER: ClassVar[int]
        ip_address: bytes
        port: int
        def __init__(self, ip_address: bytes | None = ..., port: int | None = ...) -> None: ...
    class UdsAddress(message.Message):
        __slots__ = ("filename",)
        FILENAME_FIELD_NUMBER: ClassVar[int]
        filename: str
        def __init__(self, filename: str | None = ...) -> None: ...
    class OtherAddress(message.Message):
        __slots__ = ("name", "value")
        NAME_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        name: str
        value: any_pb2.Any
        def __init__(self, name: str | None = ..., value: any_pb2.Any | Mapping | None = ...) -> None: ...
    TCPIP_ADDRESS_FIELD_NUMBER: ClassVar[int]
    UDS_ADDRESS_FIELD_NUMBER: ClassVar[int]
    OTHER_ADDRESS_FIELD_NUMBER: ClassVar[int]
    tcpip_address: Address.TcpIpAddress
    uds_address: Address.UdsAddress
    other_address: Address.OtherAddress
    def __init__(self, tcpip_address: Address.TcpIpAddress | Mapping | None = ..., uds_address: Address.UdsAddress | Mapping | None = ..., other_address: Address.OtherAddress | Mapping | None = ...) -> None: ...

class Security(message.Message):
    __slots__ = ("tls", "other")
    class Tls(message.Message):
        __slots__ = ("standard_name", "other_name", "local_certificate", "remote_certificate")
        STANDARD_NAME_FIELD_NUMBER: ClassVar[int]
        OTHER_NAME_FIELD_NUMBER: ClassVar[int]
        LOCAL_CERTIFICATE_FIELD_NUMBER: ClassVar[int]
        REMOTE_CERTIFICATE_FIELD_NUMBER: ClassVar[int]
        standard_name: str
        other_name: str
        local_certificate: bytes
        remote_certificate: bytes
        def __init__(self, standard_name: str | None = ..., other_name: str | None = ..., local_certificate: bytes | None = ..., remote_certificate: bytes | None = ...) -> None: ...
    class OtherSecurity(message.Message):
        __slots__ = ("name", "value")
        NAME_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        name: str
        value: any_pb2.Any
        def __init__(self, name: str | None = ..., value: any_pb2.Any | Mapping | None = ...) -> None: ...
    TLS_FIELD_NUMBER: ClassVar[int]
    OTHER_FIELD_NUMBER: ClassVar[int]
    tls: Security.Tls
    other: Security.OtherSecurity
    def __init__(self, tls: Security.Tls | Mapping | None = ..., other: Security.OtherSecurity | Mapping | None = ...) -> None: ...

class SocketOption(message.Message):
    __slots__ = ("name", "value", "additional")
    NAME_FIELD_NUMBER: ClassVar[int]
    VALUE_FIELD_NUMBER: ClassVar[int]
    ADDITIONAL_FIELD_NUMBER: ClassVar[int]
    name: str
    value: str
    additional: any_pb2.Any
    def __init__(self, name: str | None = ..., value: str | None = ..., additional: any_pb2.Any | Mapping | None = ...) -> None: ...

class SocketOptionTimeout(message.Message):
    __slots__ = ("duration",)
    DURATION_FIELD_NUMBER: ClassVar[int]
    duration: duration_pb2.Duration
    def __init__(self, duration: duration_pb2.Duration | Mapping | None = ...) -> None: ...

class SocketOptionLinger(message.Message):
    __slots__ = ("active", "duration")
    ACTIVE_FIELD_NUMBER: ClassVar[int]
    DURATION_FIELD_NUMBER: ClassVar[int]
    active: bool
    duration: duration_pb2.Duration
    def __init__(self, active: bool = ..., duration: duration_pb2.Duration | Mapping | None = ...) -> None: ...

class SocketOptionTcpInfo(message.Message):
    __slots__ = ("tcpi_state", "tcpi_ca_state", "tcpi_retransmits", "tcpi_probes", "tcpi_backoff", "tcpi_options", "tcpi_snd_wscale", "tcpi_rcv_wscale", "tcpi_rto", "tcpi_ato", "tcpi_snd_mss", "tcpi_rcv_mss", "tcpi_unacked", "tcpi_sacked", "tcpi_lost", "tcpi_retrans", "tcpi_fackets", "tcpi_last_data_sent", "tcpi_last_ack_sent", "tcpi_last_data_recv", "tcpi_last_ack_recv", "tcpi_pmtu", "tcpi_rcv_ssthresh", "tcpi_rtt", "tcpi_rttvar", "tcpi_snd_ssthresh", "tcpi_snd_cwnd", "tcpi_advmss", "tcpi_reordering")
    TCPI_STATE_FIELD_NUMBER: ClassVar[int]
    TCPI_CA_STATE_FIELD_NUMBER: ClassVar[int]
    TCPI_RETRANSMITS_FIELD_NUMBER: ClassVar[int]
    TCPI_PROBES_FIELD_NUMBER: ClassVar[int]
    TCPI_BACKOFF_FIELD_NUMBER: ClassVar[int]
    TCPI_OPTIONS_FIELD_NUMBER: ClassVar[int]
    TCPI_SND_WSCALE_FIELD_NUMBER: ClassVar[int]
    TCPI_RCV_WSCALE_FIELD_NUMBER: ClassVar[int]
    TCPI_RTO_FIELD_NUMBER: ClassVar[int]
    TCPI_ATO_FIELD_NUMBER: ClassVar[int]
    TCPI_SND_MSS_FIELD_NUMBER: ClassVar[int]
    TCPI_RCV_MSS_FIELD_NUMBER: ClassVar[int]
    TCPI_UNACKED_FIELD_NUMBER: ClassVar[int]
    TCPI_SACKED_FIELD_NUMBER: ClassVar[int]
    TCPI_LOST_FIELD_NUMBER: ClassVar[int]
    TCPI_RETRANS_FIELD_NUMBER: ClassVar[int]
    TCPI_FACKETS_FIELD_NUMBER: ClassVar[int]
    TCPI_LAST_DATA_SENT_FIELD_NUMBER: ClassVar[int]
    TCPI_LAST_ACK_SENT_FIELD_NUMBER: ClassVar[int]
    TCPI_LAST_DATA_RECV_FIELD_NUMBER: ClassVar[int]
    TCPI_LAST_ACK_RECV_FIELD_NUMBER: ClassVar[int]
    TCPI_PMTU_FIELD_NUMBER: ClassVar[int]
    TCPI_RCV_SSTHRESH_FIELD_NUMBER: ClassVar[int]
    TCPI_RTT_FIELD_NUMBER: ClassVar[int]
    TCPI_RTTVAR_FIELD_NUMBER: ClassVar[int]
    TCPI_SND_SSTHRESH_FIELD_NUMBER: ClassVar[int]
    TCPI_SND_CWND_FIELD_NUMBER: ClassVar[int]
    TCPI_ADVMSS_FIELD_NUMBER: ClassVar[int]
    TCPI_REORDERING_FIELD_NUMBER: ClassVar[int]
    tcpi_state: int
    tcpi_ca_state: int
    tcpi_retransmits: int
    tcpi_probes: int
    tcpi_backoff: int
    tcpi_options: int
    tcpi_snd_wscale: int
    tcpi_rcv_wscale: int
    tcpi_rto: int
    tcpi_ato: int
    tcpi_snd_mss: int
    tcpi_rcv_mss: int
    tcpi_unacked: int
    tcpi_sacked: int
    tcpi_lost: int
    tcpi_retrans: int
    tcpi_fackets: int
    tcpi_last_data_sent: int
    tcpi_last_ack_sent: int
    tcpi_last_data_recv: int
    tcpi_last_ack_recv: int
    tcpi_pmtu: int
    tcpi_rcv_ssthresh: int
    tcpi_rtt: int
    tcpi_rttvar: int
    tcpi_snd_ssthresh: int
    tcpi_snd_cwnd: int
    tcpi_advmss: int
    tcpi_reordering: int
    def __init__(self, tcpi_state: int | None = ..., tcpi_ca_state: int | None = ..., tcpi_retransmits: int | None = ..., tcpi_probes: int | None = ..., tcpi_backoff: int | None = ..., tcpi_options: int | None = ..., tcpi_snd_wscale: int | None = ..., tcpi_rcv_wscale: int | None = ..., tcpi_rto: int | None = ..., tcpi_ato: int | None = ..., tcpi_snd_mss: int | None = ..., tcpi_rcv_mss: int | None = ..., tcpi_unacked: int | None = ..., tcpi_sacked: int | None = ..., tcpi_lost: int | None = ..., tcpi_retrans: int | None = ..., tcpi_fackets: int | None = ..., tcpi_last_data_sent: int | None = ..., tcpi_last_ack_sent: int | None = ..., tcpi_last_data_recv: int | None = ..., tcpi_last_ack_recv: int | None = ..., tcpi_pmtu: int | None = ..., tcpi_rcv_ssthresh: int | None = ..., tcpi_rtt: int | None = ..., tcpi_rttvar: int | None = ..., tcpi_snd_ssthresh: int | None = ..., tcpi_snd_cwnd: int | None = ..., tcpi_advmss: int | None = ..., tcpi_reordering: int | None = ...) -> None: ...

class GetTopChannelsRequest(message.Message):
    __slots__ = ("start_channel_id", "max_results")
    START_CHANNEL_ID_FIELD_NUMBER: ClassVar[int]
    MAX_RESULTS_FIELD_NUMBER: ClassVar[int]
    start_channel_id: int
    max_results: int
    def __init__(self, start_channel_id: int | None = ..., max_results: int | None = ...) -> None: ...

class GetTopChannelsResponse(message.Message):
    __slots__ = ("channel", "end")
    CHANNEL_FIELD_NUMBER: ClassVar[int]
    END_FIELD_NUMBER: ClassVar[int]
    channel: containers.RepeatedCompositeFieldContainer[Channel]
    end: bool
    def __init__(self, channel: Iterable[Channel | Mapping] | None = ..., end: bool = ...) -> None: ...

class GetServersRequest(message.Message):
    __slots__ = ("start_server_id", "max_results")
    START_SERVER_ID_FIELD_NUMBER: ClassVar[int]
    MAX_RESULTS_FIELD_NUMBER: ClassVar[int]
    start_server_id: int
    max_results: int
    def __init__(self, start_server_id: int | None = ..., max_results: int | None = ...) -> None: ...

class GetServersResponse(message.Message):
    __slots__ = ("server", "end")
    SERVER_FIELD_NUMBER: ClassVar[int]
    END_FIELD_NUMBER: ClassVar[int]
    server: containers.RepeatedCompositeFieldContainer[Server]
    end: bool
    def __init__(self, server: Iterable[Server | Mapping] | None = ..., end: bool = ...) -> None: ...

class GetServerRequest(message.Message):
    __slots__ = ("server_id",)
    SERVER_ID_FIELD_NUMBER: ClassVar[int]
    server_id: int
    def __init__(self, server_id: int | None = ...) -> None: ...

class GetServerResponse(message.Message):
    __slots__ = ("server",)
    SERVER_FIELD_NUMBER: ClassVar[int]
    server: Server
    def __init__(self, server: Server | Mapping | None = ...) -> None: ...

class GetServerSocketsRequest(message.Message):
    __slots__ = ("server_id", "start_socket_id", "max_results")
    SERVER_ID_FIELD_NUMBER: ClassVar[int]
    START_SOCKET_ID_FIELD_NUMBER: ClassVar[int]
    MAX_RESULTS_FIELD_NUMBER: ClassVar[int]
    server_id: int
    start_socket_id: int
    max_results: int
    def __init__(self, server_id: int | None = ..., start_socket_id: int | None = ..., max_results: int | None = ...) -> None: ...

class GetServerSocketsResponse(message.Message):
    __slots__ = ("socket_ref", "end")
    SOCKET_REF_FIELD_NUMBER: ClassVar[int]
    END_FIELD_NUMBER: ClassVar[int]
    socket_ref: containers.RepeatedCompositeFieldContainer[SocketRef]
    end: bool
    def __init__(self, socket_ref: Iterable[SocketRef | Mapping] | None = ..., end: bool = ...) -> None: ...

class GetChannelRequest(message.Message):
    __slots__ = ("channel_id",)
    CHANNEL_ID_FIELD_NUMBER: ClassVar[int]
    channel_id: int
    def __init__(self, channel_id: int | None = ...) -> None: ...

class GetChannelResponse(message.Message):
    __slots__ = ("channel",)
    CHANNEL_FIELD_NUMBER: ClassVar[int]
    channel: Channel
    def __init__(self, channel: Channel | Mapping | None = ...) -> None: ...

class GetSubchannelRequest(message.Message):
    __slots__ = ("subchannel_id",)
    SUBCHANNEL_ID_FIELD_NUMBER: ClassVar[int]
    subchannel_id: int
    def __init__(self, subchannel_id: int | None = ...) -> None: ...

class GetSubchannelResponse(message.Message):
    __slots__ = ("subchannel",)
    SUBCHANNEL_FIELD_NUMBER: ClassVar[int]
    subchannel: Subchannel
    def __init__(self, subchannel: Subchannel | Mapping | None = ...) -> None: ...

class GetSocketRequest(message.Message):
    __slots__ = ("socket_id", "summary")
    SOCKET_ID_FIELD_NUMBER: ClassVar[int]
    SUMMARY_FIELD_NUMBER: ClassVar[int]
    socket_id: int
    summary: bool
    def __init__(self, socket_id: int | None = ..., summary: bool = ...) -> None: ...

class GetSocketResponse(message.Message):
    __slots__ = ("socket",)
    SOCKET_FIELD_NUMBER: ClassVar[int]
    socket: Socket
    def __init__(self, socket: Socket | Mapping | None = ...) -> None: ...
