"""Test cases for psutil.process_iter and its cache_clear method."""

from __future__ import annotations

import psutil

# Test that process_iter can be called as a function (original behavior)
for proc in psutil.process_iter():
    break

for proc in psutil.process_iter(attrs=["pid", "name"]):
    break

for proc in psutil.process_iter(attrs=["pid"], ad_value="N/A"):
    break

# Test that process_iter has cache_clear method (new behavior)
psutil.process_iter.cache_clear()

# Test that cache_clear is callable
clear_method = psutil.process_iter.cache_clear
clear_method()

# Test type annotations work correctly
from collections.abc import Iterator
from typing import Any

processes: Iterator[psutil.Process] = psutil.process_iter()
processes_with_attrs: Iterator[psutil.Process] = psutil.process_iter(attrs=["pid"])

# Test that cache_clear returns None
psutil.process_iter.cache_clear()  # Returns None, don't assign
