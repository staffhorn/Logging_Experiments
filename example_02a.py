"""
 Copyright 2022 "Holistic Mathematics Agency".
 SPDX-License-Identifier: Apache-2.0
"""

'''
Example 02a
Change logging level to suppress debugging messages.
'''

import logging

LOGGING_LEVEL = logging.INFO

logging.basicConfig(level=LOGGING_LEVEL, format='')
logging.debug('This debug uses the root logger to send simple messages.')
