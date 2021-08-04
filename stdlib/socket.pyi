# Ideally, we'd just do "from _socket import *". Unfortunately, socket
# overrides some definitions from _socket incompatibly. mypy incorrectly
# prefers the definitions from _socket over those defined here.
import _socket
import sys
from _socket import _FD
from _socket import CMSG_LEN as CMSG_LEN
from _socket import CMSG_SPACE as CMSG_SPACE
from _socket import EAI_ADDRFAMILY as EAI_ADDRFAMILY
from _socket import EAI_AGAIN as EAI_AGAIN
from _socket import EAI_BADFLAGS as EAI_BADFLAGS
from _socket import EAI_BADHINTS as EAI_BADHINTS
from _socket import EAI_FAIL as EAI_FAIL
from _socket import EAI_FAMILY as EAI_FAMILY
from _socket import EAI_MAX as EAI_MAX
from _socket import EAI_MEMORY as EAI_MEMORY
from _socket import EAI_NODATA as EAI_NODATA
from _socket import EAI_NONAME as EAI_NONAME
from _socket import EAI_OVERFLOW as EAI_OVERFLOW
from _socket import EAI_PROTOCOL as EAI_PROTOCOL
from _socket import EAI_SERVICE as EAI_SERVICE
from _socket import EAI_SOCKTYPE as EAI_SOCKTYPE
from _socket import EAI_SYSTEM as EAI_SYSTEM
from _socket import INADDR_ALLHOSTS_GROUP as INADDR_ALLHOSTS_GROUP
from _socket import INADDR_ANY as INADDR_ANY
from _socket import INADDR_BROADCAST as INADDR_BROADCAST
from _socket import INADDR_LOOPBACK as INADDR_LOOPBACK
from _socket import INADDR_MAX_LOCAL_GROUP as INADDR_MAX_LOCAL_GROUP
from _socket import INADDR_NONE as INADDR_NONE
from _socket import INADDR_UNSPEC_GROUP as INADDR_UNSPEC_GROUP
from _socket import IP_ADD_MEMBERSHIP as IP_ADD_MEMBERSHIP
from _socket import IP_DEFAULT_MULTICAST_LOOP as IP_DEFAULT_MULTICAST_LOOP
from _socket import IP_DEFAULT_MULTICAST_TTL as IP_DEFAULT_MULTICAST_TTL
from _socket import IP_DROP_MEMBERSHIP as IP_DROP_MEMBERSHIP
from _socket import IP_HDRINCL as IP_HDRINCL
from _socket import IP_MAX_MEMBERSHIPS as IP_MAX_MEMBERSHIPS
from _socket import IP_MULTICAST_IF as IP_MULTICAST_IF
from _socket import IP_MULTICAST_LOOP as IP_MULTICAST_LOOP
from _socket import IP_MULTICAST_TTL as IP_MULTICAST_TTL
from _socket import IP_OPTIONS as IP_OPTIONS
from _socket import IP_RECVDSTADDR as IP_RECVDSTADDR
from _socket import IP_RECVOPTS as IP_RECVOPTS
from _socket import IP_RECVRETOPTS as IP_RECVRETOPTS
from _socket import IP_RETOPTS as IP_RETOPTS
from _socket import IP_TOS as IP_TOS
from _socket import IP_TRANSPARENT as IP_TRANSPARENT
from _socket import IP_TTL as IP_TTL
from _socket import IPPORT_RESERVED as IPPORT_RESERVED
from _socket import IPPORT_USERRESERVED as IPPORT_USERRESERVED
from _socket import IPPROTO_AH as IPPROTO_AH
from _socket import IPPROTO_BIP as IPPROTO_BIP
from _socket import IPPROTO_DSTOPTS as IPPROTO_DSTOPTS
from _socket import IPPROTO_EGP as IPPROTO_EGP
from _socket import IPPROTO_EON as IPPROTO_EON
from _socket import IPPROTO_ESP as IPPROTO_ESP
from _socket import IPPROTO_FRAGMENT as IPPROTO_FRAGMENT
from _socket import IPPROTO_GGP as IPPROTO_GGP
from _socket import IPPROTO_GRE as IPPROTO_GRE
from _socket import IPPROTO_HELLO as IPPROTO_HELLO
from _socket import IPPROTO_HOPOPTS as IPPROTO_HOPOPTS
from _socket import IPPROTO_ICMP as IPPROTO_ICMP
from _socket import IPPROTO_ICMPV6 as IPPROTO_ICMPV6
from _socket import IPPROTO_IDP as IPPROTO_IDP
from _socket import IPPROTO_IGMP as IPPROTO_IGMP
from _socket import IPPROTO_IP as IPPROTO_IP
from _socket import IPPROTO_IPCOMP as IPPROTO_IPCOMP
from _socket import IPPROTO_IPIP as IPPROTO_IPIP
from _socket import IPPROTO_IPV4 as IPPROTO_IPV4
from _socket import IPPROTO_IPV6 as IPPROTO_IPV6
from _socket import IPPROTO_MAX as IPPROTO_MAX
from _socket import IPPROTO_MOBILE as IPPROTO_MOBILE
from _socket import IPPROTO_ND as IPPROTO_ND
from _socket import IPPROTO_NONE as IPPROTO_NONE
from _socket import IPPROTO_PIM as IPPROTO_PIM
from _socket import IPPROTO_PUP as IPPROTO_PUP
from _socket import IPPROTO_RAW as IPPROTO_RAW
from _socket import IPPROTO_ROUTING as IPPROTO_ROUTING
from _socket import IPPROTO_RSVP as IPPROTO_RSVP
from _socket import IPPROTO_SCTP as IPPROTO_SCTP
from _socket import IPPROTO_TCP as IPPROTO_TCP
from _socket import IPPROTO_TP as IPPROTO_TP
from _socket import IPPROTO_UDP as IPPROTO_UDP
from _socket import IPPROTO_VRRP as IPPROTO_VRRP
from _socket import IPPROTO_XTP as IPPROTO_XTP
from _socket import IPV6_CHECKSUM as IPV6_CHECKSUM
from _socket import IPV6_DONTFRAG as IPV6_DONTFRAG
from _socket import IPV6_DSTOPTS as IPV6_DSTOPTS
from _socket import IPV6_HOPLIMIT as IPV6_HOPLIMIT
from _socket import IPV6_HOPOPTS as IPV6_HOPOPTS
from _socket import IPV6_JOIN_GROUP as IPV6_JOIN_GROUP
from _socket import IPV6_LEAVE_GROUP as IPV6_LEAVE_GROUP
from _socket import IPV6_MULTICAST_HOPS as IPV6_MULTICAST_HOPS
from _socket import IPV6_MULTICAST_IF as IPV6_MULTICAST_IF
from _socket import IPV6_MULTICAST_LOOP as IPV6_MULTICAST_LOOP
from _socket import IPV6_NEXTHOP as IPV6_NEXTHOP
from _socket import IPV6_PATHMTU as IPV6_PATHMTU
from _socket import IPV6_PKTINFO as IPV6_PKTINFO
from _socket import IPV6_RECVDSTOPTS as IPV6_RECVDSTOPTS
from _socket import IPV6_RECVHOPLIMIT as IPV6_RECVHOPLIMIT
from _socket import IPV6_RECVHOPOPTS as IPV6_RECVHOPOPTS
from _socket import IPV6_RECVPATHMTU as IPV6_RECVPATHMTU
from _socket import IPV6_RECVPKTINFO as IPV6_RECVPKTINFO
from _socket import IPV6_RECVRTHDR as IPV6_RECVRTHDR
from _socket import IPV6_RECVTCLASS as IPV6_RECVTCLASS
from _socket import IPV6_RTHDR as IPV6_RTHDR
from _socket import IPV6_RTHDR_TYPE_0 as IPV6_RTHDR_TYPE_0
from _socket import IPV6_RTHDRDSTOPTS as IPV6_RTHDRDSTOPTS
from _socket import IPV6_TCLASS as IPV6_TCLASS
from _socket import IPV6_UNICAST_HOPS as IPV6_UNICAST_HOPS
from _socket import IPV6_USE_MIN_MTU as IPV6_USE_MIN_MTU
from _socket import IPV6_V6ONLY as IPV6_V6ONLY
from _socket import IPX_TYPE as IPX_TYPE
from _socket import LOCAL_PEERCRED as LOCAL_PEERCRED
from _socket import NI_DGRAM as NI_DGRAM
from _socket import NI_MAXHOST as NI_MAXHOST
from _socket import NI_MAXSERV as NI_MAXSERV
from _socket import NI_NAMEREQD as NI_NAMEREQD
from _socket import NI_NOFQDN as NI_NOFQDN
from _socket import NI_NUMERICHOST as NI_NUMERICHOST
from _socket import NI_NUMERICSERV as NI_NUMERICSERV
from _socket import SCM_CREDENTIALS as SCM_CREDENTIALS
from _socket import SCM_CREDS as SCM_CREDS
from _socket import SCM_RIGHTS as SCM_RIGHTS
from _socket import SHUT_RD as SHUT_RD
from _socket import SHUT_RDWR as SHUT_RDWR
from _socket import SHUT_WR as SHUT_WR
from _socket import SO_ACCEPTCONN as SO_ACCEPTCONN
from _socket import SO_BINDTODEVICE as SO_BINDTODEVICE
from _socket import SO_BROADCAST as SO_BROADCAST
from _socket import SO_DEBUG as SO_DEBUG
from _socket import SO_DONTROUTE as SO_DONTROUTE
from _socket import SO_ERROR as SO_ERROR
from _socket import SO_EXCLUSIVEADDRUSE as SO_EXCLUSIVEADDRUSE
from _socket import SO_KEEPALIVE as SO_KEEPALIVE
from _socket import SO_LINGER as SO_LINGER
from _socket import SO_MARK as SO_MARK
from _socket import SO_OOBINLINE as SO_OOBINLINE
from _socket import SO_PASSCRED as SO_PASSCRED
from _socket import SO_PEERCRED as SO_PEERCRED
from _socket import SO_PRIORITY as SO_PRIORITY
from _socket import SO_RCVBUF as SO_RCVBUF
from _socket import SO_RCVLOWAT as SO_RCVLOWAT
from _socket import SO_RCVTIMEO as SO_RCVTIMEO
from _socket import SO_REUSEADDR as SO_REUSEADDR
from _socket import SO_REUSEPORT as SO_REUSEPORT
from _socket import SO_SETFIB as SO_SETFIB
from _socket import SO_SNDBUF as SO_SNDBUF
from _socket import SO_SNDLOWAT as SO_SNDLOWAT
from _socket import SO_SNDTIMEO as SO_SNDTIMEO
from _socket import SO_TYPE as SO_TYPE
from _socket import SO_USELOOPBACK as SO_USELOOPBACK
from _socket import SOL_ATALK as SOL_ATALK
from _socket import SOL_AX25 as SOL_AX25
from _socket import SOL_HCI as SOL_HCI
from _socket import SOL_IP as SOL_IP
from _socket import SOL_IPX as SOL_IPX
from _socket import SOL_NETROM as SOL_NETROM
from _socket import SOL_ROSE as SOL_ROSE
from _socket import SOL_SOCKET as SOL_SOCKET
from _socket import SOL_TCP as SOL_TCP
from _socket import SOL_UDP as SOL_UDP
from _socket import SOMAXCONN as SOMAXCONN
from _socket import TCP_CORK as TCP_CORK
from _socket import TCP_DEFER_ACCEPT as TCP_DEFER_ACCEPT
from _socket import TCP_FASTOPEN as TCP_FASTOPEN
from _socket import TCP_INFO as TCP_INFO
from _socket import TCP_KEEPCNT as TCP_KEEPCNT
from _socket import TCP_KEEPIDLE as TCP_KEEPIDLE
from _socket import TCP_KEEPINTVL as TCP_KEEPINTVL
from _socket import TCP_LINGER2 as TCP_LINGER2
from _socket import TCP_MAXSEG as TCP_MAXSEG
from _socket import TCP_NODELAY as TCP_NODELAY
from _socket import TCP_QUICKACK as TCP_QUICKACK
from _socket import TCP_SYNCNT as TCP_SYNCNT
from _socket import TCP_WINDOW_CLAMP as TCP_WINDOW_CLAMP
from _socket import SocketType as SocketType
from _socket import _Address as _Address
from _socket import _RetAddress as _RetAddress
from _socket import dup as dup
from _socket import error as error
from _socket import gaierror as gaierror
from _socket import getdefaulttimeout as getdefaulttimeout
from _socket import gethostbyaddr as gethostbyaddr
from _socket import gethostbyname as gethostbyname
from _socket import gethostbyname_ex as gethostbyname_ex
from _socket import gethostname as gethostname
from _socket import getnameinfo as getnameinfo
from _socket import getprotobyname as getprotobyname
from _socket import getservbyname as getservbyname
from _socket import getservbyport as getservbyport
from _socket import has_ipv6 as has_ipv6
from _socket import herror as herror
from _socket import htonl as htonl
from _socket import htons as htons
from _socket import inet_aton as inet_aton
from _socket import inet_ntoa as inet_ntoa
from _socket import inet_ntop as inet_ntop
from _socket import inet_pton as inet_pton
from _socket import ntohl as ntohl
from _socket import ntohs as ntohs
from _socket import setdefaulttimeout as setdefaulttimeout
from _socket import timeout as timeout
from collections.abc import Iterable
from enum import IntEnum, IntFlag
from io import RawIOBase
from typing import Any, BinaryIO, Optional, TextIO, TypeVar, Union, overload

