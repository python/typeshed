#!/usr/bin/env python
"""Test runner for typeshed.

Depends on mypy and pytype being installed.

If pytype is installed:
    1. For every pyi, do nothing if it is in pytype_blacklist.txt.
    2. If the blacklist line has a "# parse only" comment run
      "pytd <foo.pyi>" in a separate process.
    3. If the file is not in the blacklist run
      "pytype --typeshed-location=typeshed_location --module-name=foo \
      --convert-to-pickle=tmp_file <foo.pyi>.
Option two will parse the file, mostly syntactical correctness. Option three
will load the file and all the builtins, typeshed dependencies. This will
also discover incorrect usage of imported modules.
"""

import os
import re
import sys
import argparse
import subprocess
import tempfile
import collections

parser = argparse.ArgumentParser(description="Pytype tests.")
parser.add_argument('-n', '--dry-run', action='store_true', help="Don't actually run tests")
parser.add_argument('--num-parallel', type=int, default=1,
                    help="Number of test processes to spawn")


def main():
    args = parser.parse_args()
    code, runs = pytype_test(args)

    if code:
        print("--- exit status %d ---" % code)
        sys.exit(code)
    if not runs:
        print("--- nothing to do; exit 1 ---")
        sys.exit(1)

_PARSE_ONLY_REGEX = r"\s*#\s*parse only\s*"

def load_blacklist():
    filename = os.path.join(os.path.dirname(__file__), "pytype_blacklist.txt")
    regex = r"^\s*([^\s#]+(?:%s)?)\s*(?:#.*)?$" % _PARSE_ONLY_REGEX
    with open(filename) as f:
        lines = re.findall(regex, f.read(), flags=re.M)
    blacklist = []
    parse_only = []
    parse_only_re = re.compile(_PARSE_ONLY_REGEX)
    for f in lines:
        if parse_only_re.search(f):
            parse_only.append(f.split("#")[0].strip())
        else:
            blacklist.append(f)
    return blacklist, parse_only


class BinaryRun(object):
    def __init__(self, args, dry_run=False, close_handler=None):
        self.args = args

        self.dry_run = dry_run
        self.results = None

        if dry_run:
            self.results = (0, "", "")
        else:
            self.proc = subprocess.Popen(
                self.args,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)

        if close_handler:
              close_handler()

    def communicate(self):
        if self.results:
            return self.results

        stdout, stderr = self.proc.communicate()
        self.results = self.proc.returncode, stdout, stderr
        return self.results


def pytype_test(args):
    try:
        BinaryRun(["pytd", "-h"]).communicate()
    except OSError:
        print("Cannot run pytd. Did you install pytype?")
        return 0, 0

    blacklist, parse_only = load_blacklist()
    wanted = re.compile(r"stdlib/.*\.pyi$")
    skipped = re.compile("(%s)$" % "|".join(blacklist))
    parse_only = re.compile("(%s)$" % "|".join(parse_only))

    pytype_run = []
    pytd_run = []

    for root, _, filenames in os.walk("stdlib"):
        for f in sorted(filenames):
            f = os.path.join(root, f)
            if wanted.search(f):
                if parse_only.search(f):
                    pytd_run.append(f)
                elif not skipped.search(f):
                    pytype_run.append(f)

    running_tests = collections.deque()
    max_code, runs, errors = 0, 0, 0
    files = pytype_run + pytd_run
    while 1:
        while files and len(running_tests) < args.num_parallel:
            f = files.pop()
            if f in pytype_run:
                temp = tempfile.NamedTemporaryFile(delete=False)
                temp.close()  # Windows compat.
                test_run = BinaryRun(["pytype",
                                      "--typeshed-location=%s" % os.getcwd(),
                                      "--module-name=%s" % _get_module_name(f),
                                      '--convert-to-pickle=%s' % temp.name,
                                      f],
                                      dry_run=args.dry_run,
                                      close_handler=lambda: os.remove(temp.name)
                )
            elif f in pytd_run:
                test_run = BinaryRun(["pytd", f], dry_run=args.dry_run)
            else:
                raise ValueError("Unknown action for file: %s" % f)
            running_tests.append(test_run)

        if not running_tests:
            break

        test_run = running_tests.popleft()
        code, stdout, stderr = test_run.communicate()
        max_code = max(max_code, code)
        runs += 1

        if code:
            print(stderr)
            errors += 1

    print("Ran pytype with %d pyis, got %d errors." % (runs, errors))
    return max_code, runs

def _get_module_name(filename):
    """Converts a filename stdblib/m.n/module/foo to module.foo."""
    return ".".join(filename.split(os.path.sep)[2:]).replace(
        ".pyi", "").replace('.__init__', '')

if __name__ == '__main__':
    main()
