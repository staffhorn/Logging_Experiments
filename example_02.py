"""
 Copyright 2022 "Holistic Mathematics Agency".
 SPDX-License-Identifier: Apache-2.0
"""

import logging

'''
Example 02
Log to the screen with the root logger.

NOTES:
This is just as easy to set up and use as print().
'''

LOGGING_LEVEL = logging.DEBUG
logging.basicConfig(level=LOGGING_LEVEL,format='')


logging.debug('This debug uses the root logger to send simple messages.')