from enum import Enum

def convert_json_config_to_string(config): ...
def is_valid_unix_time(unix_time): ...
def is_valid_regex(regex): ...

class ErrorMessages(Enum):
    INVALID_LOCAL_PATH: str
    INVALID_FILE_MAX_SIZE: str
    INVALID_FILE_CLOSE_INTERVAL: str
    INVALID_FILE_OPEN_FAIL_THRESHOLD: str
    INVALID_PROFILE_DEFAULT_STEPS: str
    INVALID_START_STEP: str
    INVALID_NUM_STEPS: str
    INVALID_START_UNIX_TIME: str
    INVALID_DURATION: str
    FOUND_BOTH_STEP_AND_TIME_FIELDS: str
    INVALID_METRICS_REGEX: str
    INVALID_PYTHON_PROFILER: str
    INVALID_CPROFILE_TIMER: str

class PythonProfiler(Enum):
    CPROFILE: str
    PYINSTRUMENT: str

class cProfileTimer(Enum):
    TOTAL_TIME: str
    CPU_TIME: str
    OFF_CPU_TIME: str
    DEFAULT: str
