from distutils.cmd import Command as Command
from distutils.config import PyPIRCCommand as PyPIRCCommand
from distutils.errors import *
from distutils.extension import Extension as Extension
from typing import Any

USAGE: str

def gen_usage(script_name): ...

setup_keywords: Any
extension_keywords: Any

def setup(**attrs): ...
def run_setup(script_name, script_args: Any | None = ..., stop_after: str = ...): ...
