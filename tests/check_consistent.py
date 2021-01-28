#!/usr/bin/env python3

# For security (and simplicity) reasons, only a limited kind of files can be
# present in /stdlib and /stubs directories, see README for detail. Here we
# verify these constraints.

# In addition, for various reasons we need the contents of certain files to be
# duplicated in two places, for example stdlib/@python2/builtins.pyi and
# stdlib/@python2/__builtin__.pyi must be identical.  In the past we used
# symlinks but that doesn't always work on Windows, so now you must
# manually update both files, and this test verifies that they are
# identical.  The list below indicates which sets of files must match.

import filecmp
import os

consistent_files = [
    {"stdlib/@python2/builtins.pyi", "stdlib/@python2/__builtin__.pyi"},
    {"stdlib/threading.pyi", "stdlib/_dummy_threading.pyi"},
]


def assert_stubs_only(directory):
    """Check that given directory contains only valid stub files."""
    top = directory.split(os.sep)[-1]
    assert top.isidentifier(), "Bad directory name: {}".format(top)
    for _, dirs, files in os.walk(directory):
        for file in files:
            name, ext = os.path.splitext(file)
            assert name.isidentifier(), "Files must be valid modules"
            assert ext == ".pyi", "Only stub flies allowed. Got: {} in {}".format(file, directory)
        for subdir in dirs:
            assert subdir.isidentifier(), "Directories must be valid packages"


def check_stdlib():
    for entry in os.listdir("stdlib"):
        if os.path.isfile(os.path.join("stdlib", entry)):
            name, ext = os.path.splitext(entry)
            if ext != ".pyi":
                assert entry == "VERSIONS", "Unexpected file in stdlib root: {}".format(entry)
            assert name.isidentifier(), "Bad file name in stdlib"
        else:
            if entry == "@python2":
                continue
            assert_stubs_only(os.path.join("stdlib", entry))
    for entry in os.listdir("stdlib/@python2"):
        if os.path.isfile(os.path.join("stdlib/@python2", entry)):
            name, ext = os.path.splitext(entry)
            assert name.isidentifier(), "Bad file name in stdlib"
            assert ext == ".pyi", "Unexpected file in stdlib/@python2 root"
        else:
            assert_stubs_only(os.path.join("stdlib/@python2", entry))


def check_stubs():
    for distribution in os.listdir("stubs"):
        assert not os.path.isfile(distribution), "Only directories allowed in stubs"
        for entry in os.listdir(os.path.join("stubs", distribution)):
            if os.path.isfile(os.path.join("stubs", distribution, entry)):
                name, ext = os.path.splitext(entry)
                if ext != ".pyi":
                    assert entry in {"METADATA.toml", "README", "README.md", "README.rst"}, entry
                else:
                    assert name.isidentifier(), "Bad file name in stubs"
            else:
                if entry == "@python2":
                    continue
                assert_stubs_only(os.path.join("stubs", distribution, entry))
        if os.path.isdir(os.path.join("stubs", distribution, "@python2")):
            for entry in os.listdir(os.path.join("stubs", distribution, "@python2")):
                if os.path.isfile(os.path.join("stubs", distribution, "@python2", entry)):
                    name, ext = os.path.splitext(entry)
                    assert name.isidentifier(), "Bad file name in stubs"
                    assert ext == ".pyi", "Unexpected file in @python2 stubs"
                else:
                    assert_stubs_only(os.path.join("stubs", distribution, "@python2", entry))


def check_same_files():
    files = [os.path.join(root, file) for root, dir, files in os.walk(".") for file in files]
    no_symlink = "You cannot use symlinks in typeshed, please copy {} to its link."
    for file in files:
        _, ext = os.path.splitext(file)
        if ext == ".pyi" and os.path.islink(file):
            raise ValueError(no_symlink.format(file))
    for file1, *others in consistent_files:
        f1 = os.path.join(os.getcwd(), file1)
        for file2 in others:
            f2 = os.path.join(os.getcwd(), file2)
            if not filecmp.cmp(f1, f2):
                raise ValueError(
                    "File {f1} does not match file {f2}. Please copy it to {f2}\n"
                    "Run either:\ncp {f1} {f2}\nOr:\ncp {f2} {f1}".format(f1=file1, f2=file2)
                )


if __name__ == "__main__":
    check_stdlib()
    check_stubs()
    check_same_files()
