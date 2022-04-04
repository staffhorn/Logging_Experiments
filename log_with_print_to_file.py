"""
 Copyright 2022 "Holistic Mathematics Agency".
 SPDX-License-Identifier: Apache-2.0
"""

import sys

with open(file='logs/example_print.log', mode='a') as file:
    print('This is an example of writing to a logfile with print.', file=file)
