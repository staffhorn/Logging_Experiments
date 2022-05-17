"""
 Copyright 2022 "Holistic Mathematics Agency".
 SPDX-License-Identifier: Apache-2.0
"""

import logging
from logging.handlers import SMTPHandler
import os

'''
Example 09
Configure logging to send email via a gmail account.
'''

SUBJECT='Alert'


def configure_smtp_handler(notify_list=None) -> logging.Handler:

    sender = os.environ['gmail_app_sender']
    if notify_list is None: notify_list=[sender]

    smtp_handler = SMTPHandler(
        mailhost=('smtp.gmail.com', 587), 
        fromaddr=sender,
        toaddrs=notify_list,
        subject=SUBJECT,
        credentials = ( sender, os.environ['gmail_app_pass']),
        secure=()
    )

    formatter = logging.Formatter(fmt='"%(asctime)s",%(module)s,%(name)s,%(levelname)s,"%(message)s"')
    smtp_handler.setFormatter(fmt=formatter)
    smtp_handler.setLevel(logging.ERROR)
    return smtp_handler


if __name__=="__main__":
    logging.basicConfig(format='')
    
    logger = logging.getLogger()
    logger.addHandler(configure_smtp_handler())
    logger.error('''Simulated alert. There is no emergency.''')

