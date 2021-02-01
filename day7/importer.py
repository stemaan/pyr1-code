import sys

path_copy = sys.path
sys.path = []

from test import add

add(1, 2)
