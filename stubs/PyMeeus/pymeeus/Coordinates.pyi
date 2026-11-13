from _typeshed import FloatInt
import datetime
from typing import Final, overload

from pymeeus.Angle import Angle
from pymeeus.Epoch import Epoch

NUTATION_ARG_TABLE: Final[list[list[int]]]
NUTATION_SINE_COEF_TABLE: Final[list[list[FloatInt]]]
NUTATION_COSINE_COEF_TABLE: Final[list[list[FloatInt]]]

@overload
def mean_obliquity(
    a: Epoch | list[FloatInt] | tuple[FloatInt, ...] | datetime.date,
    /,
    *,
    leap_seconds: FloatInt = 0,
    local: bool = False,
    utc: bool = False,
) -> Angle: ...
@overload
def mean_obliquity(
    year: int, month: int, day: int, /, *, leap_seconds: FloatInt = 0, local: bool = False, utc: bool = False
) -> Angle: ...

@overload
def true_obliquity(
    a: Epoch | list[FloatInt] | tuple[FloatInt, ...] | datetime.date,
    /,
    *,
    leap_seconds: FloatInt = 0,
    local: bool = False,
    utc: bool = False,
) -> Angle: ...
@overload
def true_obliquity(
    year: int, month: int, day: int, /, *, leap_seconds: FloatInt = 0, local: bool = False, utc: bool = False
) -> Angle: ...

@overload
def nutation_longitude(
    a: Epoch | list[FloatInt] | tuple[FloatInt, ...] | datetime.date,
    /,
    *,
    leap_seconds: FloatInt = 0,
    local: bool = False,
    utc: bool = False,
) -> Angle: ...
@overload
def nutation_longitude(
    year: int, month: int, day: int, /, *, leap_seconds: FloatInt = 0, local: bool = False, utc: bool = False
) -> Angle: ...

@overload
def nutation_obliquity(
    a: Epoch | list[FloatInt] | tuple[FloatInt, ...] | datetime.date,
    /,
    *,
    leap_seconds: FloatInt = 0,
    local: bool = False,
    utc: bool = False,
) -> Angle: ...
@overload
def nutation_obliquity(
    year: int, month: int, day: int, /, *, leap_seconds: FloatInt = 0, local: bool = False, utc: bool = False
) -> Angle: ...

