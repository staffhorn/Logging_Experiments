"""
 Copyright 2022 "Holistic Mathematics Agency".
 SPDX-License-Identifier: Apache-2.0
"""

import logging

'''
Example 12
Logging configuration with logging.dictConfig
'''

LOGGING_CONFIG = '''
version: 1
formatters:
    simple:
        format: '"%(asctime)s",%(module)s,%(name)s,%(levelname)s,"%(message)s"'
handlers:
    console:
        class: logging.StreamHandler
        level: DEBUG
        formatter: simple
        stream: ext://sys.stdout
loggers:
    
    

'''