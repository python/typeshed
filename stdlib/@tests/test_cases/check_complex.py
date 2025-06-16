import sys


class WithComplex:
    def __init__(self, value: complex) -> None:
        self.value = value

    def __complex__(self) -> complex:
        return self.value


complex()
complex(10)
complex(4.0)
# Complex is only supported for the single argument form.
complex(4.25 + 0j)
complex(4.25 + 0j, 0)
# Str should also work
complex("1+2j")
complex("1+2j", 0)

# Second argument must be a concrete complex number.
complex(0, WithComplex(4.25 + 0j))  # type: ignore
# Str isn't supported as a key-word argument.
complex(real="1+2j", imag=0)  # type: ignore


if sys.version_info >= (3, 14):
    # All deprecated in 3.14.
    complex(real=34 + 0j)  # type: ignore
    complex(real=34 + 0j, imag=34 + 0j)  # type: ignore
    complex(real=3, imag=34 + 0j)  # type: ignore
