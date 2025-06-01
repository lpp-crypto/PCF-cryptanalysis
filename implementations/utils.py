#!/usr/bin/env sage
#-*- Python -*-
# Time-stamp: <2025-06-02 00:43:01>

from sage.all import *
from prg import *

MAX_ROW_LENGTH = 80

def print_sequence(seq):
    row = ""
    total = 0
    for x in seq:
        row += "{:d},".format(x)
        total += x
        if len(row) == MAX_ROW_LENGTH:
            print(row)
            row = ""
    print(row)
    print("weight = {:d} = {:8.4f}%".format(total, 100.0*total/len(seq)))



