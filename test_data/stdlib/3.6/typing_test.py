from typing import NamedTuple


class Point(NamedTuple):
    x: float
    y: float


def test_typing_namedtuple():
    # type: () -> None
    p = Point(1, 2)
    p._asdict()
    p.x, p.y
    p[0] + p[1]
    p.index(1)
    Point._make([('x', 1), ('y', 3.14)])
