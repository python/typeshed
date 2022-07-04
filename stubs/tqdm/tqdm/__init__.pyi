from ._monitor import TMonitor as TMonitor, TqdmSynchronisationWarning as TqdmSynchronisationWarning
from ._tqdm_pandas import tqdm_pandas as tqdm_pandas
from .cli import main as main
from .gui import tqdm as tqdm_gui, trange as tgrange
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

def tqdm_notebook(*args, **kwargs): ...
def tnrange(*args, **kwargs): ...