from typing_extensions import Literal

from _typeshed import ReadableBuffer, Self, WriteableBuffer

if sys.version_info >= (3, 7):
    from _socket import close as close
if sys.platform != "win32":
    from _socket import sethostname as sethostname
if sys.platform != "win32" or sys.version_info >= (3, 8):
    from _socket import if_indextoname as if_indextoname, if_nameindex as if_nameindex, if_nametoindex as if_nametoindex
if sys.platform == "linux":
    from _socket import (
        ALG_OP_DECRYPT as ALG_OP_DECRYPT,
        ALG_OP_ENCRYPT as ALG_OP_ENCRYPT,
        ALG_OP_SIGN as ALG_OP_SIGN,
        ALG_OP_VERIFY as ALG_OP_VERIFY,
        ALG_SET_AEAD_ASSOCLEN as ALG_SET_AEAD_ASSOCLEN,
        ALG_SET_AEAD_AUTHSIZE as ALG_SET_AEAD_AUTHSIZE,
        ALG_SET_IV as ALG_SET_IV,
        ALG_SET_KEY as ALG_SET_KEY,
        ALG_SET_OP as ALG_SET_OP,
        ALG_SET_PUBKEY as ALG_SET_PUBKEY,
        CAN_BCM as CAN_BCM,
        CAN_BCM_RX_CHANGED as CAN_BCM_RX_CHANGED,
        CAN_BCM_RX_DELETE as CAN_BCM_RX_DELETE,
        CAN_BCM_RX_READ as CAN_BCM_RX_READ,
        CAN_BCM_RX_SETUP as CAN_BCM_RX_SETUP,
        CAN_BCM_RX_STATUS as CAN_BCM_RX_STATUS,
        CAN_BCM_RX_TIMEOUT as CAN_BCM_RX_TIMEOUT,
        CAN_BCM_TX_DELETE as CAN_BCM_TX_DELETE,
        CAN_BCM_TX_EXPIRED as CAN_BCM_TX_EXPIRED,
        CAN_BCM_TX_READ as CAN_BCM_TX_READ,
        CAN_BCM_TX_SEND as CAN_BCM_TX_SEND,
        CAN_BCM_TX_SETUP as CAN_BCM_TX_SETUP,
        CAN_BCM_TX_STATUS as CAN_BCM_TX_STATUS,
        CAN_EFF_FLAG as CAN_EFF_FLAG,
        CAN_EFF_MASK as CAN_EFF_MASK,
        CAN_ERR_FLAG as CAN_ERR_FLAG,
        CAN_ERR_MASK as CAN_ERR_MASK,
        CAN_RAW as CAN_RAW,
        CAN_RAW_ERR_FILTER as CAN_RAW_ERR_FILTER,
        CAN_RAW_FD_FRAMES as CAN_RAW_FD_FRAMES,
        CAN_RAW_FILTER as CAN_RAW_FILTER,
        CAN_RAW_LOOPBACK as CAN_RAW_LOOPBACK,
        CAN_RAW_RECV_OWN_MSGS as CAN_RAW_RECV_OWN_MSGS,
        CAN_RTR_FLAG as CAN_RTR_FLAG,
        CAN_SFF_MASK as CAN_SFF_MASK,
        PACKET_BROADCAST as PACKET_BROADCAST,
        PACKET_FASTROUTE as PACKET_FASTROUTE,
        PACKET_HOST as PACKET_HOST,
        PACKET_LOOPBACK as PACKET_LOOPBACK,
        PACKET_MULTICAST as PACKET_MULTICAST,
        PACKET_OTHERHOST as PACKET_OTHERHOST,
        PACKET_OUTGOING as PACKET_OUTGOING,
        PF_CAN as PF_CAN,
        PF_PACKET as PF_PACKET,
        PF_RDS as PF_RDS,
        RDS_CANCEL_SENT_TO as RDS_CANCEL_SENT_TO,
        RDS_CMSG_RDMA_ARGS as RDS_CMSG_RDMA_ARGS,
        RDS_CMSG_RDMA_DEST as RDS_CMSG_RDMA_DEST,
        RDS_CMSG_RDMA_MAP as RDS_CMSG_RDMA_MAP,
        RDS_CMSG_RDMA_STATUS as RDS_CMSG_RDMA_STATUS,
        RDS_CMSG_RDMA_UPDATE as RDS_CMSG_RDMA_UPDATE,
        RDS_CONG_MONITOR as RDS_CONG_MONITOR,
        RDS_FREE_MR as RDS_FREE_MR,
        RDS_GET_MR as RDS_GET_MR,
        RDS_GET_MR_FOR_DEST as RDS_GET_MR_FOR_DEST,
        RDS_RDMA_DONTWAIT as RDS_RDMA_DONTWAIT,
        RDS_RDMA_FENCE as RDS_RDMA_FENCE,
        RDS_RDMA_INVALIDATE as RDS_RDMA_INVALIDATE,
        RDS_RDMA_NOTIFY_ME as RDS_RDMA_NOTIFY_ME,
        RDS_RDMA_READWRITE as RDS_RDMA_READWRITE,
        RDS_RDMA_SILENT as RDS_RDMA_SILENT,
        RDS_RDMA_USE_ONCE as RDS_RDMA_USE_ONCE,
        RDS_RECVERR as RDS_RECVERR,
        SOL_ALG as SOL_ALG,
        SOL_CAN_BASE as SOL_CAN_BASE,
        SOL_CAN_RAW as SOL_CAN_RAW,
        SOL_RDS as SOL_RDS,
        SOL_TIPC as SOL_TIPC,
        TIPC_ADDR_ID as TIPC_ADDR_ID,
        TIPC_ADDR_NAME as TIPC_ADDR_NAME,
        TIPC_ADDR_NAMESEQ as TIPC_ADDR_NAMESEQ,
        TIPC_CFG_SRV as TIPC_CFG_SRV,
        TIPC_CLUSTER_SCOPE as TIPC_CLUSTER_SCOPE,
        TIPC_CONN_TIMEOUT as TIPC_CONN_TIMEOUT,
        TIPC_CRITICAL_IMPORTANCE as TIPC_CRITICAL_IMPORTANCE,
        TIPC_DEST_DROPPABLE as TIPC_DEST_DROPPABLE,
        TIPC_HIGH_IMPORTANCE as TIPC_HIGH_IMPORTANCE,
        TIPC_IMPORTANCE as TIPC_IMPORTANCE,
        TIPC_LOW_IMPORTANCE as TIPC_LOW_IMPORTANCE,
        TIPC_MEDIUM_IMPORTANCE as TIPC_MEDIUM_IMPORTANCE,
        TIPC_NODE_SCOPE as TIPC_NODE_SCOPE,
        TIPC_PUBLISHED as TIPC_PUBLISHED,
        TIPC_SRC_DROPPABLE as TIPC_SRC_DROPPABLE,
        TIPC_SUB_CANCEL as TIPC_SUB_CANCEL,
        TIPC_SUB_PORTS as TIPC_SUB_PORTS,
        TIPC_SUB_SERVICE as TIPC_SUB_SERVICE,
        TIPC_SUBSCR_TIMEOUT as TIPC_SUBSCR_TIMEOUT,
        TIPC_TOP_SRV as TIPC_TOP_SRV,
        TIPC_WAIT_FOREVER as TIPC_WAIT_FOREVER,
        TIPC_WITHDRAWN as TIPC_WITHDRAWN,
        TIPC_ZONE_SCOPE as TIPC_ZONE_SCOPE,
    )
