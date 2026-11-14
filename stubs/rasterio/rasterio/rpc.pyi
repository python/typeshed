from _typeshed import FloatInt
from collections.abc import Sequence
from typing import Any
from typing_extensions import Self

class RPC:
    height_off: FloatInt
    height_scale: FloatInt
    lat_off: FloatInt
    lat_scale: FloatInt
    line_den_coeff: Sequence[FloatInt]
    line_num_coeff: Sequence[FloatInt]
    line_off: FloatInt
    line_scale: FloatInt
    long_off: FloatInt
    long_scale: FloatInt
    samp_den_coeff: Sequence[FloatInt]
    samp_num_coeff: Sequence[FloatInt]
    samp_off: FloatInt
    samp_scale: FloatInt
    err_bias: FloatInt | None
    err_rand: FloatInt | None
    def __init__(
        self,
        height_off: FloatInt,
        height_scale: FloatInt,
        lat_off: FloatInt,
        lat_scale: FloatInt,
        line_den_coeff: Sequence[FloatInt],
        line_num_coeff: Sequence[FloatInt],
        line_off: FloatInt,
        line_scale: FloatInt,
        long_off: FloatInt,
        long_scale: FloatInt,
        samp_den_coeff: Sequence[FloatInt],
        samp_num_coeff: Sequence[FloatInt],
        samp_off: FloatInt,
        samp_scale: FloatInt,
        err_bias: FloatInt | None = None,
        err_rand: FloatInt | None = None,
    ) -> None: ...
    def to_dict(self) -> dict[str, Any]: ...
    def to_gdal(self) -> dict[str, str]: ...
    @classmethod
    def from_gdal(cls, rpcs: dict[str, str]) -> Self: ...
