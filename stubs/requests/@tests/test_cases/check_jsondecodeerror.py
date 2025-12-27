import requests
from requests.exceptions import JSONDecodeError

try:
    requests.get("https://httpbin.org/html")
except JSONDecodeError as exc:
    print(f"Error. doc: {exc.doc}, msg: {exc.msg}, pos: {exc.pos}")
