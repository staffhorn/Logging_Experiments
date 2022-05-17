"""
 Copyright 2022 "Holistic Mathematics Agency".
 SPDX-License-Identifier: Apache-2.0
"""

'''
Example 06a
import example_06 as a module.
'''

import logging
import example_06

example_06.FILENAME='logs/example_06a.log'
example_06.example_06_work()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(example_06.configure_handler())
logger.info('We can use example 06 configuration for a new logger.')