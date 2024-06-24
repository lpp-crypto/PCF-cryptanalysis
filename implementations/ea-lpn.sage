#!/usr/bin/sage
#-*- Python -*-
# Time-stamp: <2024-06-24 14:30:21 leo>

from sage.all import *
from prg import ReproduciblePRG



def prg(length):
    return randint(0, Integer(1 << length)-1)


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

    key: a two dimensional array (list of list) with l rows and t/l
    columns

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
        """The input is a list of length l of tuples (x_i, j_i), where

        - all x_i are integers in {1, ..., 5N/t}

        - all j_i are integers in {1, ..., t/l}

        """
        # generating the random input
        x = [self.prg(1, self.word_size) for i in range(0, self.l)]
        j = [self.prg(0, self.t_over_l) for i in range(0, self.l)]
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