if sys.platform == "linux" and sys.version_info >= (3, 7):
    from _socket import (
        CAN_ISOTP as CAN_ISOTP,
        IOCTL_VM_SOCKETS_GET_LOCAL_CID as IOCTL_VM_SOCKETS_GET_LOCAL_CID,
        SO_VM_SOCKETS_BUFFER_MAX_SIZE as SO_VM_SOCKETS_BUFFER_MAX_SIZE,
        SO_VM_SOCKETS_BUFFER_MIN_SIZE as SO_VM_SOCKETS_BUFFER_MIN_SIZE,
        SO_VM_SOCKETS_BUFFER_SIZE as SO_VM_SOCKETS_BUFFER_SIZE,
        TCP_NOTSENT_LOWAT as TCP_NOTSENT_LOWAT,
        VM_SOCKETS_INVALID_VERSION as VM_SOCKETS_INVALID_VERSION,
        VMADDR_CID_ANY as VMADDR_CID_ANY,
        VMADDR_CID_HOST as VMADDR_CID_HOST,
        VMADDR_PORT_ANY as VMADDR_PORT_ANY,
    )
if sys.platform == "linux" and sys.version_info >= (3, 8):
    from _socket import (
        CAN_BCM_CAN_FD_FRAME as CAN_BCM_CAN_FD_FRAME,
        CAN_BCM_RX_ANNOUNCE_RESUME as CAN_BCM_RX_ANNOUNCE_RESUME,
        CAN_BCM_RX_CHECK_DLC as CAN_BCM_RX_CHECK_DLC,
        CAN_BCM_RX_FILTER_ID as CAN_BCM_RX_FILTER_ID,
        CAN_BCM_RX_NO_AUTOTIMER as CAN_BCM_RX_NO_AUTOTIMER,
        CAN_BCM_RX_RTR_FRAME as CAN_BCM_RX_RTR_FRAME,
        CAN_BCM_SETTIMER as CAN_BCM_SETTIMER,
        CAN_BCM_STARTTIMER as CAN_BCM_STARTTIMER,
        CAN_BCM_TX_ANNOUNCE as CAN_BCM_TX_ANNOUNCE,
        CAN_BCM_TX_COUNTEVT as CAN_BCM_TX_COUNTEVT,
        CAN_BCM_TX_CP_CAN_ID as CAN_BCM_TX_CP_CAN_ID,
        CAN_BCM_TX_RESET_MULTI_IDX as CAN_BCM_TX_RESET_MULTI_IDX,
    )
