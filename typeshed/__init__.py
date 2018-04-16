import os


__all__ = ['__location__', '__version__']


try:
    import pkg_resources
except ImportError:
    __location__ = os.path.dirname(os.path.dirname(__file__))
else:
    __location__ = pkg_resources.resource_filename("typeshed", "")
__version__ = "18.4.0"


# Deprecated name kept for backwards compatibility.
typeshed = __location__
