import argparse
from collections.abc import Sequence
from typing import Any

from ._child_monitor import ChildProcessMonitor as ChildProcessMonitor
from .binary_collector import BinaryCollector as BinaryCollector
from .binary_reader import BinaryReader as BinaryReader
from .constants import (
    MICROSECONDS_PER_SECOND as MICROSECONDS_PER_SECOND,
    PROFILING_MODE_ALL as PROFILING_MODE_ALL,
    PROFILING_MODE_CPU as PROFILING_MODE_CPU,
    PROFILING_MODE_EXCEPTION as PROFILING_MODE_EXCEPTION,
    PROFILING_MODE_GIL as PROFILING_MODE_GIL,
    PROFILING_MODE_WALL as PROFILING_MODE_WALL,
    SORT_MODE_CUMTIME as SORT_MODE_CUMTIME,
    SORT_MODE_CUMUL_PCT as SORT_MODE_CUMUL_PCT,
    SORT_MODE_NSAMPLES as SORT_MODE_NSAMPLES,
    SORT_MODE_NSAMPLES_CUMUL as SORT_MODE_NSAMPLES_CUMUL,
    SORT_MODE_SAMPLE_PCT as SORT_MODE_SAMPLE_PCT,
    SORT_MODE_TOTTIME as SORT_MODE_TOTTIME,
)
from .errors import (
    SamplingModuleNotFoundError as SamplingModuleNotFoundError,
    SamplingScriptNotFoundError as SamplingScriptNotFoundError,
    SamplingUnknownProcessError as SamplingUnknownProcessError,
)
from .gecko_collector import GeckoCollector as GeckoCollector
from .heatmap_collector import HeatmapCollector as HeatmapCollector
from .live_collector import LiveStatsCollector as LiveStatsCollector
from .pstats_collector import PstatsCollector as PstatsCollector
from .sample import sample as sample, sample_live as sample_live
from .stack_collector import (
    CollapsedStackCollector as CollapsedStackCollector,
    DiffFlamegraphCollector as DiffFlamegraphCollector,
    FlamegraphCollector as FlamegraphCollector,
)

class CustomFormatter(argparse.ArgumentDefaultsHelpFormatter, argparse.RawDescriptionHelpFormatter): ...

class DiffFlamegraphAction(argparse.Action):
    def __call__(
        self,
        parser: argparse.ArgumentParser,
        namespace: argparse.Namespace,
        values: str | Sequence[Any] | None,
        option_string: str | None = None,
    ) -> None: ...

FORMAT_EXTENSIONS: dict[str, str]
COLLECTOR_MAP: dict[str, type[Any]]

def main() -> None: ...
