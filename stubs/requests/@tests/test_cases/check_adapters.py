from __future__ import annotations

from typing import Any
from typing_extensions import assert_type

import requests.adapters
from urllib3.poolmanager import PoolManager

adapter = requests.adapters.HTTPAdapter()

assert_type(adapter.__attrs__, list[str])
assert_type(adapter.config, dict[str, Any])
assert_type(adapter.poolmanager, PoolManager)
adapter.cert_verify(None, "https://example.com", True, None)
