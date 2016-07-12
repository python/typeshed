#!/usr/bin/env python
"""Test runner for typeshed.

Depends on mypy and pytype being installed.

If mypy is installed:
    1. Parse sys.argv
    2. Compute appropriate arguments for mypy
    3. Stuff those arguments into sys.argv
    4. Run mypy.main('')
    5. Repeat steps 2-4 for other mypy runs (e.g. --py2)

If pytype is installed:
    1. For every pyi, run "pytd <foo.pyi>" in a separate process
"""

import os
import re
import sys
import argparse
import subprocess
import collections

parser = argparse.ArgumentParser(description="Test runner for typeshed. "
                                             "Patterns are unanchored regexps on the full path.")
parser.add_argument('-v', '--verbose', action='count', default=0, help="More output")
parser.add_argument('-n', '--dry-run', action='store_true', help="Don't actually run tests")
parser.add_argument('-x', '--exclude', type=str, nargs='*', help="Exclude pattern")
parser.add_argument('-p', '--python-version', type=str, action='append',
                    help="These versions only (major[.minor])")
parser.add_argument('filter', type=str, nargs='*', help="Include pattern (default all)")
parser.add_argument('--mypy', action='store_true', help="Run mypy tests")
parser.add_argument('--pytype', action='store_true', help="Run pytype tests")
parser.add_argument('--num-parallel', type=int, default=1,
                    help="Number of test processes to spawn")


def log(args, *varargs):
    if args.verbose >= 2:
        print(" ".join(str(arg) for arg in varargs))


def match(args, fn):
    if not args.filter and not args.exclude:
        log(args, fn, 'accept by default')
        return True
    if args.exclude:
        for f in args.exclude:
            if re.search(f, fn):
                log(args, fn, 'excluded by pattern', f)
                return False
    if args.filter:
        for f in args.filter:
            if re.search(f, fn):
                log(args, fn, 'accepted by pattern', f)
                return True
    if args.filter:
        log(args, fn, 'rejected (no pattern matches)')
        return False
    log(args, fn, 'accepted (no exclude pattern matches)')
    return True


def libpath(major, minor):
    versions = ['%d.%d' % (major, minor)
                for minor in reversed(range(minor + 1))]
    versions.append(str(major))
    versions.append('2and3')
    paths = []
    for v in versions:
        for top in ['stdlib', 'third_party']:
            p = os.path.join(top, v)
            if os.path.isdir(p):
                paths.append(p)
    return paths


def main():
    args = parser.parse_args()

    test_funcs = []
    if args.mypy:
        test_funcs.append(mypy_test)
    if args.pytype:
        test_funcs.append(pytype_test)

    if not test_funcs:
        # TODO: use argparse for this logic
        print("Use --mypy or --pytype to run some tests")

    code, runs = 0, 0
    for test_func in test_funcs:
        c, r = test_func(args)
        runs += r
        code = max(code, c)

    if code:
        print("--- exit status %d ---" % code)
        sys.exit(code)
    if not runs:
        print("--- nothing to do; exit 1 ---")
        sys.exit(1)


# Pytype blacklist. Files will not be tested with pytype.
PYTYPE_SKIPPED_FILES = """
  2.7/Cookie.pyi
  2.7/SocketServer.pyi
  2.7/StringIO.pyi
  2.7/__builtin__.pyi
  2.7/__future__.pyi
  2.7/argparse.pyi
  2.7/builtins.pyi
  2.7/calendar.pyi
  2.7/codecs.pyi
  2.7/collections.pyi
  2.7/csv.pyi
  2.7/email/utils.pyi
  2.7/functools.pyi
  2.7/inspect.pyi
  2.7/logging/__init__.pyi
  2.7/os/__init__.pyi
  2.7/platform.pyi
  2.7/resource.pyi
  2.7/rfc822.pyi
  2.7/simplejson/__init__.pyi
  2.7/socket.pyi
  2.7/sqlite3/dbapi2.pyi
  2.7/ssl.pyi
  2.7/subprocess.pyi
  2.7/threading.pyi
  2.7/time.pyi
  2.7/token.pyi
  2.7/types.pyi
  2.7/typing.pyi
  2.7/unittest.pyi
  2.7/urllib2.pyi
  2.7/urlparse.pyi
  2.7/uuid.pyi
  2.7/xml/etree/ElementInclude.pyi
  2.7/xml/etree/ElementPath.pyi
  2.7/xml/etree/ElementTree.pyi
  2and3/cmath.pyi
  2and3/logging/__init__.pyi
  2and3/logging/config.pyi
  2and3/logging/handlers.pyi
  2and3/math.pyi
  2and3/warnings.pyi
  2and3/webbrowser.pyi
"""

