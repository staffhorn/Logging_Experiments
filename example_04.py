"""
 Copyright 2022 "Holistic Mathematics Agency".
 SPDX-License-Identifier: Apache-2.0
"""

import logging

'''
Example 04
Annotate our logs with a custom formatter.


'''

FORMAT = '"%(asctime)s",%(module)s,%(name)s,%(levelname)s,"%(message)s"'

logging.basicConfig(level=logging.INFO, format=FORMAT)

# Let's create a custom logger, my_logger.
my_logger = logging.getLogger(__name__)
my_logger.setLevel(logging.DEBUG)


logging.info('This INFO message sent to the root logger will display.')
logging.debug('We will not see this because DEBUG is lower than the root level INFO.')

my_logger.debug('The __main__ logger is set to a level of DEBUG, so this message displays.')
my_logger.info('Note the __main__ logger uses the format from root.')