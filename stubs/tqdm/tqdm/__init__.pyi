from _typeshed import Incomplete

from ._monitor import TMonitor as TMonitor, TqdmSynchronisationWarning as TqdmSynchronisationWarning
from ._tqdm_pandas import tqdm_pandas as tqdm_pandas
from .cli import main as main
from .gui import tqdm as tqdm_gui, trange as tgrange
from .notebook import tqdm_notebook as tqdm_notebook_cls
from .std import (
    TqdmDeprecationWarning as TqdmDeprecationWarning,
    TqdmExperimentalWarning as TqdmExperimentalWarning,
    TqdmKeyError as TqdmKeyError,
    TqdmMonitorWarning as TqdmMonitorWarning,
    TqdmTypeError as TqdmTypeError,
    TqdmWarning as TqdmWarning,
    tqdm as tqdm,
    trange as trange,
)
from .version import __version__ as __version__

__all__ = [
    "TMonitor",
    "TqdmDeprecationWarning",
    "TqdmExperimentalWarning",
    "TqdmKeyError",
    "TqdmMonitorWarning",
    "TqdmSynchronisationWarning",
    "TqdmTypeError",
    "TqdmWarning",
    "__version__",
    "main",
    "tgrange",
    "tnrange",
    "tqdm",
    "tqdm_gui",
    "tqdm_notebook",
    "tqdm_pandas",
    "trange",
]

def tqdm_notebook(*args, **kwargs) -> tqdm_notebook_cls[Incomplete]: ...
def tnrange(*args, **kwargs) -> tqdm_notebook_cls[int]: ...
