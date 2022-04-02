"""
 Copyright 2022 "Holistic Mathematics Agency".
 SPDX-License-Identifier: Apache-2.0
"""

import logging

FORMAT = '%(asctime)s, %(module)s, %(name)s, %(levelname)s, "%(message)s" '

logging.basicConfig(level=logging.INFO, format=FORMAT)
logging.info('This uses the root logger with formatting. Note the information logging adds for us.')
