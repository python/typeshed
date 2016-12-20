#!/bin/sh

./tests/mypy_test.py
./tests/pytype_test.py

# FIXME: Enable when errors listed in `.flake8` are fixed in all stub files.
# find . -name "*.pyi" | xargs -s 1024 flake8 --builtins=StandardError,apply,basestring,buffer,cmp,coerce,execfile,file,intern,long,raw_input,reduce,reload,unichr,unicode,xrange
