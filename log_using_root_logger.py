"""
 Copyright 2022 "Holistic Mathematics Agency".
 SPDX-License-Identifier: Apache-2.0
"""

import logging

'''
The logging module sets up the root logger for us, but we can easily modify some of its properties.
'''
logging.basicConfig(level=logging.INFO)
logging.info('This uses the root logger.')