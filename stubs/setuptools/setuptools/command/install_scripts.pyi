from typing import Any

import setuptools._distutils.command.install_scripts as orig

class install_scripts(orig.install_scripts):
    no_ep: bool
    def initialize_options(self) -> None: ...
    outfiles: Any
    def run(self) -> None: ...
    def write_script(self, script_name, contents, mode: str = ..., *ignored) -> None: ...
