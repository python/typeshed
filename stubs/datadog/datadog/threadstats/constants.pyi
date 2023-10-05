from _typeshed import Incomplete

class MetricType:
    Gauge: str
    Counter: str
    Histogram: str
    Rate: str
    Distribution: str

class MonitorType:
    SERVICE_CHECK: str
    METRIC_ALERT: str
    QUERY_ALERT: str
    ALL: Incomplete
