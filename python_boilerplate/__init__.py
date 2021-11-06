import logging.config
from os import path

logging_conf_path = path.join(path.dirname(path.abspath(__file__)), "logging.conf")
print(f"logging_conf_path = {logging_conf_path}, __file__ = {__file__}")
logging.config.fileConfig(logging_conf_path)
