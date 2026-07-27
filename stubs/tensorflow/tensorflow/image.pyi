from collections.abc import Sequence

from tensorflow import Tensor
from tensorflow._aliases import IntArray, TensorCompatible

def random_crop(
    value: TensorCompatible, size: Sequence[int] | IntArray | Tensor, seed: int | None = None, name: str | None = None
): ...
def __getattr__(name: str): ...  # incomplete module
