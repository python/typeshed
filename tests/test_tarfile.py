import tarfile

with tarfile.open("test.tar.xz", "w:xz") as tar:
    pass

# Test with valid preset values
for preset in range(10):
    with tarfile.open("test.tar.xz", "w:xz", preset=preset) as tar:
        pass

# Test with invalid preset values
try:
    with tarfile.open("test.tar.xz", "w:xz", preset=-1) as tar:
        pass
except ValueError:
    pass

try:
    with tarfile.open("test.tar.xz", "w:xz", preset=10) as tar:
        pass
except ValueError:
    pass

# try:
#     with tarfile.open("test.tar.xz", "w:xz", preset="high") as tar:
#         pass
# except TypeError:
#     pass
#
# try:
#     with tarfile.open("test.tar.xz", "w:xz", preset=5.5) as tar:
#         pass
# except TypeError:
#     pass

# Test with modes that don't support preset
try:
    with tarfile.open("test.tar.xz", "r", preset=5) as tar:
        pass
except tarfile.TarError:
    pass

try:
    with tarfile.open("test.tar.xz", "w", preset=5) as tar:
        pass
except tarfile.TarError:
    pass
