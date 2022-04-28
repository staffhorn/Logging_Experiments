"""
 Copyright 2022 "Holistic Mathematics Agency".
 SPDX-License-Identifier: Apache-2.0
"""

import logging

'''
Example 04
Annotate our logs with a custom formatter.

NOTES:
1. Configure the root logger with a nice format.
2. Create a custom logger with a level of DEBUG, and a name of __name__, which in this case is "__main__".
'''

FORMAT = '"%(asctime)s",%(module)s,%(name)s,%(levelname)s,"%(message)s"'

if __name__=="__main__":
    # Configure the root logger, set to the level of INFO.
    # Logging will dispatch log messages at INFO or above, but
    # will filter out lower (DEBUG) messages.

    logging.basicConfig(level=logging.INFO, format=FORMAT)

    # Now configure a custom logger, and set it to DEBUG.
    # Inherit the custom format from the root logger.

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    logger.debug('The __main__ logger is set to a level of DEBUG, so this message displays.')

    # Since the root logger is set to INFO, this debug message will not appear.\
    logging.debug('We will not see this because DEBUG is lower than INFO.')