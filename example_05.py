"""
 Copyright 2022 "Holistic Mathematics Agency".
 SPDX-License-Identifier: Apache-2.0
"""

import sys

'''
Example 05
Log to a file with print()
'''
with open(file='logs/example_print.log', mode='a') as file:
    print('This is an example of writing to a logfile with print.', file=file)
