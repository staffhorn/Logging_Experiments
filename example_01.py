"""
 Copyright 2022 "Holistic Mathematics Agency".
 SPDX-License-Identifier: Apache-2.0
"""

'''
Example 01
Print debugging to the screen using print()

NOTES:
We consider debug messages to be messages we want to see while developing or troubleshooting the code,
but we don't want to see them during operations.

When we use a print() to debug our code, we have to comment it out or delete it later when we deploy 
to operations. Here we only print if LEVEL=='DEBUG'

Using logging, we can level our debug messages in the code and suppress them by configuration.
'''

import os

LEVEL = 'DEBUG'

if LEVEL=='DEBUG':
    print('This debug message uses print.')
