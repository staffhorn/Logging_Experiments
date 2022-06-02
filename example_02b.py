"""
 Copyright 2022 "Holistic Mathematics Agency".
 SPDX-License-Identifier: Apache-2.0
"""
# Here is *some* code that uses print().  It's fine.

with open('example_13.yaml') as file:
  for line in file.readlines():
    print(line[:-1])

