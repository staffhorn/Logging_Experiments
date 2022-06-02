"""
 Copyright 2022 "Holistic Mathematics Agency".
 SPDX-License-Identifier: Apache-2.0
"""

'''
Example 02
Log to the screen with the root logger.

NOTES:
This is almost as easy to set up and use as print().
'''

import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug('This debug message uses the root logger.')