if sys.platform == "linux" and sys.version_info >= (3, 9):
    from _socket import (
        CAN_J1939 as CAN_J1939,
        J1939_EE_INFO_NONE as J1939_EE_INFO_NONE,
        J1939_EE_INFO_TX_ABORT as J1939_EE_INFO_TX_ABORT,
        J1939_FILTER_MAX as J1939_FILTER_MAX,
        J1939_IDLE_ADDR as J1939_IDLE_ADDR,
        J1939_MAX_UNICAST_ADDR as J1939_MAX_UNICAST_ADDR,
        J1939_NLA_BYTES_ACKED as J1939_NLA_BYTES_ACKED,
        J1939_NLA_PAD as J1939_NLA_PAD,
        J1939_NO_ADDR as J1939_NO_ADDR,
        J1939_NO_NAME as J1939_NO_NAME,
        J1939_NO_PGN as J1939_NO_PGN,
        J1939_PGN_ADDRESS_CLAIMED as J1939_PGN_ADDRESS_CLAIMED,
        J1939_PGN_ADDRESS_COMMANDED as J1939_PGN_ADDRESS_COMMANDED,
        J1939_PGN_MAX as J1939_PGN_MAX,
        J1939_PGN_PDU1_MAX as J1939_PGN_PDU1_MAX,
        J1939_PGN_REQUEST as J1939_PGN_REQUEST,
        SCM_J1939_DEST_ADDR as SCM_J1939_DEST_ADDR,
        SCM_J1939_DEST_NAME as SCM_J1939_DEST_NAME,
        SCM_J1939_ERRQUEUE as SCM_J1939_ERRQUEUE,
        SCM_J1939_PRIO as SCM_J1939_PRIO,
        SO_J1939_ERRQUEUE as SO_J1939_ERRQUEUE,
        SO_J1939_FILTER as SO_J1939_FILTER,
        SO_J1939_PROMISC as SO_J1939_PROMISC,
        SO_J1939_SEND_PRIO as SO_J1939_SEND_PRIO,
    )
