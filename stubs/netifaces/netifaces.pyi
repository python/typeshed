from typing import Dict, List, Tuple, Union, Literal

AF_12844: int
AF_APPLETALK: int
AF_ASH: int
AF_ATM: int
AF_ATMPVC: int
AF_ATMSVC: int
AF_AX25: int
AF_BAN: int
AF_BLUETOOTH: int
AF_BRIDGE: int
AF_DATAKIT: int
AF_DECnet: int
AF_CCITT: int
AF_CHAOS: int
AF_CLUSTER: int
AF_CNT: int
AF_COIP: int
AF_DLI: int
AF_ECONET: int
AF_ECMA: int
AF_FILE: int
AF_FIREFOX: int
AF_HYLINK: int
AF_IMPLINK: int
AF_INET: int
AF_INET6: int
AF_IPX: int
AF_IRDA: int
AF_ISDN: int
AF_ISO: int
AF_KEY: int
AF_LAT: int
AF_LINK: int
AF_NATM: int
AF_NETBEUI: int
AF_NETBIOS: int
AF_NETDES: int
AF_NETGRAPH: int
AF_NETLINK: int
AF_NETROM: int
AF_NDRV: int
AF_NS: int
AF_PACKET: int
AF_PPP: int
AF_PPPOX: int
AF_PUP: int
AF_ROSE: int
AF_ROUTE: int
AF_SECURITY: int
AF_SIP: int
AF_SNA: int
AF_SYSTEM: int
AF_UNIX: int
AF_UNKNOWN1: int
AF_UNSPEC: int
AF_VOICEVIEW: int
AF_WANPIPE: int
AF_X25: int
IN6_IFF_AUTOCONF: int
IN6_IFF_TEMPORARY: int
IN6_IFF_DYNAMIC: int
IN6_IFF_OPTIMISTIC: int
IN6_IFF_SECURED: int

address_families: Dict[int, str]
version: str

def gateways() -> (
    Dict[Union[int, Literal["default"]], Union[List[Union[Tuple[str, str, bool], Tuple[str, str]]], Dict[int, Tuple[str, str]]]]
): ...
def ifaddresses(ifname: str, /) -> Dict[int, List[Dict[str, str]]]: ...
def interfaces() -> List[str]: ...
