import re

romanNumeralMap: tuple[tuple[str, int],...]

def toRoman(n: int) -> str: ...

romanNumeralPattern: re.Pattern[str]

def fromRoman(s: str) -> int: ...
