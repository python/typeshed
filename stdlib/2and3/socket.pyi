# Stubs for socket
# Ron Murawski <ron@horizonchess.com>

# based on: http://docs.python.org/3.2/library/socket.html
# see: http://hg.python.org/cpython/file/3d0686d90f55/Lib/socket.py
# see: http://nullege.com/codes/search/socket
# adapted for Python 2.7 by Michal Pokorny
import sys
from typing import Any, Tuple, List, Optional, Union, overload

# ----- variables and constants -----

AF_UNIX: int
AF_INET: int
AF_INET6: int
SOCK_STREAM: int
SOCK_DGRAM: int
SOCK_RAW: int
SOCK_RDM: int
SOCK_SEQPACKET: int
SOCK_CLOEXEC: int
SOCK_NONBLOCK: int
SOMAXCONN: int
has_ipv6: bool
_GLOBAL_DEFAULT_TIMEOUT: Any
SocketType: Any
SocketIO: Any


# the following constants are included with Python 3.2.3 (Ubuntu)
# some of the constants may be Linux-only
# all Windows/Mac-specific constants are absent
AF_APPLETALK: int
AF_ASH: int
AF_ATMPVC: int
AF_ATMSVC: int
AF_AX25: int
AF_BLUETOOTH: int
AF_BRIDGE: int
AF_DECnet: int
AF_ECONET: int
AF_IPX: int
AF_IRDA: int
AF_KEY: int
AF_LLC: int
AF_NETBEUI: int
AF_NETLINK: int
AF_NETROM: int
AF_PACKET: int
AF_PPPOX: int
AF_ROSE: int
AF_ROUTE: int
AF_SECURITY: int
AF_SNA: int
AF_TIPC: int
AF_UNSPEC: int
AF_WANPIPE: int
AF_X25: int
AI_ADDRCONFIG: int
AI_ALL: int
AI_CANONNAME: int
AI_NUMERICHOST: int
AI_NUMERICSERV: int
AI_PASSIVE: int
AI_V4MAPPED: int
BDADDR_ANY: int
BDADDR_LOCAL: int
BTPROTO_HCI: int
BTPROTO_L2CAP: int
BTPROTO_RFCOMM: int
BTPROTO_SCO: int
CAPI: int
EAGAIN: int
EAI_ADDRFAMILY: int
EAI_AGAIN: int
EAI_BADFLAGS: int
EAI_FAIL: int
EAI_FAMILY: int
EAI_MEMORY: int
EAI_NODATA: int
EAI_NONAME: int
EAI_OVERFLOW: int
EAI_SERVICE: int
EAI_SOCKTYPE: int
EAI_SYSTEM: int
EBADF: int
EINTR: int
EWOULDBLOCK: int
HCI_DATA_DIR: int
HCI_FILTER: int
HCI_TIME_STAMP: int
INADDR_ALLHOSTS_GROUP: int
INADDR_ANY: int
INADDR_BROADCAST: int
INADDR_LOOPBACK: int
INADDR_MAX_LOCAL_GROUP: int
INADDR_NONE: int
INADDR_UNSPEC_GROUP: int
IPPORT_RESERVED: int
IPPORT_USERRESERVED: int
IPPROTO_AH: int
IPPROTO_DSTOPTS: int
IPPROTO_EGP: int
IPPROTO_ESP: int
IPPROTO_FRAGMENT: int
IPPROTO_GRE: int
IPPROTO_HOPOPTS: int
IPPROTO_ICMP: int
IPPROTO_ICMPV6: int
IPPROTO_IDP: int
IPPROTO_IGMP: int
IPPROTO_IP: int
IPPROTO_IPIP: int
IPPROTO_IPV6: int
IPPROTO_NONE: int
IPPROTO_PIM: int
IPPROTO_PUP: int
IPPROTO_RAW: int
IPPROTO_ROUTING: int
IPPROTO_RSVP: int
IPPROTO_TCP: int
IPPROTO_TP: int
IPPROTO_UDP: int
IPV6_CHECKSUM: int
IPV6_DSTOPTS: int
IPV6_HOPLIMIT: int
IPV6_HOPOPTS: int
IPV6_JOIN_GROUP: int
IPV6_LEAVE_GROUP: int
IPV6_MULTICAST_HOPS: int
IPV6_MULTICAST_IF: int
IPV6_MULTICAST_LOOP: int
IPV6_NEXTHOP: int
IPV6_PKTINFO: int
IPV6_RECVDSTOPTS: int
IPV6_RECVHOPLIMIT: int
IPV6_RECVHOPOPTS: int
IPV6_RECVPKTINFO: int
IPV6_RECVRTHDR: int
IPV6_RECVTCLASS: int
IPV6_RTHDR: int
IPV6_RTHDRDSTOPTS: int
IPV6_RTHDR_TYPE_0: int
IPV6_TCLASS: int
IPV6_UNICAST_HOPS: int
IPV6_V6ONLY: int
IP_ADD_MEMBERSHIP: int
IP_DEFAULT_MULTICAST_LOOP: int
IP_DEFAULT_MULTICAST_TTL: int
IP_DROP_MEMBERSHIP: int
IP_HDRINCL: int
IP_MAX_MEMBERSHIPS: int
IP_MULTICAST_IF: int
IP_MULTICAST_LOOP: int
IP_MULTICAST_TTL: int
IP_OPTIONS: int
IP_RECVOPTS: int
IP_RECVRETOPTS: int
IP_RETOPTS: int
IP_TOS: int
IP_TTL: int
MSG_CTRUNC: int
MSG_DONTROUTE: int
MSG_DONTWAIT: int
MSG_EOR: int
MSG_OOB: int
MSG_PEEK: int
MSG_TRUNC: int
MSG_WAITALL: int
NETLINK_DNRTMSG: int
NETLINK_FIREWALL: int
NETLINK_IP6_FW: int
NETLINK_NFLOG: int
NETLINK_ROUTE: int
NETLINK_USERSOCK: int
NETLINK_XFRM: int
NI_DGRAM: int
NI_MAXHOST: int
NI_MAXSERV: int
NI_NAMEREQD: int
NI_NOFQDN: int
NI_NUMERICHOST: int
NI_NUMERICSERV: int
PACKET_BROADCAST: int
PACKET_FASTROUTE: int
PACKET_HOST: int
PACKET_LOOPBACK: int
PACKET_MULTICAST: int
PACKET_OTHERHOST: int
PACKET_OUTGOING: int
PF_PACKET: int
SHUT_RD: int
SHUT_RDWR: int
SHUT_WR: int
SOL_HCI: int
SOL_IP: int
SOL_SOCKET: int
SOL_TCP: int
SOL_TIPC: int
SOL_UDP: int
SO_ACCEPTCONN: int
SO_BROADCAST: int
SO_DEBUG: int
SO_DONTROUTE: int
SO_ERROR: int
SO_KEEPALIVE: int
SO_LINGER: int
SO_OOBINLINE: int
SO_RCVBUF: int
SO_RCVLOWAT: int
SO_RCVTIMEO: int
SO_REUSEADDR: int
SO_SNDBUF: int
SO_SNDLOWAT: int
SO_SNDTIMEO: int
SO_TYPE: int
TCP_CORK: int
TCP_DEFER_ACCEPT: int
TCP_INFO: int
TCP_KEEPCNT: int
TCP_KEEPIDLE: int
TCP_KEEPINTVL: int
TCP_LINGER2: int
TCP_MAXSEG: int
TCP_NODELAY: int
TCP_QUICKACK: int
TCP_SYNCNT: int
TCP_WINDOW_CLAMP: int
TIPC_ADDR_ID: int
TIPC_ADDR_NAME: int
TIPC_ADDR_NAMESEQ: int
TIPC_CFG_SRV: int
TIPC_CLUSTER_SCOPE: int
TIPC_CONN_TIMEOUT: int
TIPC_CRITICAL_IMPORTANCE: int
TIPC_DEST_DROPPABLE: int
TIPC_HIGH_IMPORTANCE: int
TIPC_IMPORTANCE: int
TIPC_LOW_IMPORTANCE: int
TIPC_MEDIUM_IMPORTANCE: int
TIPC_NODE_SCOPE: int
TIPC_PUBLISHED: int
TIPC_SRC_DROPPABLE: int
TIPC_SUBSCR_TIMEOUT: int
TIPC_SUB_CANCEL: int
TIPC_SUB_PORTS: int
TIPC_SUB_SERVICE: int
TIPC_TOP_SRV: int
TIPC_WAIT_FOREVER: int
TIPC_WITHDRAWN: int
TIPC_ZONE_SCOPE: int


