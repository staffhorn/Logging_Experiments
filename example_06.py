"""
 Copyright 2022 "Holistic Mathematics Agency".
 SPDX-License-Identifier: Apache-2.0
"""

import logging

'''
Example 06
Customize our logger with a file handler and a formatter.
'''

FORMAT = '"%(asctime)s",%(module)s,%(name)s,%(levelname)s,"%(message)s"'
FILENAME='logs/example.log'

def configure_handler() -> logging.Handler:
    '''
    We customize our logger with a logging.Handler:
     - set level to DEBUG
     - create a custom formatter
     - send log messages to a file.
    '''
    
    handler = logging.FileHandler(filename=FILENAME, mode='a')
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(fmt=logging.Formatter(FORMAT))
    return handler


if __name__ == "__main__":
    logger = logging.getLogger()
    logger.addHandler(configure_handler())
    logger.debug("Let's see what got logged, ok?")
