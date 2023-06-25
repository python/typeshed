from _typeshed import Incomplete

CHI_SQUARED_METHOD: str
L_INFINITY_METHOD: str

class DataQualityDistributionConstraints:
    categorical_drift_method: Incomplete
    def __init__(self, categorical_drift_method: str | None = None) -> None: ...
    @staticmethod
    def valid_distribution_constraints(distribution_constraints): ...
    @staticmethod
    def valid_categorical_drift_method(categorical_drift_method): ...

class DataQualityMonitoringConfig:
    distribution_constraints: Incomplete
    def __init__(self, distribution_constraints: DataQualityDistributionConstraints | None = None) -> None: ...
    @staticmethod
    def valid_monitoring_config(monitoring_config): ...
