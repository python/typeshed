from _typeshed import Incomplete

DOCKER_CONFIG_FILENAME: Incomplete
LEGACY_DOCKER_CONFIG_FILENAME: str
log: Incomplete

def find_config_file(config_path: Incomplete | None = None): ...
def config_path_from_environment(): ...
def home_dir(): ...
def load_general_config(config_path: Incomplete | None = None): ...
