import distutils.command.build_clib as orig

from setuptools.dep_util import newer_pairwise_group as newer_pairwise_group

class build_clib(orig.build_clib):
    def build_libraries(self, libraries) -> None: ...
