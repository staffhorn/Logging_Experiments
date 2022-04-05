"""
 Copyright 2022 "Holistic Mathematics Agency".
 SPDX-License-Identifier: Apache-2.0
"""
import logging
import logging_tree
import example_07

LOGGING_LEVEL = logging.INFO
'''
Example 08
Create a tree view of the logging configuration from Example 07 using the python logging_tree module.'''

if __name__=="__main__":
    logging.basicConfig(level=LOGGING_LEVEL,format="%(message)s")
    logger = example_07.configure_logger()
    logging.info("Here is a view of the logging tree:\n\n")
    logging_tree.printout()
    logging.info("\n\n")