if sys.platform == "win32":
    from _socket import (
        RCVALL_IPLEVEL as RCVALL_IPLEVEL,
        RCVALL_MAX as RCVALL_MAX,
        RCVALL_OFF as RCVALL_OFF,
        RCVALL_ON as RCVALL_ON,
        RCVALL_SOCKETLEVELONLY as RCVALL_SOCKETLEVELONLY,
        SIO_KEEPALIVE_VALS as SIO_KEEPALIVE_VALS,
        SIO_LOOPBACK_FAST_PATH as SIO_LOOPBACK_FAST_PATH,
        SIO_RCVALL as SIO_RCVALL,
    )

_T = TypeVar("_T")

# Re-exported from errno
EBADF: int
EAGAIN: int
EWOULDBLOCK: int

class AddressFamily(IntEnum):
    AF_UNIX: int
    AF_INET: int
    AF_INET6: int
    AF_AAL5: int
    AF_ALG: int
    AF_APPLETALK: int
    AF_ASH: int
    AF_ATMPVC: int
    AF_ATMSVC: int
    AF_AX25: int
    AF_BLUETOOTH: int
    AF_BRIDGE: int
    AF_CAN: int
    AF_DECnet: int
    AF_ECONET: int
    AF_IPX: int
    AF_IRDA: int
    AF_KEY: int
    AF_LINK: int
    AF_LLC: int
    AF_NETBEUI: int
    AF_NETLINK: int
    AF_NETROM: int
    AF_PACKET: int
    AF_PPPOX: int
    AF_QIPCRTR: int
    AF_RDS: int
    AF_ROSE: int
    AF_ROUTE: int
    AF_SECURITY: int
    AF_SNA: int
    AF_SYSTEM: int
    AF_TIPC: int
    AF_UNSPEC: int
    AF_VSOCK: int
    AF_WANPIPE: int
    AF_X25: int

