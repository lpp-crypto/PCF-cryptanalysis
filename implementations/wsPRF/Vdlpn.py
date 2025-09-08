#!/usr/bin/env sage
#-*- Python -*-


from sage.all import *
from .Utils import *


def triangular(_x):
    """The Boolean function x_1(1 + x_2(1 + ... )) applied to the
    binary list `_x`.

    """
    x = _x
    counter = 0
    while ((x & 1) != 0) and (x != 0):
        counter += 1
        x = x >> 1
    return counter % 2


class VDLPN:
    def __init__(
            self,
            d, # the degree of the boolean function 
            w, # the number of binary variables that are simply added
    ):
        self.d = d
        self.w = w
        
        
    def __call__(self, k, x):
        assert len(x) == self.w
        assert len(k) == self.w
        xors = [x[i] ^ k[i] for i in range(0, self.w)]
        return sum(triangular(xors[i]) for i in range(0, self.w)) % 2

    
