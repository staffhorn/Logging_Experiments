"""
 Copyright 2022 "Holistic Mathematics Agency".
 SPDX-License-Identifier: Apache-2.0
"""

from email.utils import format_datetime
import queue
import logging
from logging.handlers import QueueHandler, QueueListener
from example_09 import configure_smtp_handler
from example_10 import time_logger

'''
Example 11 Use QueueHandler to unblock smtp logging.
'''

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

log_queue = queue.Queue(maxsize=-1)
queue_handler = QueueHandler(queue=log_queue)
logger = logging.getLogger(name=__name__)
formatter = logging.Formatter('%(threadName)s, "%(asctime)s",%(module)s,%(name)s,%(levelname)s,"%(message)s"')

# Note the only handler we add directly to the Logger is QueueHandler
logger.addHandler(queue_handler)

smtp_handler = configure_smtp_handler()
smtp_handler.setFormatter(formatter)

# Create a QueueListener, add a Queue and all the other LoggingHandlers here:
listener = QueueListener(log_queue, smtp_handler)
# This starts up a background thread to monitor the queue for LogRecords send to smtp logger.
listener.start()

smtp_time = time_logger(logger, logging.ERROR, 'Simulated alert message.  There is no actual emergency')
logging.info(f"SMTP logger took {smtp_time:0.4f} seconds")

# Make sure all messages get processed before terminating.
listener.stop()