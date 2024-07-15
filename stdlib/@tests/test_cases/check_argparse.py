from argparse import ArgumentParser, FileType

parser = ArgumentParser()

parser.add_argument("--foo")
parser.add_argument("--foo", choices=[""])
parser.add_argument("--foo", choices=[1, 2, 3])  # type: ignore

parser.add_argument("--foo", type=int)
parser.add_argument("--foo", type=int, choices=[1, 2, 3])
parser.add_argument("--foo", type=int, choices=[""])  # type: ignore

parser.add_argument("--foo", type="")
parser.add_argument("--foo", type="", choices=[1, 2, 3])
parser.add_argument("--foo", type="", choices=[""])

parser.add_argument("--foo", type=FileType())
parser.add_argument("--foo", type=FileType(), choices=[""])  # type: ignore
