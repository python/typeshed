from __future__ import annotations

import signal
from typing_extensions import assert_type

# See https://github.com/python/mypy/issues/18628
signals = []
signals.append(signal.SIGALRM)
signals.append(signal.SIGUSR1)
assert_type(signals, list[signal.Signals])