AF_UNIX: AddressFamily
AF_INET: AddressFamily
AF_INET6: AddressFamily
AF_AAL5: AddressFamily
AF_APPLETALK: AddressFamily
AF_ASH: AddressFamily
AF_ATMPVC: AddressFamily
AF_ATMSVC: AddressFamily
AF_AX25: AddressFamily
AF_BRIDGE: AddressFamily
AF_DECnet: AddressFamily
AF_ECONET: AddressFamily
AF_IPX: AddressFamily
AF_IRDA: AddressFamily
AF_KEY: AddressFamily
AF_LLC: AddressFamily
AF_NETBEUI: AddressFamily
AF_NETROM: AddressFamily
AF_PPPOX: AddressFamily
AF_ROSE: AddressFamily
AF_ROUTE: AddressFamily
AF_SECURITY: AddressFamily
AF_SNA: AddressFamily
AF_SYSTEM: AddressFamily
AF_UNSPEC: AddressFamily
AF_WANPIPE: AddressFamily
AF_X25: AddressFamily
if sys.platform == "linux":
    AF_CAN: AddressFamily
    AF_PACKET: AddressFamily
    AF_RDS: AddressFamily
    AF_TIPC: AddressFamily
    AF_ALG: AddressFamily
    AF_NETLINK: AddressFamily
    if sys.version_info >= (3, 7):
        AF_VSOCK: AddressFamily
    if sys.version_info >= (3, 8):
        AF_QIPCRTR: AddressFamily
