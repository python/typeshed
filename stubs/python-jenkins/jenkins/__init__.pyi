from _typeshed import Incomplete
from collections.abc import Mapping, MutableMapping, Sequence
from typing import Any

import requests
from requests.models import Request, Response

LAUNCHER_SSH: str
LAUNCHER_COMMAND: str
LAUNCHER_JNLP: str
LAUNCHER_WINDOWS_SERVICE: str
DEFAULT_HEADERS: dict[str, str]
DEFAULT_TIMEOUT: float
INFO: str
PLUGIN_INFO: str
CRUMB_URL: str
WHOAMI_URL: str
JOBS_QUERY: str
JOBS_QUERY_TREE: str
JOB_INFO: str
JOB_NAME: str
ALL_BUILDS: str
Q_INFO: str
Q_ITEM: str
CANCEL_QUEUE: str
CREATE_JOB: str
CONFIG_JOB: str
DELETE_JOB: str
ENABLE_JOB: str
DISABLE_JOB: str
CHECK_JENKINSFILE_SYNTAX: str
SET_JOB_BUILD_NUMBER: str
COPY_JOB: str
RENAME_JOB: str
BUILD_JOB: str
STOP_BUILD: str
BUILD_WITH_PARAMS_JOB: str
BUILD_INFO: str
BUILD_CONSOLE_OUTPUT: str
BUILD_ENV_VARS: str
BUILD_TEST_REPORT: str
BUILD_ARTIFACT: str
BUILD_STAGES: str
DELETE_BUILD: str
WIPEOUT_JOB_WORKSPACE: str
NODE_LIST: str
CREATE_NODE: str
DELETE_NODE: str
NODE_INFO: str
NODE_TYPE: str
TOGGLE_OFFLINE: str
CONFIG_NODE: str
VIEW_NAME: str
VIEW_JOBS: str
CREATE_VIEW: str
CONFIG_VIEW: str
DELETE_VIEW: str
SCRIPT_TEXT: str
NODE_SCRIPT_TEXT: str
PROMOTION_NAME: str
PROMOTION_INFO: str
DELETE_PROMOTION: str
CREATE_PROMOTION: str
CONFIG_PROMOTION: str
LIST_CREDENTIALS: str
CREATE_CREDENTIAL: str
CONFIG_CREDENTIAL: str
CREDENTIAL_INFO: str
QUIET_DOWN: str
EMPTY_CONFIG_XML: str
EMPTY_FOLDER_XML: str
RECONFIG_XML: str
EMPTY_VIEW_CONFIG_XML: str
EMPTY_PROMO_CONFIG_XML: str
PROMO_RECONFIG_XML: str

class JenkinsException(Exception): ...
class NotFoundException(JenkinsException): ...
class EmptyResponseException(JenkinsException): ...
class BadHTTPException(JenkinsException): ...
class TimeoutException(JenkinsException): ...

class WrappedSession(requests.Session):
    def merge_environment_settings(
        self,
        url: str | bytes | None,
        proxies: MutableMapping[str, str] | None,
        stream: bool | None,
        verify: bool | str | None,
        cert: str | tuple[str, str] | None,
    ) -> dict[str, Any]: ...

