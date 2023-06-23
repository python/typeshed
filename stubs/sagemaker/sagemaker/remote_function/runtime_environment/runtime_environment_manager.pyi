import logging
import time
from _typeshed import Incomplete

class _UTCFormatter(logging.Formatter):
    converter = time.gmtime

def get_logger(): ...

logger: Incomplete

class RuntimeEnvironmentManager:
    def snapshot(self, dependencies: str = None) -> str: ...
    def bootstrap(self, local_dependencies_file: str, client_python_version: str, conda_env: str = None): ...
    def run_pre_exec_script(self, pre_exec_script_path: str): ...

class RuntimeEnvironmentError(Exception):
    message: Incomplete
    def __init__(self, message) -> None: ...
