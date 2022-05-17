"""
 Copyright 2022 "Holistic Mathematics Agency".
 SPDX-License-Identifier: Apache-2.0
"""

import logging
from logging.config import dictConfig
import yaml
import os

'''
Example 12
Logging configuration with logging.dictConfig
'''

with open('example_12.yaml','r') as config_file:
    my_config = yaml.load(config_file, yaml.Loader)

my_config['handlers']['email']['credentials'] = (os.environ['gmail_app_sender'], os.environ['gmail_app_pass'])
dictConfig(my_config)
del my_config

logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')