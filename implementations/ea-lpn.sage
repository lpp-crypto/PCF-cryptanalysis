#!/usr/bin/sage
#-*- Python -*-
# Time-stamp: <2024-06-24 10:57:25 leo>

from sage.all import *


# !TODO! implement EA-LPN


class EALPN:
    """An implementation of the EA-LPN PRF. It uses the following
    parameters:

    N: code-words of the underlying code are of size 5N
    
    t: is the number of cells for the noise; in each cell, the noise
    is all zero before a threshold, all 1 after

    l: the number of cells in the input, it has to be a divisor of t
    """    
    def __init__(self,
                 N = 2**45,
                 t = 660,
                 l = 11):
        self.N = N
        self.t = t
        self.l = l

        
    def __eval__(self, x, key):
        # !TODO! implement evaluation method 
        return None



# parameters
# !TODO! double check parameters 
aggressive_ealpn = EALPN(N = 2**45,
                         t = 660,
                         l = 11)

safe_ealpn = EALPN(N = 2**45,
                   t = 660,
                   l = 11)


