"""
 Copyright 2022 "Holistic Mathematics Agency".
 SPDX-License-Identifier: Apache-2.0
"""

import logging
from operator import le

'''
Example 06
Customize our logger with a file handler and a formatter.
'''

FORMAT = '"%(asctime)s",%(module)s,%(name)s,%(levelname)s,"%(message)s"'
FILENAME='logs/example_06.log'
LEVEL=logging.DEBUG

my_logger = None

def get_logger() -> logging.getLogger:
    if my_logger is None:
        logger =  logging.getLogger(__name__)
        logger.setLevel(LEVEL)
    else:
        logger = my_logger
    return logger

def configure_handler() -> logging.Handler:
    '''
    We customize our logger with a logging.Handler:
     - set level to DEBUG
     - create a custom formatter
     - send log messages to a file.
    '''
    
    handler = logging.FileHandler(filename=FILENAME, mode='a')
    handler.setLevel(LEVEL)
    handler.setFormatter(fmt=logging.Formatter(FORMAT))
    return handler


def example_06_work():
    logger = get_logger()
    logger.addHandler(configure_handler())
    logger.debug(f"Debug messages go to the file {FILENAME}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    example_06_work()
