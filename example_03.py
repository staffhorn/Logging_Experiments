"""
 Copyright 2022 "Holistic Mathematics Agency".
 SPDX-License-Identifier: Apache-2.0
"""

import logging


'''
Example 03
Add formatting to the root logger with logging.basicConfig() and a custom format string.
'''

LOGGING_LEVEL = logging.INFO
FORMAT = '"%(asctime)s",%(module)s,%(name)s,%(levelname)s,"%(message)s"'

logging.basicConfig(level=LOGGING_LEVEL, format=FORMAT)
logging.info('This uses the root logger with a custom format, adding context information to each message.')
