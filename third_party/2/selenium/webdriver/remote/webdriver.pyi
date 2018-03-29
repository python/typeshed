from typing import Any, Dict, List, Optional, Text
from .mobile import Mobile as Mobile
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.errorhandler import ErrorHandler
from selenium.webdriver.remote.file_detector import FileDetector

Capabilities = Dict[basestring, Any]
ExecuteResult = Dict[basestring, Any]  # containing 'success', 'value', 'sessionId'

class WebDriver:
    command_executor = ...  # type: basestring
    session_id = ...  # type: Any
    capabilities = ...  # type: Capabilities
    error_handler = ...  # type: ErrorHandler
    file_detector = ...  # type: FileDetector
    def __init__(self,
                 command_executor: basestring = ...,
                 desired_capabilities: Capabilities = ...,
                 browser_profile: Optional[Any] = ...,  # should be selenium.webdriver.firefox.firefox_profile.FirefoxProfile, but we don't have a stub for that
                 proxy: Optional[Any] = ...,  # should be selenium.webdriver.common.proxy.Proxy, but there's no stub for that
                 keep_alive: bool = ...
                 ) -> None: ...
    @property
    def mobile(self) -> Mobile: ...
    @property
    def name(self) -> basestring: ...
    def start_client(self): ...
    def stop_client(self): ...
    w3c = ...  # type: Any
    def start_session(self, desired_capabilities, browser_profile=None): ...
    def create_web_element(self, element_id: basestring) -> WebElement: ...
    def execute(self, driver_command: basestring, params: Optional[Dict[basestring, Any]] = ...) -> ExecuteResult: ...
    def get(self, url: basestring) -> None: ...
    @property
    def title(self) -> basestring: ...
    def find_element_by_id(self, id_: basestring) -> WebElement: ...
    def find_elements_by_id(self, id_: basestring) -> List[WebElement]: ...
    def find_element_by_xpath(self, xpath: basestring) -> WebElement: ...
    def find_elements_by_xpath(self, xpath: basestring) -> List[WebElement]: ...
    def find_element_by_link_text(self, link_text: basestring) -> WebElement: ...
    def find_elements_by_link_text(self, text: basestring) -> List[WebElement]: ...
    def find_element_by_partial_link_text(self, link_text: basestring) -> WebElement: ...
    def find_elements_by_partial_link_text(self, link_text: basestring) -> List[WebElement]: ...
    def find_element_by_name(self, name: basestring) -> WebElement: ...
    def find_elements_by_name(self, name: basestring) -> List[WebElement]: ...
    def find_element_by_tag_name(self, name: basestring) -> WebElement: ...
    def find_elements_by_tag_name(self, name: basestring) -> List[WebElement]: ...
    def find_element_by_class_name(self, name: basestring) -> WebElement: ...
    def find_elements_by_class_name(self, name: basestring) -> List[WebElement]: ...
    def find_element_by_css_selector(self, css_selector: basestring) -> WebElement: ...
    def find_elements_by_css_selector(self, css_selector: basestring) -> List[WebElement]: ...
    def execute_script(self, script, *args): ...
    def execute_async_script(self, script, *args): ...
    @property
    def current_url(self) -> basestring: ...
    @property
    def page_source(self): ...
    def close(self): ...
    def quit(self): ...
    @property
    def current_window_handle(self): ...
    @property
    def window_handles(self): ...
    def maximize_window(self): ...
    @property
    def switch_to(self): ...
    def switch_to_active_element(self): ...
    def switch_to_window(self, window_name): ...
    def switch_to_frame(self, frame_reference): ...
    def switch_to_default_content(self): ...
    def switch_to_alert(self): ...
    def back(self): ...
    def forward(self): ...
    def refresh(self): ...
    def get_cookies(self): ...
    def get_cookie(self, name): ...
    def delete_cookie(self, name): ...
    def delete_all_cookies(self): ...
    def add_cookie(self, cookie_dict): ...
    def implicitly_wait(self, time_to_wait): ...
    def set_script_timeout(self, time_to_wait): ...
    def set_page_load_timeout(self, time_to_wait): ...
    def find_element(self, by=..., value=None): ...
    def find_elements(self, by=..., value=None): ...
    @property
    def desired_capabilities(self) -> Capabilities: ...
    def get_screenshot_as_file(self, filename: Text) -> bool: ...
    def save_screenshot(self, filename: Text) -> bool: ...
    def get_screenshot_as_png(self) -> bytes: ...
    def get_screenshot_as_base64(self) -> str: ...
    def set_window_size(self, width: int, height: int, windowHandle: str = ...) -> None: ...
    def get_window_size(self, windowHandle: str = ...) -> Dict[str, int]: ...
    def set_window_position(self, x: int, y: int, windowHandle: str = ...) -> None: ...
    def get_window_position(self, windowHandle: str = ...) -> Dict[str, int]: ...
    @property
    def file_detector(self): ...
    @file_detector.setter
    def file_detector(self, detector): ...
    @property
    def orientation(self): ...
    @orientation.setter
    def orientation(self, value): ...
    @property
    def application_cache(self): ...
    @property
    def log_types(self): ...
    def get_log(self, log_type): ...
