from typing import NamedTuple


def test_typing_namedtuple():
    # type: () -> None
    Point = NamedTuple('Point', [('x', float), ('y', float)])
    p = Point(1, 2)

    p._replace(y=3.14)
    p._asdict()
    p.x, p.y
    p[0] + p[1]
    p.index(1)
    Point._make([('x', 1), ('y', 3.14)])