# These cause problems for different reasons from above
PYTYPE_SKIPPED_FILES += """
  2.7/_functools.pyi
  2.7/array.pyi
  2.7/ast.pyi
  2.7/encodings/utf_8.pyi
  2.7/fcntl.pyi
  2.7/itertools.pyi
  2.7/json.pyi
  2.7/multiprocessing/process.pyi
  2.7/pickle.pyi
  2.7/tempfile.pyi
  2and3/argparse.pyi
  2and3/bz2.pyi
"""

class PytdRun(object):
    def __init__(self, args, dry_run=False):
        self.args = args
        self.dry_run = dry_run
        self.results = None

        if dry_run:
            self.results = (0, "", "")
        else:
            self.proc = subprocess.Popen(
                ["pytd"] + args,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)

    def communicate(self):
        if self.results:
            return self.results

        stdout, stderr = self.proc.communicate()
        self.results = self.proc.returncode, stdout, stderr
        return self.results


def pytype_test(args):
    # TODO(acaceres): look at args like filter, exclude, verbose

    try:
        PytdRun(["-h"]).communicate()
    except OSError:
        print("Cannot run pytd. Did you install pytype?")
        return 0, 0

    wanted = re.compile(r"stdlib/(2\.7|2and3)/.*\.pyi$")
    skipped = re.compile("(%s)$" % "|".join(PYTYPE_SKIPPED_FILES.split()))
    files = []

    for root, _, filenames in os.walk("stdlib"):
        for f in sorted(filenames):
            f = os.path.join(root, f)
            if wanted.search(f) and not skipped.search(f):
                files.append(f)

    running_tests = collections.deque()
    max_code, runs, errors = 0, 0, 0
    print("Running pytype tests...")
    while 1:
        while files and len(running_tests) < args.num_parallel:
            test_run = PytdRun([files.pop()], dry_run=args.dry_run)
            running_tests.append(test_run)

        if not running_tests:
            break

        test_run = running_tests.popleft()
        code, stdout, stderr = test_run.communicate()
        max_code = max(max_code, code)
        runs += 1

        if code:
            print("pytd error processing \"%s\":" % test_run.args[0])
            print(stderr)
            errors += 1

    print("Ran pytype with %d pyis, got %d errors." % (runs, errors))
    return max_code, runs


def mypy_test(args):
    try:
        from mypy.main import main as mypy_main
    except ImportError:
        print("Cannot import mypy. Did you install it?")
        return 0, 0

    versions = [(3, 5), (3, 4), (3, 3), (3, 2), (2, 7)]
    if args.python_version:
        versions = [v for v in versions
                    if any(('%d.%d' % v).startswith(av) for av in args.python_version)]
        if not versions:
            print("--- no versions selected ---")
            return 0, 0

    code = 0
    runs = 0
    for major, minor in versions:
        roots = libpath(major, minor)
        files = []
        seen = {'__builtin__', 'builtins', 'typing'}  # Always ignore these.
        for root in roots:
            names = os.listdir(root)
            for name in names:
                full = os.path.join(root, name)
                mod, ext = os.path.splitext(name)
                if mod in seen:
                    continue
                if ext in ['.pyi', '.py']:
                    if match(args, full):
                        seen.add(mod)
                        files.append(full)
                elif (os.path.isfile(os.path.join(full, '__init__.pyi')) or
                      os.path.isfile(os.path.join(full, '__init__.py'))):
                    for r, ds, fs in os.walk(full):
                        ds.sort()
                        fs.sort()
                        for f in fs:
                            m, x = os.path.splitext(f)
                            if x in ['.pyi', '.py']:
                                fn = os.path.join(r, f)
                                if match(args, fn):
                                    seen.add(mod)
                                    files.append(fn)
        if files:
            runs += 1
            flags = ['--python-version', '%d.%d' % (major, minor)]
            sys.argv = ['mypy'] + flags + files
            if args.verbose:
                print("running", ' '.join(sys.argv))
            else:
                print("running mypy", ' '.join(flags), "# with", len(files), "files")
            try:
                if not args.dry_run:
                    mypy_main('')
            except SystemExit as err:
                code = max(code, err.code)

    return code, runs


if __name__ == '__main__':
    main()
