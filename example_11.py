"""
 Copyright 2022 "Holistic Mathematics Agency".
 SPDX-License-Identifier: Apache-2.0
"""

from email.utils import format_datetime
import queue
import logging
from logging.handlers import QueueHandler, QueueListener
from example_09 import configure_smtp_handler
import time

'''
Example 11 timing multithreaded SMTP logger.
'''

logging.basicConfig(level=logging.DEBUG, format='%(message)s')


log_queue = queue.Queue(maxsize=-1)
queue_handler = QueueHandler(queue=log_queue)
logger = logging.getLogger(name=__name__)
formatter = logging.Formatter('%(threadName)s, "%(asctime)s",%(module)s,%(name)s,%(levelname)s,"%(message)s"')

# Note the only handler we add directly to the Logger is QueueHandler
logger.addHandler(queue_handler)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

smtp_handler = configure_smtp_handler()
smtp_handler.setFormatter(formatter)

# we add a Queue and all the other LoggingHandlers here:
listener = QueueListener(log_queue, console_handler, smtp_handler)
# This starts up a background thread to monitor the queue for LogRecords to process.
listener.start()

tic = time.perf_counter()
logger.error('Simulated alert message.  There is no actual emergency')
toc = time.perf_counter()

logging.info(f"SMTP logger took {toc-tic:0.4f} seconds")

listener.stop()