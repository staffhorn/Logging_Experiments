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
FILENAME='logs/example.log'

CUSTOM_LEVEL = logging.DEBUG

def configure_logger() -> logging.Logger:
    logger = logging.getLogger(name=__name__)
    logger.setLevel(CUSTOM_LEVEL)

    '''
    We add two handlers to logger
    - one for the screen (debug and above)
    - one for a file (info and above).
    '''

    formatter = logging.Formatter(fmt=FORMAT)

    screen_handler = logging.StreamHandler()
    screen_handler.setLevel(CUSTOM_LEVEL)
    logger.addHandler(screen_handler)

    file_handler = logging.FileHandler(filename=FILENAME, mode='a')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger

if __name__ == "__main__":
    logging.basicConfig(level=CUSTOM_LEVEL)
    logger = configure_logger()
    logger.debug("Helpful debugging goes to screen if debugging turned on.")
    logger.info("Info messages go to screen and file")
