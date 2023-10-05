from _typeshed import Incomplete

class CheckStatus:
    OK: int
    WARNING: int
    CRITICAL: int
    UNKNOWN: int
    ALL: Incomplete

class MonitorType:
    QUERY_ALERT: str
    COMPOSITE: str
    SERVICE_CHECK: str
    PROCESS_ALERT: str
    LOG_ALERT: str
    METRIC_ALERT: str
    RUM_ALERT: str
    EVENT_ALERT: str
    SYNTHETICS_ALERT: str
    TRACE_ANALYTICS: str
