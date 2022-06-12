from datetime import datetime
from decimal import Decimal
from fractions import Fraction
from unittest import TestCase


def test_assertAlmostEqual(case: TestCase) -> None:
    case.assertAlmostEqual(2.4, 2.41)
    case.assertAlmostEqual(Fraction(49, 50), Fraction(48, 50))
    case.assertAlmostEqual(datetime(1999, 1, 2), datetime(1999, 1, 2, microsecond=1))
    case.assertAlmostEqual(Decimal("1.1"), Decimal("1.11"))
