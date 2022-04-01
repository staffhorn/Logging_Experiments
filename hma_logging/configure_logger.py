"""
 Copyright 2022 "Holistic Mathematics Agency".
 SPDX-License-Identifier: Apache-2.0
"""
import logging
from logging.handlers import TimedRotatingFileHandler, SMTPHandler
import os

SUBJECT = 'Holisticmath alert notification'

def configure_logfile_logger(logger:logging.Logger, filename:str) -> logging.Logger:
    '''
    Configure a logger to send to a timed rotating logfile. 
    >>> logger = logging.getLogger('file notifier')
    >>> logger = configure_logfile_logger(logger, filename='logs/rotatinglogfile_test.log')
    >>> logger.info('Rotating logfile logging test works')
    '''
    file_handler = TimedRotatingFileHandler(filename=filename, when='midnight', backupCount=5)
    formatter = logging.Formatter(fmt='%(asctime)s %(module)s %(levelname)s %(message)s ')
    file_handler.setFormatter(fmt=formatter)

    logger.setLevel(level=logging.INFO)
    logger.addHandler(file_handler)
    return logger

def configure_smtp_logger(logger:logging.Logger, notify_list=None) -> logging.Logger:
    '''
    Configure a logger to send record to a notification list.
    >>> logger = logging.getLogger('alert notifier')
    >>> logger = configure_smtp_logger(logger)
    >>> logger.info('Where does this go?')
    >>> logger.error('Logging notification test works')
    '''
    SENDER=os.environ['gmail_app_sender']
    SENDER_PASS=os.environ['gmail_app_pass']

    if notify_list is None: notify_list = [SENDER]

    formatter = logging.Formatter(fmt='%(asctime)s %(module)s %(levelname)s %(message)s ')
    smtp_handler = SMTPHandler(mailhost=('smtp.gmail.com', 587), 
        fromaddr=SENDER,
        toaddrs=notify_list,
        subject=SUBJECT,
        credentials = (
            SENDER,
            SENDER_PASS
        ),
        secure=()
    )
    smtp_handler.setFormatter(fmt=formatter)
    smtp_handler.setLevel(logging.ERROR)
    logger = logging.getLogger(name=__name__)
    logger.addHandler(smtp_handler)
    logger.setLevel(logging.DEBUG)
    return logger

if __name__ == "__main__":
    '''
    Run some test examples from function docstrings.
    '''
    import doctest
    doctest.testmod()
