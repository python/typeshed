from typing import Any

from selenium.common.exceptions import WebDriverException as WebDriverException
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.support.ui import WebDriverWait as WebDriverWait

LOAD_TIMEOUT: int

class WebDriver(RemoteWebDriver):
    def __init__(
        self, device_password, bb_tools_dir: Any | None = ..., hostip: str = ..., port: int = ..., desired_capabilities=...
    ): ...
    def quit(self) -> None: ...
