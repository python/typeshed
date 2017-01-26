def test_object_sizeof():
    # type: () -> None

    class C(object):
        pass

    object().__sizeof__()
    C().__sizeof__()
