#!/usr/bin/sage
#-*- Python -*-
# Time-stamp: <2024-07-01 14:59:47 leo>

from sage.all import *
from prg import ReproduciblePRG


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

    # !TODO! Add reference 
    """    
    def __init__(self,
                 N = 2**45,
                 t = 660,
                 l = 11,
                 seed = b"seed"):
        # initializing the variables
        self.N = N
        self.t = l * ceil(t / l)
        self.l = l
        self.t_over_l = Integer(self.t / self.l)
        self.prg = ReproduciblePRG(seed)
        self.word_size = ceil((5*self.N) / self.t)
        self.k = [
            self.prg(1, self.word_size)
            for i in range(0, self.t)
        ]

        
    def __call__(self):
        """Generates a random input and evaluates the function on it.
        The input is a list of length l of tuples (x_i, j_i), where

        - all x_i are integers in {1, ..., 5N/t}

        - all j_i are integers in {1, ..., t/l}

        """
        # generating the random input
        x = [self.prg(1, self.word_size) for i in range(0, self.l)]
        j = [self.prg(0, self.t_over_l) for i in range(0, self.l)]
        # computing the function
        result = 0
        for i in range(0, self.l):
            result += greater_than(x[i], self.k[j[i]])
        return result % 2



# parameters
# !TODO! double check parameters
aggressive_ealpn = EALPN(N = 2**45,
                         t = 660,
                         l = 11)

safe_ealpn = EALPN(N = 2**45,
                   t = 660,
                   l = 11)

eval_time_optimized = EALPN(N = 2**45,
                            t = 1000,
                            l = 7)

if __name__ == "__main__":
    for pcf in [aggressive_ealpn, safe_ealpn, eval_time_optimized]:
        row = ""
        for t in range(0, 50):
            row += "{:d} ".format(pcf())
        print(row)

