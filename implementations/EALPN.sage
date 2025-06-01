#!/usr/bin/env sage
#-*- Python -*-
# Time-stamp: <2025-06-01 23:24:19>

from sage.all import *
from utils import *


def greater_than(x, k):
    if x >= k:
        return 1
    else:
        return 0
    

class EALPN:
    """An implementation of the EA-LPN PRF. It uses the following
    parameters:

    N: code-words of the underlying code are of size 5N
    
    t: is the number of cells for the noise; in each cell, the noise
    is all zero before a threshold, all 1 after

    l: the number of cells in the input, it has to be a divisor of t
    """    
    def __init__(
            self,
            m, # main size (5N/t in slides)
            l, # number of rows in the key
            u, # length of each key row
    ):
        # initializing the variables
        self.m = m
        self.l = l
        self.u = u

        
    def __call__(self, k, jx):
        """Both the key `k` and the input `jx` are two-dimensional arrays:

        - `k` must contain l rows, each with u elements in {1, ..., m}
        - `jx` is contains l rows, each with two elements:
            - `j` in {0, ..., u-1} (index in key row)
            - `x` in {1, ..., m} (value to compare)
        """
        # computing the function
        result = 0
        for i in range(0, self.l):
            j, x = jx[i]
            assert j < self.u
            assert x < self.m
            result += greater_than(x, k[i][j])
        return result % 2



# parameters
# m is equal to 5N/t, and u to t/l
# -- sage, N=2**45, t=85, l=3ln(5N)=98.4
safe_ealpn = EALPN(
    2**41, # m
    99,    # l
    1      # u
)

# -- aggressive, N=2**45, t=660, l=11
aggressive_ealpn = EALPN(
    2**38, # m
    11,    # l
    60     # u
)
                   


if __name__ == "__main__":
    seed = b""
    prng = ReproducibleRangePRG(seed)
    sequence_length = 500
    # 128-bit secure
    instance = safe_ealpn
    # generating the key
    k = [
        [prng(0, instance.m) for t in range(0, instance.u)]
        for i in range(0, instance.l)
    ]
    # printing sequence
    seq = []
    for t in range(0, sequence_length):
        # generating the random input
        jx = [
            (
                prng(0, instance.u), # j
                prng(0, instance.m), # x
            )
            for i in range(0, instance.l)
        ]
        seq.append(instance(k, jx))
    print_sequence(seq)

    
