from distutils.command import upload as orig

from setuptools.errors import RemovedCommandError as RemovedCommandError

class upload(orig.upload):
    def run(self) -> None: ...
