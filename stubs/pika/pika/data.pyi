from pika.compat import PY2 as PY2, basestring as basestring

def encode_short_string(pieces, value): ...
def decode_short_string(encoded, offset): ...
def encode_table(pieces, table): ...
def encode_value(pieces, value): ...
def decode_table(encoded, offset): ...
def decode_value(encoded, offset): ...
