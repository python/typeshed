#!/usr/bin/env python3

# For various reasons we need the contents of certain files to be
# duplicated in two places, for example stdlib/2and3/builtins.pyi and
# stdlib/2/__builtin__.pyi must be identical.  In the past we used
# symlinks but that doesn't always work on Windows, so now you must
# manually update both files, and this test verifies that they are
# identical.  The list below indicates which sets of files must match.

import os
import filecmp

consistent_files = [
    {'stdlib/2and3/builtins.pyi', 'stdlib/2/__builtin__.pyi'},
    {'stdlib/2/SocketServer.pyi', 'stdlib/3/socketserver.pyi'},
    {'stdlib/2/os2emxpath.pyi', 'stdlib/2and3/posixpath.pyi',
     'stdlib/2and3/ntpath.pyi', 'stdlib/2and3/macpath.pyi',
     'stdlib/2/os/path.pyi', 'stdlib/3/os/path.pyi'},
    {'stdlib/3/enum.pyi', 'third_party/2/enum.pyi'},
    {'stdlib/3/unittest/mock.pyi', 'third_party/2and3/mock.pyi'},
    {'stdlib/3/concurrent/__init__.pyi', 'third_party/2/concurrent/__init__.pyi'},
    {'stdlib/3/concurrent/futures/__init__.pyi', 'third_party/2/concurrent/futures/__init__.pyi'},
    {'stdlib/3/concurrent/futures/_base.pyi', 'third_party/2/concurrent/futures/_base.pyi'},
    {'stdlib/3/concurrent/futures/thread.pyi', 'third_party/2/concurrent/futures/thread.pyi'},
    {'stdlib/3/concurrent/futures/process.pyi', 'third_party/2/concurrent/futures/process.pyi'},
    {'stdlib/3.7/dataclasses.pyi', 'third_party/3/dataclasses.pyi'},
    {'stdlib/3/pathlib.pyi', 'third_party/2/pathlib2.pyi'},
    {'stdlib/3.7/contextvars.pyi', 'third_party/3/contextvars.pyi'},
]

def main():
    files = [os.path.join(root, file) for root, dir, files in os.walk('.') for file in files]
    no_symlink = 'You cannot use symlinks in typeshed, please copy {} to its link.'
    for file in files:
        _, ext = os.path.splitext(file)
        if ext == '.pyi' and os.path.islink(file):
            raise ValueError(no_symlink.format(file))
    for file1, *others in consistent_files:
        f1 = os.path.join(os.getcwd(), file1)
        for file2 in others:
            f2 = os.path.join(os.getcwd(), file2)
            if not filecmp.cmp(f1, f2):
                raise ValueError('File {f1} does not match file {f2}. Please copy it to {f2}'.format(f1=file1, f2=file2))

if __name__ == '__main__':
    main()
