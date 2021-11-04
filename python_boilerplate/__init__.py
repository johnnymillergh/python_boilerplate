import logging.config
from os import path

logging_conf_path = path.join(path.dirname(path.abspath(__file__)), "../logging.conf")
logging.config.fileConfig(logging_conf_path)
