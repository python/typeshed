from _typeshed import Incomplete
from collections import UserList

class Equivalency(UserList[Incomplete]):
    data: Incomplete
    name: Incomplete
    kwargs: Incomplete
    def __init__(self, equiv_list, name: str = ..., kwargs: Incomplete | None = ...) -> None: ...
    def __add__(self, other): ...
    def __eq__(self, other): ...

def dimensionless_angles(): ...
def logarithmic(): ...
def parallax(): ...
def spectral(): ...
def spectral_density(wav, factor: Incomplete | None = ...): ...
def doppler_radio(rest): ...
def doppler_optical(rest): ...
def doppler_relativistic(rest): ...
def doppler_redshift(): ...
def molar_mass_amu(): ...
def mass_energy(): ...
def brightness_temperature(frequency, beam_area: Incomplete | None = ...): ...
def beam_angular_area(beam_area): ...
def thermodynamic_temperature(frequency, T_cmb: Incomplete | None = ...): ...
def temperature(): ...
def temperature_energy(): ...
def pixel_scale(pixscale): ...
def plate_scale(platescale): ...
