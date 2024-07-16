from __future__ import annotations

from collections import Counter
from decimal import Decimal
from typing_extensions import assert_type

# Initialize a Counter for strings with integer values
word_counts: Counter[str] = Counter()
word_counts["foo"] += 3
word_counts["bar"] += 2
assert_type(word_counts, "Counter[str, int]")

# Initialize a Counter for strings with float values
floating_point_counts: Counter[str, float] = Counter()
floating_point_counts["foo"] += 3.0
floating_point_counts["bar"] += 5.0

# Initialize a Counter for strings with Decimal values
decimal_counts: Counter[str, Decimal] = Counter()
decimal_counts["foo"] += Decimal("3.0")
decimal_counts["bar"] += Decimal("5.0")

# Counter combining integers and floats
mixed_type_counter = Counter({"foo": 3, "bar": 2.5})
mixed_type_counter["baz"] += 1.5
assert_type(mixed_type_counter, "Counter[str, int | float]")

# Check ORing and ANDing Counters with different value types
assert_type(mixed_type_counter or decimal_counts, "Counter[str, int | float] | Counter[str, Decimal]")
assert_type(decimal_counts or mixed_type_counter, "Counter[str, Decimal] | Counter[str, int | float]")
assert_type(mixed_type_counter and decimal_counts, "Counter[str, int | float] | Counter[str, Decimal]")
assert_type(decimal_counts and mixed_type_counter, "Counter[str, Decimal] | Counter[str, int | float]")

# We shouldn't be able to add Counters with incompatible value types
_ = mixed_type_counter + decimal_counts  # type: ignore
mixed_type_counter += decimal_counts  # type: ignore

# Adding Counters with compatible types
_ = word_counts + Counter({"foo": 2, "baz": 1})
word_counts += Counter({"foo": 2, "baz": 1})

# Combining Counters of different key types
integer_key_counter = Counter({1: 2, 2: 3})
combined_word_and_integer_keys = word_counts + integer_key_counter
assert_type(combined_word_and_integer_keys, "Counter[str | int, int]")
