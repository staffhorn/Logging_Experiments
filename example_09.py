"""
 Copyright 2022 "Holistic Mathematics Agency".
 SPDX-License-Identifier: Apache-2.0
"""

import logging
import logging_tree
import sys

'''
Example 09
A logger that sends debug messages to the screen and info messages to a file.
In example 08, we could see that the default stream for StreamHandler is sys.stderr.
In example 09, we send screen output to sys.stdout
'''

FORMAT = '"%(asctime)s",%(module)s,%(name)s,%(levelname)s,"%(message)s"'
FILENAME='logs/example.log'

CUSTOM_LEVEL = logging.DEBUG

def configure_logger() -> logging.Logger:
    '''
    Create a logger and configure handlers to route messages to stdout and to a file
    '''

    logger = logging.getLogger(name=__name__)
    logger.setLevel(CUSTOM_LEVEL)

    '''
    We add two handlers to logger
    - one for the screen (debug and above)
    - one for a file (info and above).
    '''

    formatter = logging.Formatter(fmt=FORMAT)

    screen_handler = logging.StreamHandler(sys.stdout)
    screen_handler.setLevel(CUSTOM_LEVEL)
    logger.addHandler(screen_handler)

    file_handler = logging.FileHandler(filename=FILENAME, mode='a')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger

if __name__ == '__main__':
    # The root logger will still go to sys.stderr, since we don't override the default.
    logging.basicConfig(level=CUSTOM_LEVEL, format='%(message)s')  
    logger = configure_logger()
    logging.info('The new tree:\n\n')
    logging_tree.printout()
