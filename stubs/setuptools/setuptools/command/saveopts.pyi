from setuptools.command.setopt import edit_config as edit_config, option_base as option_base

class saveopts(option_base):
    description: str
    def run(self) -> None: ...
