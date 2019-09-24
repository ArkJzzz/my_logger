#!usr/bin/python3.7

"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

#############################################################################
#           ToDo
#   Добавить отправку логов в Telegram
#
#
#############################################################################

__author__ = 'ArkJzzz (arkjzzz@gmail.com)'

import sys
import time
import logging
from logging.handlers import RotatingFileHandler


LOG_FILE = 'testing_logging.log'
LOG_FORMAT = '%(asctime)s %(name)s - %(funcName)s:%(lineno)d - %(message)s'
DATE_FORMAT = '%Y-%b-%d %H:%M:%S (%Z)'
FORMATTER = logging.Formatter(
    fmt=LOG_FORMAT, 
    datefmt=DATE_FORMAT,
    )


class CustomHandler(logging.Handler):
    def emit(self, record):
        log_entry = self.format(record)
        # print(f'{log_entry}<<<<<<')
        # send log_entry to telegram

def get_custom_handler():
    custom_handler = CustomHandler()
    custom_handler.setLevel(logging.INFO)
    custom_handler.setFormatter(FORMATTER)
    return custom_handler

def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler

def get_file_handler():
    file_handler = RotatingFileHandler(
        LOG_FILE, 
        maxBytes=10240, 
        backupCount=2,
        )
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(FORMATTER)
    return file_handler

def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())
    logger.addHandler(get_custom_handler())
    logger.propagate = False
    return logger

def main():
    logger = get_logger('Testing logger')

    logger.debug("This is a DEBUG message")
    logger.info("INFO message")
    logger.warning("WARNING message")
    logger.error("An ERROR has happened!")
    logger.critical("CRITICAL message")

if __name__ == '__main__':
    main()