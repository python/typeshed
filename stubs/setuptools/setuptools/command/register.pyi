import distutils.command.register as orig

from setuptools.errors import RemovedCommandError as RemovedCommandError

class register(orig.register):
    def run(self) -> None: ...
