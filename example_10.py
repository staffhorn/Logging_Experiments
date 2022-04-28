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


if __name__=="__main__":
    import time
    import sys

    logging.basicConfig(
        format='',
        level=logging.DEBUG,
        stream=sys.stdout
        )

   
    file_logger = logging.getLogger('File')
    file_logger.setLevel(logging.INFO)
    file_logger.addHandler(configure_file_handler())
    smtp_logger = logging.getLogger('SMTP')
    smtp_logger.setLevel(logging.ERROR)
    smtp_logger.addHandler(configure_smtp_handler())

    tic0 = time.perf_counter()
    logging.debug('Gentle debug message, sent to stdout.')
    tic1 = time.perf_counter()
    logging.debug(f"stream logger {tic1-tic0:0.4f} seconds.")
    tic2 = time.perf_counter()
    file_logger.info('Informative info message, sent to file.')
    tic3 = time.perf_counter()
    logging.debug(f"file logger {tic3-tic2:0.4f} seconds.")
    tic4 = time.perf_counter()
    smtp_logger.error('Simulated alert message--not an actual error.')
    toc = time.perf_counter()
    logging.debug(f"SMTP logger {toc-tic4:0.4f} seconds.")

    import logging_tree
    logging_tree.printout()
    
