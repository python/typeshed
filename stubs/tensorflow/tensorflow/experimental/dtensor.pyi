from _typeshed import Incomplete

import numpy as np
import numpy.typing as npt
from tensorflow._aliases import IntDataSequence

class Mesh:
    def __init__(
        self,
        dim_names: list[str],
        global_device_ids: npt.NDArray[np.uint] | IntDataSequence,
        local_device_ids: list[int],
        local_devices: list[Incomplete | str],
        mesh_name: str = "",
        global_devices: list[Incomplete | str] | None = None,
        use_xla_spmd: bool = True,
    ) -> None: ...

def __getattr__(name: str) -> Incomplete: ...