# enum versions of above flags py 3.4+
if sys.version_info >= (3, 4):
    from enum import IntEnum

    class AddressFamily(IntEnum):
        AF_UNIX = ...
        AF_INET = ...
        AF_INET6 = ...
        AF_APPLETALK = ...
        AF_ASH = ...
        AF_ATMPVC = ...
        AF_ATMSVC = ...
        AF_AX25 = ...
        AF_BLUETOOTH = ...
        AF_BRIDGE = ...
        AF_DECnet = ...
        AF_ECONET = ...
        AF_IPX = ...
        AF_IRDA = ...
        AF_KEY = ...
        AF_LLC = ...
        AF_NETBEUI = ...
        AF_NETLINK = ...
        AF_NETROM = ...
        AF_PACKET = ...
        AF_PPPOX = ...
        AF_ROSE = ...
        AF_ROUTE = ...
        AF_SECURITY = ...
        AF_SNA = ...
        AF_TIPC = ...
        AF_UNSPEC = ...
        AF_WANPIPE = ...
        AF_X25 = ...

    class SocketKind(IntEnum):
        SOCK_STREAM = ...
        SOCK_DGRAM = ...
        SOCK_RAW = ...
        SOCK_RDM = ...
        SOCK_SEQPACKET = ...
        SOCK_CLOEXEC = ...
        SOCK_NONBLOCK = ...

