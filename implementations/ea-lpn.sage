#!/usr/bin/sage
#-*- Python -*-
# Time-stamp: <2024-06-24 11:28:31 leo>

from sage.all import *

from prg import ReproduciblePRG


# !TODO! implement EA-LPN

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
                 seed):
        # checking validity of parameters
        assert (t % l) == 0
        # initializing the variables
        self.N = N
        self.t = t
        self.l = l
        self.t_over_l = Integer(t / l)
        # !TODO! generate key from seed
        
        assert len(self.key) == l
        assert len(self.key[0]) == self.t_over_l
        

        
    def __eval__(self):
        """The input is a list of length l of tuples (x_i, j_i), where

        - all x_i are integers in {1, ..., 5N/t}

        - all j_i are integers in {1, ..., t/l}

        """
        # !TODO! modify logic to encapsulate the queries 
        assert len(x) == l
        assert len(x[0]) = 2
        # evaluating the function
        x = [xj[i][0] for i in range(0, l)]
        j = [xj[i][1] for i in range(0, l)]
        result = 0
        for i in range(0, l):
            result += greater_than(x[i], self.key[j[i]])
        return result % 2



# parameters
# !TODO! double check parameters
aggressive_ealpn = EALPN(N = 2**45,
                         t = 660,
                         l = 11)

safe_ealpn = EALPN(N = 2**45,
                   t = 660,
                   l = 11)

if __name__ == "__main__":
    print("bla")

    # !TODO! write tests 

