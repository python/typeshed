from argparse import _ActionsContainer, FileType

container = _ActionsContainer("", "", "", "")

container.add_argument("--foo")
container.add_argument("--foo", choices=[""])
container.add_argument("--foo", choices=[1, 2, 3])  # type: ignore

container.add_argument("--foo", type=int)
container.add_argument("--foo", type=int, choices=[1, 2, 3])
container.add_argument("--foo", type=int, choices=[""])  # type: ignore

container.add_argument("--foo", type="")
container.add_argument("--foo", type="", choices=[1, 2, 3])
container.add_argument("--foo", type="", choices=[""])

container.add_argument("--foo", type=FileType())
container.add_argument("--foo", type=FileType(), choices=[""])  # type: ignore
