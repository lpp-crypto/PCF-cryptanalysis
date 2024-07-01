#!/usr/bin/sage
#-*- Python -*-
# Time-stamp: <2024-07-01 15:21:37 leo>

from sage.all import *
from prg import ReproduciblePRG


def get_sequence(oracle, N_queries):
    return [oracle() for i in range(0, N_queries)]


def pretty_sequence(binary_sequence):
    result = ""
    for x in binary_sequence:
        result += "{:d} ".format(x)
    return result[:-1]



