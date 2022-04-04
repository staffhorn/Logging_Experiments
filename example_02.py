"""
 Copyright 2022 "Holistic Mathematics Agency".
 SPDX-License-Identifier: Apache-2.0
"""

import logging

'''
Example 02
Log to the screen with the root logger.

NOTES:
The logging module sets up a very basic root logger for us automatically.
We access the root logger with logging level calls, logging.basicConfig() and logging.debug()
In this case, we change the level to DEBUG.  We will talk about levels later.
This is about as easy to set up and use as print(), and easier when we deploy to operations,
we'll see.
'''

logging.basicConfig(level=logging.DEBUG)
logging.debug('This uses the root logger.')