AF_LINK: AddressFamily  # availability: BSD, macOS
if sys.platform != "win32" and sys.platform != "darwin":
    AF_BLUETOOTH: AddressFamily

class SocketKind(IntEnum):
    SOCK_STREAM: int
    SOCK_DGRAM: int
    SOCK_RAW: int
    SOCK_RDM: int
    SOCK_SEQPACKET: int
    SOCK_CLOEXEC: int
    SOCK_NONBLOCK: int

SOCK_STREAM: SocketKind
SOCK_DGRAM: SocketKind
SOCK_RAW: SocketKind
SOCK_RDM: SocketKind
SOCK_SEQPACKET: SocketKind
if sys.platform == "linux":
    SOCK_CLOEXEC: SocketKind
    SOCK_NONBLOCK: SocketKind

class MsgFlag(IntFlag):
    MSG_CTRUNC: int
    MSG_DONTROUTE: int
    MSG_DONTWAIT: int
    MSG_EOR: int
    MSG_OOB: int
    MSG_PEEK: int
    MSG_TRUNC: int
    MSG_WAITALL: int

MSG_BCAST: MsgFlag
MSG_BTAG: MsgFlag
MSG_CMSG_CLOEXEC: MsgFlag
MSG_CONFIRM: MsgFlag
MSG_CTRUNC: MsgFlag
MSG_DONTROUTE: MsgFlag
MSG_DONTWAIT: MsgFlag
MSG_EOF: MsgFlag
MSG_EOR: MsgFlag
MSG_ERRQUEUE: MsgFlag
MSG_ETAG: MsgFlag
MSG_FASTOPEN: MsgFlag
MSG_MCAST: MsgFlag
MSG_MORE: MsgFlag
MSG_NOSIGNAL: MsgFlag
MSG_NOTIFICATION: MsgFlag
MSG_OOB: MsgFlag
MSG_PEEK: MsgFlag
MSG_TRUNC: MsgFlag
MSG_WAITALL: MsgFlag

class AddressInfo(IntFlag):
    AI_ADDRCONFIG: int
    AI_ALL: int
    AI_CANONNAME: int
    AI_NUMERICHOST: int
    AI_NUMERICSERV: int
    AI_PASSIVE: int
    AI_V4MAPPED: int

