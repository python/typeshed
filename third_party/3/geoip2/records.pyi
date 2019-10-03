# Stubs for geoip2.records (Python 3)

from typing import Any, Mapping, Optional, Sequence, Tuple

from geoip2.mixins import SimpleEquality

_Locales = Optional[Sequence[str]]
_Names = Mapping[str, str]

class Record(SimpleEquality):
    __metaclass__: Any = ...
    def __init__(self, **kwargs: Any) -> None: ...
    def __setattr__(self, name: str, value: Any) -> None: ...

class PlaceRecord(Record):
    __metaclass__: Any = ...
    def __init__(self, locales: _Locales = ..., **kwargs: Any) -> None: ...
    @property
    def name(self) -> str: ...

class City(PlaceRecord):
    confidence: int = ...
    geoname_id: int = ...
    names: _Names = ...

class Continent(PlaceRecord):
    code: str = ...
    geoname_id: int = ...
    names: _Names = ...

class Country(PlaceRecord):
    confidence: int = ...
    geoname_id: int = ...
    is_in_european_union: bool = ...
    iso_code: str = ...
    names: _Names = ...
    def __init__(self, locales: _Locales = ..., **kwargs: Any) -> None: ...

class RepresentedCountry(Country):
    type: str = ...

class Location(Record):
    average_income: int = ...
    accuracy_radius: int = ...
    latitude: float = ...
    longitude: float = ...
    metro_code: int = ...
    population_density: int = ...
    time_zone: str = ...

class MaxMind(Record):
    queries_remaining: int = ...

class Postal(Record):
    code: str = ...
    confidence: int = ...

class Subdivision(PlaceRecord):
    confidence: int = ...
    geoname_id: int = ...
    iso_code: str = ...
    names: _Names = ...

class Subdivisions(Tuple[Subdivision]):
    def __new__(cls, locales: _Locales, *subdivisions: Subdivision) -> Subdivisions: ...
    def __init__(self, locales: _Locales, *subdivisions: Subdivision) -> None: ...
    @property
    def most_specific(self) -> Subdivision: ...

class Traits(Record):
    autonomous_system_number: int = ...
    autonomous_system_organization: int = ...
    connection_type: str = ...
    domain: str = ...
    ip_address: str = ...
    is_anonymous: bool = ...
    is_anonymous_proxy: bool = ...
    is_anonymous_vpn: bool = ...
    is_hosting_provider: bool = ...
    is_legitimate_proxy: bool = ...
    is_public_proxy: bool = ...
    is_satellite_provider: bool = ...
    is_tor_exit_node: bool = ...
    isp: str = ...
    organization: str = ...
    user_type: str = ...
    def __init__(self, **kwargs: Any) -> None: ...
