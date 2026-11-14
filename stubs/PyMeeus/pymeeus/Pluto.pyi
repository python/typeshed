from _typeshed import FloatInt
from typing import Final

from pymeeus.Angle import Angle
from pymeeus.Epoch import Epoch

PLUTO_ARGUMENT: Final[list[tuple[FloatInt, FloatInt, FloatInt]]]
PLUTO_LONGITUDE: Final[list[tuple[FloatInt, FloatInt]]]
PLUTO_LATITUDE: Final[list[tuple[FloatInt, FloatInt]]]
PLUTO_RADIUS_VECTOR: Final[list[tuple[FloatInt, FloatInt]]]

class Pluto:
    @staticmethod
    def geometric_heliocentric_position(epoch: Epoch) -> tuple[Angle, Angle, float]: ...
    @staticmethod
    def geocentric_position(epoch: Epoch) -> tuple[Angle, Angle]: ...

def main() -> None: ...
