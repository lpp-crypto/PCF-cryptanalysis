#!/usr/bin/env sage
#-*- Python -*-



from .Utils import *


def greater_than(x, k):
    if x >= k:
        return 1
    else:
        return 0
    

class EALPN:
    """An implementation of the EA-LPN PRF, as specified in

    Elette Boyle, Geoffroy Couteau, Niv Gilboa, Yuval Ishai, Lisa Kohl, Nicolas Resch, and Peter Scholl. Correlated pseudorandomness from expand-accumulate codes. In Yevgeniy Dodis and Thomas Shrimpton, editors, CRYPTO 2022, Part II, volume 13508 of LNCS, pages 603–633. Springer, Cham, August 2022.
    
    """
    
    def __init__(self, m, l, u,):
        """Initializes an instance of EALPN by specifying all its parameters.
        
        Args:
            N (int): code-words of the underlying code are of size 5N.
            t (int) : is the number of cells for the noise; in each cell, the noise is all zero before a threshold, all 1 after.
            l (int): the number of cells in the input, it has to be a divisor of t.
        """
        self.m = m
        self.l = l
        self.u = u

        
    def __call__(self, k, jx):
        """Evaluates EALP on the given secret key `k` and input `jx`. Both the key `k` and the input `jx` must be two-dimensional arrays:
        - `k` must contain l rows, each with u elements in {1, ..., m}
        - `jx` is contains l rows, each with two elements:
            - `j` in {0, ..., u-1} (index in key row)
            - `x` in {1, ..., m} (value to compare)

        Args:
            k (list[list]): the secret key
            jx (list[list]): the public input
        
        Returns:
            int: An integer equal to 0 or 1.

        """
        result = 0
        for i in range(0, self.l):
            j, x = jx[i]
            assert j < self.u
            assert x < self.m
            result += greater_than(x, k[i][j])
        return result % 2


