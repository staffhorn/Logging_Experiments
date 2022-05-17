"""
 Copyright 2022 "Holistic Mathematics Agency".
 SPDX-License-Identifier: Apache-2.0
"""

import logging
from logging.handlers import SMTPHandler
import os
from example_07 import configure_file_handler
from example_09 import configure_smtp_handler


'''
Example 10
Using time module to see which logging handlers take a long time.
'''

import logging
from time import perf_counter
import sys


def time_logger(logger: logging.Logger, level:int, message:str) -> float:
    '''
    time_logger
    measures the time taken to log a message
    '''
    tic = perf_counter()
    logger.log(level, message)
    toc = perf_counter()
    return toc-tic

if __name__=='__main__':
    logging.basicConfig(format='', level=logging.DEBUG, stream=sys.stdout)


    file_logger = logging.getLogger('File')
    file_logger.setLevel(logging.INFO)
    file_logger.addHandler(configure_file_handler())
    smtp_logger = logging.getLogger('SMTP')
    smtp_logger.setLevel(logging.ERROR)
    smtp_logger.addHandler(configure_smtp_handler())

    # Get time for each type of logging handler

    stream_time = time_logger(logging.root, logging.DEBUG, 'Stream to stdout')
    file_time = time_logger(file_logger, logging.INFO, 'File logger.')
    smtp_time = time_logger(smtp_logger, logging.ERROR, 'SMTP logger.')

    # print times

    logging.debug(f"stream logger {stream_time:0.4f} seconds.")
    logging.debug(f"file logger   {file_time:0.4f} seconds.")
    logging.debug(f"SMTP logger   {smtp_time:0.4f} seconds.")

    # from logging_tree import printout
    # printout()