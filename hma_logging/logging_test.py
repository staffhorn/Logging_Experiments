"""
 Copyright 2022 Holistic Mathematics Agency
 
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 
     http://www.apache.org/licenses/LICENSE-2.0
 
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""


from importlib import import_module
from logging_rotatefile import log_to_rotatinglogfile
import os

def test_me():
    '''
    >>> logger = log_to_rotatinglogfile(filename='logs/doctest.log').info('Logging test worked')
    '''
    pass


import doctest
doctest.testmod()