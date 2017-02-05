import pytest
import sys
import os


def main():
    if sys.version_info < (3, 0):
        version_dirs = [
            '2and3',
            '2',
        ]
    else:
        version_dirs = [
            '2and3',
            '3',
            '%d.%d' % (sys.version_info[0], sys.version_info[1]),
        ]
    top_dirs = ['stdlib', 'third_party']
    possible_paths = [os.path.join('test_data', t, v)
                      for t in top_dirs
                      for v in version_dirs]
    print(possible_paths)
    paths = [path for path in possible_paths if os.path.exists(path)]
    print(paths)
    pytest.main(paths)


if __name__ == '__main__':
    main()
