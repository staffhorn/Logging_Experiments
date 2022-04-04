"""
 Copyright 2022 "Holistic Mathematics Agency".
 SPDX-License-Identifier: Apache-2.0
"""

import logging

FORMAT = '"%(asctime)s",%(module)s,%(name)s,%(levelname)s,"%(message)s"'
FILENAME='logs/example.log'

def example_file_logger():
    logger = logging.getLogger(name=__name__)
    '''
    We completely customize our logger to log formatted and annoted messages to a file.
    '''
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(filename=FILENAME, mode='a')
    formatter = logging.Formatter(fmt=FORMAT)
    handler.setFormatter(fmt=formatter)
    logger.addHandler(hdlr=handler)

    return logger


if __name__ == "__main__":
    logger = example_file_logger()
    logger.info("Let's see what got logged, ok?")
