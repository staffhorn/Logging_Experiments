"""
 Copyright 2022 "Holistic Mathematics Agency".
 SPDX-License-Identifier: Apache-2.0
"""

import logging

'''
Example 07
A logger that sends debug messages to the screen and info messages to a file
'''

FORMAT = '"%(asctime)s",%(module)s,%(name)s,%(levelname)s,"%(message)s"'
FILENAME='logs/example_07.log'
CUSTOM_LEVEL = logging.DEBUG

formatter = logging.Formatter(fmt=FORMAT)

def get_logger() -> logging.getLogger:
    logger =  logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    return logger

def configure_file_handler() -> logging.Handler:

    file_handler = logging.FileHandler(filename=FILENAME, mode='a')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    return file_handler

def configure_screen_handler() -> logging.Handler:
    import sys

    screen_handler = logging.StreamHandler(stream=sys.stdout)
    screen_handler.setLevel(CUSTOM_LEVEL)
    screen_handler.setFormatter(formatter)

    return screen_handler

if __name__ == "__main__":
    logger = get_logger()
    logger.addHandler(configure_screen_handler())
    logger.addHandler(configure_file_handler())

    logger.debug('debug')
    logger.info("Info messages go to screen and file")
