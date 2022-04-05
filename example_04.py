"""
 Copyright 2022 "Holistic Mathematics Agency".
 SPDX-License-Identifier: Apache-2.0
"""

import logging

'''
Example 04
Annotate our logs with a custom formatter.

NOTES:
Configure the root logger with a nice format.
Create a custom logger with a level of DEBUG, and a name of __name__, which in this case is "__main__".
Notice we didn't give the custom logger a format, so it inherits the format of the root logger. 
'''

FORMAT = '"%(asctime)s",%(module)s,%(name)s,%(levelname)s,"%(message)s"'
LOGGING_LEVEL = logging.DEBUG

def configure_logger() :
    logger = logging.getLogger(__name__)
    logger.setLevel(LOGGING_LEVEL)
    return logger



if __name__=="__main__":
    # Configure the root logger, set to the level of INFO, and will filter out debug messages.

    logging.basicConfig(level=logging.INFO, format=FORMAT)

    # Now configure a custom logger, and set it to DEBUG.
    # Inherit the custom format from the root logger.

    logger = configure_logger()
    logger.debug('The custom logger is set to a level of DEBUG.')

    # Since the root logger is set to INFO, debug messages will not print.

    logging.debug('We will not see this.')