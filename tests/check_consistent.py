import os
import filecmp

consistent_files = [
    ('stdlib/2/builtins.pyi', 'stdlib/2/__builtin__.pyi'),
    ('stdlib/2/SocketServer.pyi', 'stdlib/3/socketserver.pyi'),
    ('stdlib/2/os2emxpath.pyi', 'stdlib/2/posixpath.pyi'),
    ('stdlib/2/ntpath.pyi', 'stdlib/2/posixpath.pyi'),
    ('stdlib/2/macpath.pyi', 'stdlib/2/posixpath.pyi'),
    ('stdlib/3/ntpath.pyi', 'stdlib/3/posixpath.pyi'),
    ('stdlib/3/macpath.pyi', 'stdlib/3/posixpath.pyi'),
    ('stdlib/3.4/enum.pyi', 'third_party/3/enum.pyi'),
]

def main():
    no_symlink = 'You cannot use symlinks in typeshed, please copy the contents of {} into {}'
    for file1, file2 in consistent_files:
        f1 = os.path.join(os.getcwd(), file1)
        f2 = os.path.join(os.getcwd(), file2)
        if os.path.islink(f1):
            raise ValueError(no_symlink.format(file1, file2))
        elif os.path.islink(f2):
            raise ValueError(no_symlink.format(file2, file1))
        else:
            if not filecmp.cmp(f1, f2):
                raise ValueError('File {f1} does not match file {f2}. Please copy it to {f2}'.format(f1=file1, f2=file2))

if __name__ == '__main__':
    main()