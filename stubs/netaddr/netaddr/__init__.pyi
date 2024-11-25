from netaddr.contrib.subnet_splitter import SubnetSplitter as SubnetSplitter
from netaddr.core import (
    INET_ATON as INET_ATON,
    INET_PTON as INET_PTON,
    NOHOST as NOHOST,
    ZEROFILL as ZEROFILL,
    AddrConversionError as AddrConversionError,
    AddrFormatError as AddrFormatError,
    NotRegisteredError as NotRegisteredError,
)
from netaddr.eui import EUI as EUI, IAB as IAB, OUI as OUI
from netaddr.ip import (
    IPAddress as IPAddress,
    IPNetwork as IPNetwork,
    IPRange as IPRange,
    all_matching_cidrs as all_matching_cidrs,
    cidr_abbrev_to_verbose as cidr_abbrev_to_verbose,
    cidr_exclude as cidr_exclude,
    cidr_merge as cidr_merge,
    iprange_to_cidrs as iprange_to_cidrs,
    iter_iprange as iter_iprange,
    iter_unique_ips as iter_unique_ips,
    largest_matching_cidr as largest_matching_cidr,
    smallest_matching_cidr as smallest_matching_cidr,
    spanning_cidr as spanning_cidr,
)
from netaddr.ip.glob import (
    IPGlob as IPGlob,
    cidr_to_glob as cidr_to_glob,
    glob_to_cidrs as glob_to_cidrs,
    glob_to_iprange as glob_to_iprange,
    glob_to_iptuple as glob_to_iptuple,
    iprange_to_globs as iprange_to_globs,
    valid_glob as valid_glob,
)
from netaddr.ip.nmap import iter_nmap_range as iter_nmap_range, valid_nmap_range as valid_nmap_range
from netaddr.ip.rfc1924 import base85_to_ipv6 as base85_to_ipv6, ipv6_to_base85 as ipv6_to_base85
from netaddr.ip.sets import IPSet as IPSet
from netaddr.strategy.eui48 import (
    mac_bare as mac_bare,
    mac_cisco as mac_cisco,
    mac_eui48 as mac_eui48,
    mac_pgsql as mac_pgsql,
    mac_unix as mac_unix,
    mac_unix_expanded as mac_unix_expanded,
    valid_str as valid_mac,
)
from netaddr.strategy.eui64 import (
    eui64_bare as eui64_bare,
    eui64_base as eui64_base,
    eui64_cisco as eui64_cisco,
    eui64_unix as eui64_unix,
    eui64_unix_expanded as eui64_unix_expanded,
    valid_str as valid_eui64,
)
from netaddr.strategy.ipv4 import expand_partial_address as expand_partial_ipv4_address, valid_str as valid_ipv4
from netaddr.strategy.ipv6 import (
    ipv6_compact as ipv6_compact,
    ipv6_full as ipv6_full,
    ipv6_verbose as ipv6_verbose,
    valid_str as valid_ipv6,
)

__all__ = [
    "EUI",
    "IAB",
    "INET_ATON",
    "INET_PTON",
    "NOHOST",
    "OUI",
    "ZEROFILL",
    "AddrConversionError",
    "AddrFormatError",
    "IPAddress",
    "IPGlob",
    "IPNetwork",
    "IPRange",
    "IPSet",
    "NotRegisteredError",
    "SubnetSplitter",
    "all_matching_cidrs",
    "base85_to_ipv6",
    "cidr_abbrev_to_verbose",
    "cidr_exclude",
    "cidr_merge",
    "cidr_to_glob",
    "eui64_bare",
    "eui64_base",
    "eui64_cisco",
    "eui64_unix",
    "eui64_unix_expanded",
    "expand_partial_ipv4_address",
    "glob_to_cidrs",
    "glob_to_iprange",
    "glob_to_iptuple",
    "iprange_to_cidrs",
    "iprange_to_globs",
    "ipv6_compact",
    "ipv6_full",
    "ipv6_to_base85",
    "ipv6_verbose",
    "iter_iprange",
    "iter_nmap_range",
    "iter_unique_ips",
    "largest_matching_cidr",
    "mac_bare",
    "mac_cisco",
    "mac_eui48",
    "mac_pgsql",
    "mac_unix",
    "mac_unix_expanded",
    "smallest_matching_cidr",
    "spanning_cidr",
    "valid_eui64",
    "valid_glob",
    "valid_ipv4",
    "valid_ipv6",
    "valid_mac",
    "valid_nmap_range",
]

__version__: str
VERSION: tuple[int, ...]
STATUS: str
