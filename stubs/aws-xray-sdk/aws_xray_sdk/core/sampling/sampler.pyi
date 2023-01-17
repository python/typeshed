from _typeshed import Incomplete
from typing import Any

from .connector import ServiceConnector as ServiceConnector
from .local.sampler import LocalSampler as LocalSampler
from .reservoir import ReservoirDecision as ReservoirDecision
from .rule_cache import RuleCache as RuleCache
from .rule_poller import RulePoller as RulePoller
from .target_poller import TargetPoller as TargetPoller

log: Any

class DefaultSampler:
    def __init__(self) -> None: ...
    def start(self) -> None: ...
    def should_trace(self, sampling_req: Incomplete | None = ...): ...
    def load_local_rules(self, rules) -> None: ...
    def load_settings(self, daemon_config, context, origin: Incomplete | None = ...) -> None: ...
    @property
    def xray_client(self): ...
    @xray_client.setter
    def xray_client(self, v) -> None: ...