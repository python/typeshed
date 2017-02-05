import pip  # type: ignore

pip.main('install six==1.10.0'.split())

from six import PY2, PY3  # noqa: E402
from six.moves import xrange  # noqa: E402


def test_python_checks():
    assert PY2 ^ PY3


def test_xrange():
    xs = xrange(4)
    assert xs.__iter__
    assert xs[0] == 0
    assert sum(xs, 10)
