from OpenGL.GL import *

from .GLMeshItem import GLMeshItem

__all__ = ["GLSurfacePlotItem"]

class GLSurfacePlotItem(GLMeshItem):
    def __init__(self, x=None, y=None, z=None, colors=None, parentItem=None, **kwds) -> None: ...
    def setData(self, x=None, y=None, z=None, colors=None) -> None: ...
    def generateFaces(self) -> None: ...
