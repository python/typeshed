"""Test cases for psutil functions that can return None at runtime."""

from __future__ import annotations

import sys
from typing_extensions import assert_type

import psutil
from psutil._ntuples import pionice, scpufreq, snetio

# cpu_freq() and net_io_counters() return None if the platform reports nothing.
assert_type(psutil.cpu_freq(), scpufreq | None)
assert_type(psutil.cpu_freq(percpu=True), list[scpufreq])
assert_type(psutil.net_io_counters(), snetio | None)
assert_type(psutil.net_io_counters(pernic=True), dict[str, snetio])

proc = psutil.Process()

# wait() returns None if the process is not a child of the current process.
assert_type(proc.wait(), int | None)

if sys.platform != "darwin":
    # Getting returns the current value, setting returns None.
    assert_type(proc.ionice(), pionice)
    assert_type(proc.ionice(2), None)

if sys.platform == "linux":
    assert_type(proc.rlimit(psutil.RLIMIT_NOFILE), tuple[int, int])
    assert_type(proc.rlimit(psutil.RLIMIT_NOFILE, (1024, 4096)), None)
