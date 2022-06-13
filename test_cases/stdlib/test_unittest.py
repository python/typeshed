# pyright: reportUnnecessaryTypeIgnoreComment=true

import unittest
from datetime import datetime, timedelta
from decimal import Decimal
from fractions import Fraction


case = unittest.TestCase()

case.assertAlmostEqual(2.4, 2.41)
case.assertAlmostEqual(Fraction(49, 50), Fraction(48, 50))
case.assertAlmostEqual(datetime(1999, 1, 2), datetime(1999, 1, 2, microsecond=1), delta=timedelta(hours=1))
case.assertAlmostEqual(Decimal("1.1"), Decimal("1.11"))
case.assertAlmostEqual(2.4, 2.41, places=8)
case.assertAlmostEqual(2.4, 2.41, delta=0.02)

case.assertAlmostEqual(2.4, 2.41, places=9, delta=0.02)  # type: ignore[call-overload]
case.assertAlmostEqual("foo", "bar")  # type: ignore[call-overload]
case.assertAlmostEqual(datetime(1999, 1, 2), datetime(1999, 1, 2, microsecond=1))  # type: ignore[arg-type]
