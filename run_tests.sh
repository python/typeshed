!# /bin/bash


python3 tests/mypy_test.py
python3 tests/pytype_test.py
python3 tests/mypy_selftest.py
python3 tests/stubtest_test.py
flake8