if sys.version_info >= (3, 6):
    from enum import IntFlag

    class AddressInfo(IntFlag):
        AI_ADDRCONFIG = ...
        AI_ALL = ...
        AI_CANONNAME = ...
        AI_NUMERICHOST = ...
        AI_NUMERICSERV = ...
        AI_PASSIVE = ...
        AI_V4MAPPED = ...

    class MsgFlag(IntFlag):
        MSG_CTRUNC = ...
        MSG_DONTROUTE = ...
        MSG_DONTWAIT = ...
        MSG_EOR = ...
        MSG_OOB = ...
        MSG_PEEK = ...
        MSG_TRUNC = ...
        MSG_WAITALL = ...


# ----- exceptions -----
class error(IOError):
    ...

class herror(error):
    def __init__(self, herror: int, string: str) -> None: ...

class gaierror(error):
    def __init__(self, error: int, string: str) -> None: ...

class timeout(error):
    ...


# Addresses can be either tuples of varying lengths (AF_INET, AF_INET6,
# AF_NETLINK, AF_TIPC) or strings (AF_UNIX).

# TODO AF_PACKET and AF_BLUETOOTH address objects


# ----- classes -----
class socket:
    family: int
    type: int
    proto: int

    if sys.version_info < (3,):
        def __init__(self, family: int = ..., type: int = ...,
                 proto: int = ...) -> None: ...
    else:
        def __init__(self, family: int = ..., type: int = ...,
                     proto: int = ..., fileno: Optional[int] = ...) -> None: ...

    # --- methods ---
    # second tuple item is an address
    def accept(self) -> Tuple['socket', Any]: ...
    def bind(self, address: Union[tuple, str]) -> None: ...
    def close(self) -> None: ...
    def connect(self, address: Union[tuple, str]) -> None: ...
    def connect_ex(self, address: Union[tuple, str]) -> int: ...
    def detach(self) -> int: ...
    def fileno(self) -> int: ...

    # return value is an address
    def getpeername(self) -> Any: ...
    def getsockname(self) -> Any: ...

    @overload
    def getsockopt(self, level: int, optname: int) -> int: ...
    @overload
    def getsockopt(self, level: int, optname: int, buflen: int) -> bytes: ...

    def gettimeout(self) -> float: ...
    def ioctl(self, control: object,
              option: Tuple[int, int, int]) -> None: ...
    def listen(self, backlog: int) -> None: ...
    # TODO the return value may be BinaryIO or TextIO, depending on mode
    def makefile(self, mode: str = ..., buffering: int = ...,
                 encoding: str = ..., errors: str = ...,
                 newline: str = ...) -> Any:
        ...
    def recv(self, bufsize: int, flags: int = ...) -> bytes: ...

    # return type is an address
    def recvfrom(self, bufsize: int, flags: int = ...) -> Any: ...
    def recvfrom_into(self, buffer: bytes, nbytes: int,
                      flags: int = ...) -> Any: ...
    def recv_into(self, buffer: bytes, nbytes: int,
                  flags: int = ...) -> Any: ...
    def send(self, data: bytes, flags: int = ...) -> int: ...
    def sendall(self, data: bytes, flags: int =...) -> None:
        ...  # return type: None on success
    @overload
    def sendto(self, data: bytes, address: Union[tuple, str]) -> int: ...
    @overload
    def sendto(self, data: bytes, flags: int, address: Union[tuple, str]) -> int: ...
    def setblocking(self, flag: bool) -> None: ...
    def settimeout(self, value: Union[float, None]) -> None: ...
    def setsockopt(self, level: int, optname: int, value: Union[int, bytes]) -> None: ...
    def shutdown(self, how: int) -> None: ...


