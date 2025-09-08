#!/usr/bin/env sage
#-*- Python -*-



from .Utils import *


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


