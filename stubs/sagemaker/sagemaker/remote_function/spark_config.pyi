from typing import Dict, List, Optional

class SparkConfig:
    submit_jars: Optional[List[str]]
    submit_py_files: Optional[List[str]]
    submit_files: Optional[List[str]]
    configuration: Optional[List[Dict, Dict]]
    spark_event_logs_uri: Optional[str]
    def __init__(self, submit_jars, submit_py_files, submit_files, configuration, spark_event_logs_uri) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
