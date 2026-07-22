from setuptools._distutils.command import build_clib as orig
from setuptools.dist import Distribution

class build_clib(orig.build_clib):
    distribution: Distribution  # override distutils.dist.Distribution with setuptools.dist.Distribution

    def build_libraries(self, libraries) -> None: ...
