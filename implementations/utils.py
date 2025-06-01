#!/usr/bin/sage
#-*- Python -*-
# Time-stamp: <2025-06-01 22:15:53>

from sage.all import *
from prg import *

MAX_ROW_LENGTH = 80

def print_sequence(binary_sequence):
    row = ""
    for x in binary_sequence:
        row += "{:d},".format(x)
        if len(row) == MAX_ROW_LENGTH:
            print(row)
            row = ""
    print(row)



