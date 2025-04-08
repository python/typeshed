import logging
import types

import click
import flask
import jinja2

jinja_env: jinja2.Environment
script_file: str | None
click_root_cmd: str | None
OUTPUT_FOLDER: str
_flask_app: flask.Flask | None
logger: logging.Logger | None

def create_click_web_app(module: types.ModuleType, command: click.BaseCommand, root: str = "/") -> flask.Flask: ...
