"""
 Copyright 2022 "Holistic Mathematics Agency".
 SPDX-License-Identifier: Apache-2.0
"""

'''
Example 02a
Change logging level INFO to suppress DEBUG messages.
'''

import logging

logging.basicConfig(level=logging.INFO)

logging.debug('This debug uses the root logger.')