AI_ADDRCONFIG: AddressInfo
AI_ALL: AddressInfo
AI_CANONNAME: AddressInfo
AI_DEFAULT: AddressInfo
AI_MASK: AddressInfo
AI_NUMERICHOST: AddressInfo
AI_NUMERICSERV: AddressInfo
AI_PASSIVE: AddressInfo
AI_V4MAPPED: AddressInfo
AI_V4MAPPED_CFG: AddressInfo

if sys.platform == "win32":
    errorTab: dict[int, str]  # undocumented

class socket(_socket.socket):
    def __init__(
        self,
        family: Union[AddressFamily, int] = ...,
        type: Union[SocketKind, int] = ...,
        proto: int = ...,
        fileno: Optional[int] = ...,
    ) -> None: ...
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args: object) -> None: ...
    def dup(self: _T) -> _T: ...  # noqa: F811
    def accept(self) -> tuple[socket, _RetAddress]: ...
    # Note that the makefile's documented windows-specific behavior is not represented
    # mode strings with duplicates are intentionally excluded
    @overload
    def makefile(
        self,
        mode: Literal["r", "w", "rw", "wr", ""] = ...,
        buffering: Optional[int] = ...,
        *,
        encoding: Optional[str] = ...,
        errors: Optional[str] = ...,
        newline: Optional[str] = ...,
    ) -> TextIO: ...
    @overload
    def makefile(
        self,
        mode: Literal["b", "rb", "br", "wb", "bw", "rwb", "rbw", "wrb", "wbr", "brw", "bwr"],
        buffering: Optional[int] = ...,
        *,
        encoding: Optional[str] = ...,
        errors: Optional[str] = ...,
        newline: Optional[str] = ...,
    ) -> BinaryIO: ...
    def sendfile(self, file: BinaryIO, offset: int = ..., count: Optional[int] = ...) -> int: ...
    @property
    def family(self) -> AddressFamily: ...  # type: ignore
    @property
    def type(self) -> SocketKind: ...  # type: ignore
    def get_inheritable(self) -> bool: ...
    def set_inheritable(self, inheritable: bool) -> None: ...

def fromfd(fd: _FD, family: AddressFamily | int, type: SocketKind | int, proto: int = ...) -> socket: ...

if sys.platform != "win32":
    if sys.version_info >= (3, 9):
        # flags and address appear to be unused in send_fds and recv_fds
        def send_fds(
            sock: socket, buffers: Iterable[bytes], fds: Union[bytes, Iterable[int]], flags: int = ..., address: None = ...
        ) -> int: ...
        def recv_fds(sock: socket, bufsize: int, maxfds: int, flags: int = ...) -> tuple[bytes, list[int], int, Any]: ...

if sys.platform == "win32":
    def fromshare(info: bytes) -> socket: ...

if sys.platform == "win32":
    def socketpair(family: int = ..., type: int = ..., proto: int = ...) -> tuple[socket, socket]: ...

else:
    def socketpair(  # type: ignore
        family: Union[int, AddressFamily, None] = ..., type: Union[SocketType, int] = ..., proto: int = ...
    ) -> tuple[socket, socket]: ...

class SocketIO(RawIOBase):
    def __init__(self, sock: socket, mode: Literal["r", "w", "rw", "rb", "wb", "rwb"]) -> None: ...
    def readinto(self, b: WriteableBuffer) -> Optional[int]: ...
    def write(self, b: ReadableBuffer) -> Optional[int]: ...
    @property
    def name(self) -> int: ...  # return value is really "int"
    @property
    def mode(self) -> Literal["rb", "wb", "rwb"]: ...

def getfqdn(name: str = ...) -> str: ...
def create_connection(
    address: tuple[Optional[str], int],
    timeout: Optional[float] = ...,  # noqa: F811
    source_address: Optional[tuple[Union[bytearray, bytes, str], int]] = ...,
) -> socket: ...

if sys.version_info >= (3, 8):
    def has_dualstack_ipv6() -> bool: ...
    def create_server(
        address: _Address, *, family: int = ..., backlog: Optional[int] = ..., reuse_port: bool = ..., dualstack_ipv6: bool = ...
    ) -> socket: ...

# the 5th tuple item is an address
def getaddrinfo(
    host: Optional[Union[bytearray, bytes, str]],
    port: Union[str, int, None],
    family: int = ...,
    type: int = ...,
    proto: int = ...,
    flags: int = ...,
) -> list[tuple[AddressFamily, SocketKind, int, str, Union[tuple[str, int], tuple[str, int, int, int]]]]: ...
