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

formatter = logging.Formatter(fmt=FORMAT)

def configure_screen_handler() -> logging.Handler:
    '''
    handlers to route messages to stdout and to a file
    '''

    logger = logging.getLogger(name=__name__)
    logger.setLevel(CUSTOM_LEVEL)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(CUSTOM_LEVEL)

    return handler

def configure_file_handler() -> logging.Handler:
    '''
    handlers to route messages to stdout and to a file
    '''
 
    handler = logging.FileHandler(filename=FILENAME, mode='a')
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    return handler

if __name__ == '__main__':
    # The root logger will still go to sys.stderr, since we don't override the default.
    logging.basicConfig(level=CUSTOM_LEVEL, format='%(message)s')  
    logger = logging.getLogger()
    logger.addHandler(configure_screen_handler())
    logger.addHandler(configure_file_handler)

    logging.info('The new tree:\n\n')
    logging_tree.printout()
