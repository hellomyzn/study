"""
サードパーティライブラリー
"""

import collections
import sys
import os
from termcolor import colored

print("test")
print(colored("test", "red"))

print(help(colored))

print(collections.__file__)
print(termcolor.__file__)

print(sys.path)
