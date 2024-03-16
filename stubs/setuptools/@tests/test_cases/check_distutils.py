import distutils.command.sdist
import distutils.config
from distutils.util import split_version

s = split_version("")
d = distutils.config.PyPIRCCommand
c = distutils.command.sdist.sdist
