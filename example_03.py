"""
 Copyright 2022 "Holistic Mathematics Agency".
 SPDX-License-Identifier: Apache-2.0
"""

import logging


'''
Example 03
Add formatting to the root logger with logging.basicConfig()

NOTES:
With basicConfig() we can easily annotate each log message with a the root logger's formatter. 
Here we add a timestamp, information about the software and the logger, and the level of the message.
'''

FORMAT = '"%(asctime)s",%(module)s,%(name)s,%(levelname)s,"%(message)s"'
logging.basicConfig(level=logging.INFO, format=FORMAT)
logging.info('This uses the root logger with formatting. Note the information logging adds for us.')