class Jenkins:
    server: str
    auth: Incomplete
    crumb: Mapping[str, Any] | bool | Any
    timeout: float
    def __init__(self, url: str, username: str | None = None, password: str | None = None, timeout: int = ...) -> None: ...
    def maybe_add_crumb(self, req: Request) -> None: ...
    def get_job_info(self, name: str, depth: int = 0, fetch_all_builds: bool = False) -> Mapping[Any, Any]: ...
    def get_job_info_regex(
        self, pattern: str, depth: int = 0, folder_depth: int = 0, folder_depth_per_request: int = 10
    ) -> Sequence[Mapping[Any, Any]]: ...
    def get_job_name(self, name: str) -> str | None: ...
    def debug_job_info(self, job_name: str) -> None: ...
    def jenkins_open(self, req: Request, add_crumb: bool = True, resolve_auth: bool = True) -> str: ...
    def jenkins_open_stream(self, req: Request, add_crumb: bool = True, resolve_auth: bool = True) -> Response: ...
    def jenkins_request(
        self, req: Request, add_crumb: bool = True, resolve_auth: bool = True, stream: bool | None = None
    ) -> Response: ...
    def get_queue_item(self, number: int, depth: int = 0) -> Mapping[Any, Any]: ...
    def get_build_info(self, name: str, number: int, depth: int = 0) -> Mapping[Any, Any]: ...
    def get_build_env_vars(self, name: str, number: int, depth: int = 0) -> Mapping[Any, Any] | None: ...
    def get_build_test_report(self, name: str, number: int, depth: int = 0) -> Mapping[Any, Any] | None: ...
    def get_build_artifact(self, name: str, number: int, artifact: str) -> Mapping[Any, Any]: ...
    def get_build_artifact_as_bytes(self, name: str, number: int, artifact: str) -> bytes: ...
    def get_build_stages(self, name: str, number: int) -> Mapping[Any, Any]: ...
    def get_queue_info(self) -> Mapping[Any, Any]: ...
    def cancel_queue(self, id: int) -> None: ...
    def get_info(self, item: str = "", query: str | None = None) -> Mapping[Any, Any]: ...
    def get_whoami(self, depth: int = 0) -> Mapping[Any, Any]: ...
    def get_version(self) -> str: ...
    def get_plugins_info(self, depth: int = 2) -> Mapping[Any, Any]: ...
    def get_plugin_info(self, name: str, depth: int = 2) -> Mapping[Any, Any]: ...
    def get_plugins(self, depth: int = 2) -> Mapping[Any, Any]: ...
    def get_jobs(
        self, folder_depth: int = 0, folder_depth_per_request: int = 10, view_name: str | None = None
    ) -> Sequence[Mapping[str, str]]: ...
    def get_all_jobs(
        self, folder_depth: int | None = None, folder_depth_per_request: int = 10
    ) -> Sequence[Mapping[str, str]]: ...
    def copy_job(self, from_name: str, to_name: str) -> None: ...
    def rename_job(self, from_name: str, to_name: str) -> None: ...
    def delete_job(self, name: str) -> None: ...
    def enable_job(self, name: str) -> None: ...
    def disable_job(self, name: str) -> None: ...
    def set_next_build_number(self, name: str, number: int) -> None: ...
    def job_exists(self, name: str) -> bool: ...
    def jobs_count(self) -> int: ...
    def assert_job_exists(self, name: str, exception_message: str = "job[%s] does not exist") -> None: ...
    def create_folder(self, folder_name: str, ignore_failures: bool = False) -> None: ...
    def upsert_job(self, name: str, config_xml: str) -> None: ...
    def check_jenkinsfile_syntax(self, jenkinsfile: str) -> Sequence[str]: ...
    def create_job(self, name: str, config_xml: str) -> None: ...
    def get_job_config(self, name: str) -> str: ...
    def reconfig_job(self, name: str, config_xml: str) -> None: ...
    def build_job_url(
        self, name: str, parameters: Mapping[str, Any] | Sequence[tuple[str, Any]] | None = None, token: str | None = None
    ) -> str: ...
    def build_job(
        self, name: str, parameters: Mapping[str, Any] | Sequence[tuple[str, Any]] | None = None, token: str | None = None
    ) -> int: ...
    def run_script(self, script, node: str | None = None) -> str: ...
    def install_plugin(self, name: str, include_dependencies: bool = True) -> bool: ...
    def stop_build(self, name: str, number: int) -> None: ...
    def delete_build(self, name: str, number: int) -> None: ...
    def wipeout_job_workspace(self, name: str) -> None: ...
    def get_running_builds(self) -> Sequence[Mapping[str, Any]]: ...
    def get_nodes(self, depth: int = 0) -> Sequence[Mapping[str, Any]]: ...
    def get_node_info(self, name: str, depth: int = 0) -> Mapping[str, Any]: ...
    def node_exists(self, name: str) -> bool: ...
    def assert_node_exists(self, name: str, exception_message: str = "node[%s] does not exist") -> None: ...
    def delete_node(self, name: str) -> None: ...
    def disable_node(self, name: str, msg: str = "") -> None: ...
    def enable_node(self, name: str) -> None: ...
    def create_node(
        self,
        name: str,
        numExecutors: int = 2,
        nodeDescription: str | None = None,
        remoteFS: str = "/var/lib/jenkins",
        labels: str | None = None,
        exclusive: bool = False,
        launcher: str = "hudson.slaves.CommandLauncher",
        launcher_params: Mapping[str, Any] = {},
    ) -> None: ...
    def get_node_config(self, name: str): ...
    def reconfig_node(self, name: str, config_xml: str) -> None: ...
    def get_build_console_output(self, name: str, number: int) -> str: ...
    def get_view_name(self, name: str) -> str | None: ...
    def assert_view_exists(self, name: str, exception_message: str = "view[%s] does not exist") -> None: ...
    def view_exists(self, name: str) -> bool: ...
    def get_views(self) -> Sequence[Mapping[Any, Any]]: ...
    def delete_view(self, name: str) -> None: ...
    def create_view(self, name: str, config_xml: str) -> None: ...
    def reconfig_view(self, name: str, config_xml: str) -> None: ...
    def get_view_config(self, name: str) -> str: ...
    def get_promotion_name(self, name: str, job_name: str) -> str | None: ...
    def assert_promotion_exists(
        self, name: str, job_name: str, exception_message: str = "promotion[%s] does not exist for job[%s]"
    ) -> None: ...
    def promotion_exists(self, name: str, job_name: str) -> bool: ...
    def get_promotions_info(self, job_name: str, depth: int = 0) -> Mapping[str, Any]: ...
    def get_promotions(self, name: str) -> Sequence[Mapping[str, Any]]: ...
    def delete_promotion(self, name: str, job_name: str) -> None: ...
    def create_promotion(self, name: str, job_name: str, config_xml: str) -> None: ...
    def reconfig_promotion(self, name: str, job_name: str, config_xml: str) -> None: ...
    def get_promotion_config(self, name: str, job_name: str) -> str: ...
    def assert_folder(self, name: str, exception_message: str = "job[%s] is not a folder") -> None: ...
    def is_folder(self, name: str) -> bool: ...
    def assert_credential_exists(
        self,
        name: str,
        folder_name: str,
        domain_name: str = "_",
        exception_message: str = "credential[%s] does not exist in the domain[%s] of [%s]",  # noqa: Y053
    ) -> None: ...
    def credential_exists(self, name: str, folder_name: str, domain_name: str = "_") -> bool: ...
    def get_credential_info(self, name: str, folder_name: str, domain_name: str = "_") -> Mapping[Any, Any]: ...
    def get_credential_config(self, name: str, folder_name: str, domain_name: str = "_") -> str: ...
    def create_credential(self, folder_name: str, config_xml: str, domain_name: str = "_") -> None: ...
    def delete_credential(self, name: str, folder_name: str, domain_name: str = "_") -> None: ...
    def reconfig_credential(self, folder_name: str, config_xml: str, domain_name: str = "_") -> None: ...
    def list_credentials(self, folder_name: str, domain_name: str = "_") -> Sequence[Any]: ...
    def quiet_down(self) -> None: ...
    def wait_for_normal_op(self, timeout: int) -> bool: ...
