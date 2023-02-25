from _typeshed import Incomplete, Unused
from abc import abstractmethod
from collections.abc import Iterable, Iterator
from typing import SupportsInt, overload
from typing_extensions import Literal, Self, SupportsIndex, TypeAlias

from netaddr.core import DictDotLookup
from netaddr.strategy.ipv6 import ipv6_verbose

class BaseIP:
    def __init__(self) -> None: ...
    @property
    def value(self) -> int | None: ...
    @value.setter
    def value(self, value: int) -> None: ...
    @abstractmethod
    def key(self) -> tuple[int, ...]: ...
    @abstractmethod
    def sort_key(self) -> tuple[int, ...]: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __lt__(self, other: BaseIP) -> bool: ...
    def __le__(self, other: BaseIP) -> bool: ...
    def __gt__(self, other: BaseIP) -> bool: ...
    def __ge__(self, other: BaseIP) -> bool: ...
    def is_unicast(self) -> bool: ...
    def is_multicast(self) -> bool: ...
    def is_loopback(self) -> bool: ...
    def is_private(self) -> bool: ...
    def is_link_local(self) -> bool: ...
    def is_reserved(self) -> bool: ...
    def is_ipv4_mapped(self) -> bool: ...
    def is_ipv4_compat(self) -> bool: ...
    @property
    def info(self) -> DictDotLookup: ...
    @property
    def version(self) -> Literal[4, 6]: ...

_IPAddressAddr: TypeAlias = BaseIP | int | str
_IPNetworkAddr: TypeAlias = IPNetwork | IPAddress | tuple[int, int] | str

class IPAddress(BaseIP):
    def __init__(self, addr: _IPAddressAddr, version: Literal[4, 6] | None = ..., flags: int = ...) -> None: ...
    def netmask_bits(self) -> int: ...
    def is_hostmask(self) -> bool: ...
    def is_netmask(self) -> bool: ...
    def __iadd__(self, num: int) -> Self: ...
    def __isub__(self, num: int) -> Self: ...
    def __add__(self, num: int) -> Self: ...
    __radd__ = __add__
    def __sub__(self, num: int) -> Self: ...
    def __rsub__(self, num: int) -> Self: ...
    def key(self) -> tuple[int, ...]: ...
    def sort_key(self) -> tuple[int, ...]: ...
    def __int__(self) -> int: ...
    def __long__(self) -> int: ...
    def __oct__(self) -> str: ...
    def __hex__(self) -> str: ...
    def __index__(self) -> int: ...
    def __bytes__(self) -> bytes: ...
    def bits(self, word_sep: str | None = ...) -> str: ...
    @property
    def packed(self) -> bytes: ...
    @property
    def words(self) -> tuple[int, ...]: ...
    @property
    def bin(self) -> str: ...
    @property
    def reverse_dns(self) -> str: ...
    def ipv4(self) -> Self: ...
    def ipv6(self, ipv4_compatible: bool = ...) -> Self: ...
    def format(self, dialect: type[ipv6_verbose] | None = ...) -> str: ...
    def __or__(self, other: str | SupportsInt | SupportsIndex) -> Self: ...
    def __and__(self, other: str | SupportsInt | SupportsIndex) -> Self: ...
    def __xor__(self, other: str | SupportsInt | SupportsIndex) -> Self: ...
    def __lshift__(self, numbits: int) -> Self: ...
    def __rshift__(self, numbits: int) -> Self: ...
    def __bool__(self) -> bool: ...

class IPListMixin:
    def __iter__(self) -> Iterator[IPAddress]: ...
    @property
    def size(self) -> int: ...
    def __len__(self) -> int: ...
    @overload
    def __getitem__(self, index: SupportsIndex) -> IPAddress: ...
    @overload
    def __getitem__(self, index: slice) -> Iterator[IPAddress]: ...
    @overload
    def __getitem__(self, index: SupportsIndex | slice) -> IPAddress | Iterator[IPAddress]: ...
    def __contains__(self, other: BaseIP | _IPAddressAddr) -> bool: ...
    def __bool__(self) -> Literal[True]: ...

def parse_ip_network(
    module: Incomplete, addr: tuple[int, int] | str, implicit_prefix: bool = ..., flags: int = ...
) -> tuple[int, int]: ...

