from typing import Any

from selenium.webdriver.common import utils as utils
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities as DesiredCapabilities
from selenium.webdriver.remote.remote_connection import RemoteConnection as RemoteConnection
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

from .service import Service as Service

class WebDriver(RemoteWebDriver):
    port: Any
    edge_service: Any
    def __init__(
        self,
        executable_path: str = ...,
        capabilities: Any | None = ...,
        port: int = ...,
        verbose: bool = ...,
        service_log_path: Any | None = ...,
        log_path: Any | None = ...,
        keep_alive: bool = ...,
    ) -> None: ...
    def quit(self) -> None: ...
