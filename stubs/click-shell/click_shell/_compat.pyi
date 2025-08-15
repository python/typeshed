import click

def get_choices(
    cli: click.Command, prog_name: str, args: list[str], incomplete: str
) -> list[str]: ...
