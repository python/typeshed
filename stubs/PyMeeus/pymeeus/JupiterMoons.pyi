from _typeshed import FloatInt
from typing import Literal, overload

from pymeeus.Angle import Angle
from pymeeus.Epoch import Epoch

class JupiterMoons:
    @staticmethod
    def jupiter_system_angles(epoch: Epoch) -> tuple[float, float]: ...
    @staticmethod
    def rectangular_positions_jovian_equatorial(
        epoch: Epoch, tofk5: bool = True, solar: bool = False, do_correction: bool = True
    ) -> tuple[
        tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]
    ]: ...

    @overload
    @staticmethod
    def apparent_rectangular_coordinates(
        epoch: Epoch,
        X: FloatInt,
        Y: FloatInt,
        Z: FloatInt,
        OMEGA: FloatInt,
        psi: FloatInt,
        i: FloatInt,
        lambda_0: FloatInt,
        beta_0: FloatInt,
        D: FloatInt = 0,
        isFictional: Literal[True] = ...,
    ) -> float: ...
    @overload
    @staticmethod
    def apparent_rectangular_coordinates(
        epoch: Epoch,
        X: FloatInt,
        Y: FloatInt,
        Z: FloatInt,
        OMEGA: FloatInt,
        psi: FloatInt,
        i: FloatInt,
        lambda_0: FloatInt,
        beta_0: FloatInt,
        D: FloatInt = 0,
        isFictional: Literal[False] | None = False,
    ) -> tuple[float, float, float]: ...

    @staticmethod
    def calculate_delta(
        epoch: Epoch,
    ) -> tuple[float, float, Angle, Angle, float] | tuple[float, float, Literal[0], Literal[0], Literal[0]]: ...

    @overload
    @staticmethod
    def correct_rectangular_positions(
        R: FloatInt, i_sat: int, DELTA: FloatInt, X_coordinate: list[FloatInt] | tuple[FloatInt, FloatInt, FloatInt]
    ) -> tuple[float, float, float]: ...
    @overload
    @staticmethod
    def correct_rectangular_positions(
        R: FloatInt, i_sat: int, DELTA: FloatInt, X_coordinate: FloatInt, Y_coordinate: FloatInt = 0, Z_coordinate: FloatInt = 0
    ) -> tuple[float, float, float]: ...

    @overload
    @staticmethod
    def check_phenomena(epoch: Epoch, check_all: Literal[True] = True, i_sat: int = 0) -> list[list[float]]: ...
    @overload
    @staticmethod
    def check_phenomena(epoch: Epoch, check_all: Literal[False] | None, i_sat: int = 0) -> tuple[float, float]: ...

    @staticmethod
    def is_phenomena(epoch: Epoch) -> list[list[bool]]: ...
    @staticmethod
    def check_coordinates(X: FloatInt, Y: FloatInt) -> float: ...
    @staticmethod
    def check_occultation(
        X: FloatInt = 0, Y: FloatInt = 0, Z: FloatInt = 0, epoch: Epoch | None = None, i_sat: int | None = None
    ) -> float: ...
    @staticmethod
    def check_eclipse(
        X_0: FloatInt = 0, Y_0: FloatInt = 0, Z_0: FloatInt = 0, epoch: Epoch | None = None, i_sat: int | None = None
    ) -> float: ...

def main() -> None: ...
