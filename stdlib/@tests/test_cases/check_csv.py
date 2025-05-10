import csv
import sys

csv.writer(open("test.csv", "w"), quoting=csv.QUOTE_ALL)
csv.writer(open("test.csv", "w"), quoting=csv.QUOTE_MINIMAL)
csv.writer(open("test.csv", "w"), quoting=csv.QUOTE_NONE)
csv.writer(open("test.csv", "w"), quoting=csv.QUOTE_NONNUMERIC)

if sys.version_info >= (3, 12):
    csv.writer(open("test.csv", "w"), quoting=csv.QUOTE_STRINGS)
    csv.writer(open("test.csv", "w"), quoting=csv.QUOTE_NOTNULL)


csv.reader(open("test.csv", "r"), quoting=20)  # type: ignore