# ----- functions -----
def create_connection(address: Tuple[str, int],
                      timeout: float = ...,
                      source_address: Tuple[str, int] = ...) -> socket: ...

# the 5th tuple item is an address
# TODO the "Tuple[Any, ...]" should be "Union[Tuple[str, int], Tuple[str, int, int, int]]" but that triggers
# https://github.com/python/mypy/issues/2509
def getaddrinfo(
        host: Optional[str], port: Union[str, int, None], family: int = ...,
        socktype: int = ..., proto: int = ...,
        flags: int = ...) -> List[Tuple[int, int, int, str, Tuple[Any, ...]]]:
    ...

def getfqdn(name: str = ...) -> str: ...
def gethostbyname(hostname: str) -> str: ...
def gethostbyname_ex(hostname: str) -> Tuple[str, List[str], List[str]]: ...
def gethostname() -> str: ...
def gethostbyaddr(ip_address: str) -> Tuple[str, List[str], List[str]]: ...
def getnameinfo(sockaddr: tuple, flags: int) -> Tuple[str, int]: ...
def getprotobyname(protocolname: str) -> int: ...
def getservbyname(servicename: str, protocolname: str = ...) -> int: ...
def getservbyport(port: int, protocolname: str = ...) -> str: ...
def socketpair(family: int = ...,
               type: int = ...,
               proto: int = ...) -> Tuple[socket, socket]: ...
def fromfd(fd: int, family: int, type: int, proto: int = ...) -> socket: ...
def ntohl(x: int) -> int: ...  # param & ret val are 32-bit ints
def ntohs(x: int) -> int: ...  # param & ret val are 16-bit ints
def htonl(x: int) -> int: ...  # param & ret val are 32-bit ints
def htons(x: int) -> int: ...  # param & ret val are 16-bit ints
def inet_aton(ip_string: str) -> bytes: ...  # ret val 4 bytes in length
def inet_ntoa(packed_ip: bytes) -> str: ...
def inet_pton(address_family: int, ip_string: str) -> bytes: ...
def inet_ntop(address_family: int, packed_ip: bytes) -> str: ...
def getdefaulttimeout() -> Optional[float]: ...
def setdefaulttimeout(timeout: Optional[float]) -> None: ...
