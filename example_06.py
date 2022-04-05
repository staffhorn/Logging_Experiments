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

def configure_logger() -> logging.Logger:
    '''
    We customize our logger:
     - set level to DEBUG
     - create a custom formatter
     - create a custom handler to send log messages to a file.
    '''

    logger = logging.getLogger()
    handler = logging.FileHandler(filename=FILENAME, mode='a')
    formatter = logging.Formatter(fmt=FORMAT)
    handler.setFormatter(fmt=formatter)
    logger.addHandler(hdlr=handler)
    return logger


if __name__ == "__main__":
    logger = configure_logger()
    logger.setLevel(logging.DEBUG)
    logger.debug("Let's see what got logged, ok?")