def precession_equatorial(
    start_epoch: Epoch,
    final_epoch: Epoch,
    start_ra: Angle,
    start_dec: Angle,
    p_motion_ra: FloatInt | Angle = 0.0,
    p_motion_dec: FloatInt | Angle = 0.0,
) -> tuple[Angle, Angle]: ...
def precession_ecliptical(
    start_epoch: Epoch,
    final_epoch: Epoch,
    start_lon: Angle,
    start_lat: Angle,
    p_motion_lon: FloatInt | Angle = 0.0,
    p_motion_lat: FloatInt | Angle = 0.0,
) -> tuple[Angle, Angle]: ...
def p_motion_equa2eclip(
    p_motion_ra: Angle, p_motion_dec: Angle, ra: Angle, dec: Angle, lat: Angle, epsilon: Angle
) -> tuple[float, float]: ...
def precession_newcomb(
    start_epoch: Epoch,
    final_epoch: Epoch,
    start_ra: Angle,
    start_dec: Angle,
    p_motion_ra: FloatInt | Angle = 0.0,
    p_motion_dec: FloatInt | Angle = 0.0,
) -> tuple[Angle, Angle]: ...
def motion_in_space(
    start_ra: Angle,
    start_dec: Angle,
    distance: FloatInt,
    velocity: FloatInt,
    p_motion_ra: FloatInt | Angle,
    p_motion_dec: FloatInt | Angle,
    time: FloatInt,
) -> tuple[Angle, Angle]: ...
def equatorial2ecliptical(right_ascension: Angle, declination: Angle, obliquity: Angle) -> tuple[Angle, Angle]: ...
def ecliptical2equatorial(longitude: Angle, latitude: Angle, obliquity: Angle) -> tuple[Angle, Angle]: ...
def equatorial2horizontal(hour_angle: Angle, declination: Angle, geo_latitude: Angle) -> tuple[Angle, Angle]: ...
def horizontal2equatorial(azimuth: Angle, elevation: Angle, geo_latitude: Angle) -> tuple[Angle, Angle]: ...
def equatorial2galactic(right_ascension: Angle, declination: Angle) -> tuple[Angle, Angle]: ...
def galactic2equatorial(longitude: Angle, latitude: Angle) -> tuple[Angle, Angle]: ...
def parallactic_angle(hour_angle: Angle, declination: Angle, geo_latitude: Angle) -> Angle | None: ...
def ecliptic_horizon(local_sidereal_time: Angle, geo_latitude: Angle, obliquity: Angle) -> tuple[Angle, Angle, Angle]: ...
def ecliptic_equator(longitude: Angle, latitude: Angle, obliquity: Angle) -> Angle: ...
def diurnal_path_horizon(declination: Angle, geo_latitude: Angle) -> Angle: ...
def times_rise_transit_set(
    longitude: Angle,
    latitude: Angle,
    alpha1: Angle,
    delta1: Angle,
    alpha2: Angle,
    delta2: Angle,
    alpha3: Angle,
    delta3: Angle,
    h0: Angle,
    delta_t: FloatInt,
    theta0: Angle,
) -> tuple[float, float, float] | tuple[None, None, None]: ...
def refraction_apparent2true(apparent_elevation: Angle, pressure: FloatInt = 1010.0, temperature: FloatInt = 10.0) -> Angle: ...
def refraction_true2apparent(true_elevation: Angle, pressure: FloatInt = 1010.0, temperature: FloatInt = 10.0) -> Angle: ...
def angular_separation(alpha1: Angle, delta1: Angle, alpha2: Angle, delta2: Angle) -> Angle: ...
def minimum_angular_separation(
    alpha1_1: Angle,
    delta1_1: Angle,
    alpha1_2: Angle,
    delta1_2: Angle,
    alpha1_3: Angle,
    delta1_3: Angle,
    alpha2_1: Angle,
    delta2_1: Angle,
    alpha2_2: Angle,
    delta2_2: Angle,
    alpha2_3: Angle,
    delta2_3: Angle,
) -> tuple[float, Angle]: ...
def relative_position_angle(alpha1: Angle, delta1: Angle, alpha2: Angle, delta2: Angle) -> Angle: ...
def planetary_conjunction(
    alpha1_list: list[Angle] | tuple[Angle, ...],
    delta1_list: list[Angle] | tuple[Angle, ...],
    alpha2_list: list[Angle] | tuple[Angle, ...],
    delta2_list: list[Angle] | tuple[Angle, ...],
) -> tuple[float, Angle]: ...
def planet_star_conjunction(
    alpha_list: list[Angle] | tuple[Angle, ...], delta_list: list[Angle] | tuple[Angle, ...], alpha_star: Angle, delta_star: Angle
) -> tuple[float, Angle]: ...
def planet_stars_in_line(
    alpha_list: list[Angle] | tuple[Angle, ...],
    delta_list: list[Angle] | tuple[Angle, ...],
    alpha_star1: Angle,
    delta_star1: Angle,
    alpha_star2: Angle,
    delta_star2: Angle,
) -> float: ...
def straight_line(
    alpha1: Angle, delta1: Angle, alpha2: Angle, delta2: Angle, alpha3: Angle, delta3: Angle
) -> tuple[Angle, Angle]: ...
def circle_diameter(alpha1: Angle, delta1: Angle, alpha2: Angle, delta2: Angle, alpha3: Angle, delta3: Angle) -> Angle: ...
def vsop_pos(
    epoch: Epoch, vsop_l: list[list[list[FloatInt]]], vsop_b: list[list[list[FloatInt]]], vsop_r: list[list[list[FloatInt]]]
) -> tuple[Angle, Angle, float]: ...
def geometric_vsop_pos(
    epoch: Epoch,
    vsop_l: list[list[list[FloatInt]]],
    vsop_b: list[list[list[FloatInt]]],
    vsop_r: list[list[list[FloatInt]]],
    tofk5: bool | None = True,
) -> tuple[Angle, Angle, float]: ...
def apparent_vsop_pos(
    epoch: Epoch,
    vsop_l: list[list[list[FloatInt]]],
    vsop_b: list[list[list[FloatInt]]],
    vsop_r: list[list[list[FloatInt]]],
    nutation: bool | None = True,
) -> tuple[Angle, Angle, float]: ...
def apparent_position(epoch: Epoch, alpha: Angle, delta: Angle, sun_lon: Angle) -> tuple[Angle, Angle]: ...
def orbital_equinox2equinox(epoch0: Epoch, epoch: Epoch, i0: Angle, arg0: Angle, lon0: Angle) -> tuple[Angle, Angle, Angle]: ...
def kepler_equation(eccentricity: FloatInt, mean_anomaly: Angle) -> tuple[Angle, Angle]: ...
def orbital_elements(
    epoch: Epoch, parameters1: list[list[FloatInt]], parameters2: list[list[FloatInt]]
) -> tuple[Angle, float, float, Angle, Angle, Angle]: ...
def velocity(r: FloatInt, a: FloatInt) -> float: ...
def velocity_perihelion(e: FloatInt, a: FloatInt) -> float: ...
def velocity_aphelion(e: FloatInt, a: FloatInt) -> float: ...
def length_orbit(e: FloatInt, a: FloatInt) -> float: ...
def passage_nodes_elliptic(omega: Angle, e: FloatInt, a: FloatInt, t: Epoch, ascending: bool | None = True) -> tuple[Epoch, float]: ...
def passage_nodes_parabolic(omega: Angle, q: FloatInt, t: Epoch, ascending: bool | None = True) -> tuple[Epoch, float]: ...
def phase_angle(sun_dist: FloatInt, earth_dist: FloatInt, sun_earth_dist: FloatInt) -> Angle: ...
def illuminated_fraction(sun_dist: FloatInt, earth_dist: FloatInt, sun_earth_dist: FloatInt) -> float: ...
def main() -> None: ...
