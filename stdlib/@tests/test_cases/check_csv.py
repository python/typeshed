import csv
import io
import sys
from typing_extensions import assert_type

if sys.version_info >= (3, 12):
    reader = csv.DictReader(io.StringIO("1,2"), fieldnames=iter(["a", "b"]))
    writer = csv.DictWriter(io.StringIO(), fieldnames=iter(["a", "b"]))
    assert_type(reader, csv.DictReader[str])
    assert_type(writer, csv.DictWriter[str])
