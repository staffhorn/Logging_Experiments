"""
 Copyright 2022 "Holistic Mathematics Agency".
 SPDX-License-Identifier: Apache-2.0
"""

import logging


FORMAT = '"%(asctime)s",%(module)s,%(name)s,%(levelname)s,"%(message)s"'

# Configure the root logger, set to the level of INFO, and will filter out debug messages.
logging.basicConfig(level=logging.INFO, format=FORMAT)

'''
Create a custom logger with a level of DEBUG, and a name of __name__ which in this case is "__main__".
Notice we didn't give the custom logger a format (with a custom formatter), so it inherits the format of the root logger. 
'''
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.debug('The custom logger is set to a level of DEBUG.')
