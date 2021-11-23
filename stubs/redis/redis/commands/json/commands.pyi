from typing import Any

class JSONCommands:
    def arrappend(self, name, path=..., *args): ...
    def arrindex(self, name, path, scalar, start: int = ..., stop: int = ...): ...
    def arrinsert(self, name, path, index, *args): ...
    def arrlen(self, name, path=...): ...
    def arrpop(self, name, path=..., index: int = ...): ...
    def arrtrim(self, name, path, start, stop): ...
    def type(self, name, path=...): ...
    def resp(self, name, path=...): ...
    def objkeys(self, name, path=...): ...
    def objlen(self, name, path=...): ...
    def numincrby(self, name, path, number): ...
    def nummultby(self, name, path, number): ...
    def clear(self, name, path=...): ...
    def delete(self, key, path=...): ...
    forget = delete
    def get(self, name, *args, no_escape: bool = ...): ...
    def mget(self, keys, path): ...
    def set(self, name, path, obj, nx: bool = ..., xx: bool = ..., decode_keys: bool = ...): ...
    def strlen(self, name, path: Any | None = ...): ...
    def toggle(self, name, path=...): ...
    def strappend(self, name, value, path=...): ...
    def debug(self, subcommand, key: Any | None = ..., path=...): ...
    def jsonget(self, *args, **kwargs): ...
    def jsonmget(self, *args, **kwargs): ...
    def jsonset(self, *args, **kwargs): ...
