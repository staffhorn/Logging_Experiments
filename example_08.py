"""
 Copyright 2022 "Holistic Mathematics Agency".
 SPDX-License-Identifier: Apache-2.0
"""
import logging
from logging_tree import printout
from example_07 import configure_logger

LOGGING_LEVEL = logging.DEBUG

if __name__=="__main__":
    logging.basicConfig(level=LOGGING_LEVEL)
    logger = configure_logger()
    printout()
