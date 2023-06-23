import logging
import time

class _UTCFormatter(logging.Formatter):
    converter = time.gmtime

def get_logger(): ...