class IPNetwork(BaseIP, IPListMixin):
    def __init__(
        self, addr: _IPNetworkAddr, implicit_prefix: bool = ..., version: Literal[4, 6] | None = ..., flags: int = ...
    ) -> None: ...
    @property
    def prefixlen(self) -> int: ...
    @prefixlen.setter
    def prefixlen(self, value: int) -> None: ...
    @property
    def ip(self) -> IPAddress: ...
    @property
    def network(self) -> IPAddress: ...
    @property
    def broadcast(self) -> IPAddress | None: ...
    @property
    def first(self) -> int: ...
    @property
    def last(self) -> int: ...
    @property
    def netmask(self) -> IPAddress: ...
    @netmask.setter
    def netmask(self, value: _IPAddressAddr) -> None: ...
    @property
    def hostmask(self) -> IPAddress: ...
    @property
    def cidr(self) -> IPNetwork: ...
    def __iadd__(self, num: int) -> Self: ...
    def __isub__(self, num: int) -> Self: ...
    # runtime overrides __contains__ with incompatible type for "other"
    def __contains__(self, other: BaseIP | _IPNetworkAddr) -> bool: ...  # type: ignore[override]
    def key(self) -> tuple[int, ...]: ...
    def sort_key(self) -> tuple[int, ...]: ...
    def ipv4(self) -> Self: ...
    def ipv6(self, ipv4_compatible: bool = ...) -> Self: ...
    def previous(self, step: int = ...) -> Self: ...
    def next(self, step: int = ...) -> Self: ...
    def supernet(self, prefixlen: int = ...) -> list[IPNetwork]: ...
    def subnet(self, prefixlen: int, count: int | None = ..., fmt: Unused = None) -> Iterator[Self]: ...
    def iter_hosts(self) -> Iterator[IPAddress]: ...

class IPRange(BaseIP, IPListMixin):
    def __init__(self, start: _IPAddressAddr, end: _IPAddressAddr, flags: int = ...) -> None: ...
    def __contains__(self, other: BaseIP | _IPAddressAddr) -> bool: ...
    @property
    def first(self) -> int: ...
    @property
    def last(self) -> int: ...
    def key(self) -> tuple[int, ...]: ...
    def sort_key(self) -> tuple[int, ...]: ...
    def cidrs(self) -> list[IPNetwork]: ...

def iter_unique_ips(*args: IPRange | _IPNetworkAddr) -> Iterator[IPAddress]: ...
def cidr_abbrev_to_verbose(abbrev_cidr: str | SupportsInt | SupportsIndex) -> str: ...
def cidr_merge(ip_addrs: Iterable[IPRange | _IPNetworkAddr]) -> list[IPNetwork]: ...
def cidr_exclude(target: _IPNetworkAddr, exclude: _IPNetworkAddr) -> list[IPNetwork]: ...
def cidr_partition(
    target: _IPNetworkAddr, exclude: _IPNetworkAddr
) -> tuple[list[IPNetwork], list[IPNetwork], list[IPNetwork]]: ...
def spanning_cidr(ip_addrs: Iterable[_IPNetworkAddr]) -> IPNetwork: ...
def iter_iprange(start: _IPAddressAddr, end: _IPAddressAddr, step: SupportsInt | SupportsIndex = ...) -> Iterator[IPAddress]: ...
def iprange_to_cidrs(start: _IPNetworkAddr, end: _IPNetworkAddr) -> list[IPNetwork]: ...
def smallest_matching_cidr(ip: _IPAddressAddr, cidrs: Iterable[_IPNetworkAddr]) -> IPNetwork | None: ...
def largest_matching_cidr(ip: _IPAddressAddr, cidrs: Iterable[_IPNetworkAddr]) -> IPNetwork | None: ...
def all_matching_cidrs(ip: _IPAddressAddr, cidrs: Iterable[_IPNetworkAddr]) -> list[IPNetwork]: ...

IPV4_LOOPBACK: IPNetwork
IPV4_PRIVATE: tuple[IPNetwork | IPRange, ...]
IPV4_LINK_LOCAL: IPNetwork
IPV4_MULTICAST: IPNetwork
IPV4_6TO4: IPNetwork
IPV4_RESERVED: tuple[IPNetwork | IPRange, ...]
IPV6_LOOPBACK: IPAddress
IPV6_PRIVATE: tuple[IPNetwork, ...]
IPV6_LINK_LOCAL: IPNetwork
IPV6_MULTICAST: IPNetwork
IPV6_RESERVED: tuple[IPNetwork, ...]
