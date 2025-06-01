#!/usr/bin/sage
#-*- Python -*-
# Time-stamp: <2025-06-01 22:20:01>

from sage.all import *
from utils import *


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
            k  # the value of the key
    ):
        self.d = d
        self.w = w
        self.k = k
        
        
    def __call__(self, x):
        assert self.k != None
        assert len(x) == self.w
        xors = [x[i] ^^ self.k[i] for i in range(0, self.w)]
        return sum(triangular(xors[i]) for i in range(0, self.w)) % 2


if __name__ == "__main__":
    seed = b""
    prng = ReproducibleRangePRG(seed)
    sequence_length = 500
    # 128-bit security
    d = 40
    w = 120
    # keygen
    k = [
        prng(0, 2**d)        # the key is made of integers in [0,2^d-1]
        for i in range(0, w) # namely, w of them
    ]
    vdlpn_instance = VDLPN(d, w, k)
    print_sequence([
        vdlpn_instance([prng(0, 2**d) for j in range(0, w)])
        for i in range(0, sequence_length)
    ])

    
