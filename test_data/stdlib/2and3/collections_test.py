from collections import namedtuple


def test_collections_namedtuple():
    # type: () -> None
    Point = namedtuple('Point', 'x y')
    p = Point(1, 2)

    p._replace(y=3.14)
    p._asdict()
    p.x, p.y
    p[0] + p[1]
    p.index(1)
    Point._make([('x', 1), ('y', 3.14)])
