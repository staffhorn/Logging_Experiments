"""
 Copyright 2022 "Holistic Mathematics Agency".
 SPDX-License-Identifier: Apache-2.0
"""

'''
Example 02a
Display the logging configuration of example 02 with  the logging_tree module.
'''

import logging
from logging_tree import printout

LOGGING_LEVEL = logging.DEBUG

logging.basicConfig(level=LOGGING_LEVEL, format='')
logging.info('\n\n Basic config: root logger, Stream Handler, output just the message to stderr.\n')
printout()