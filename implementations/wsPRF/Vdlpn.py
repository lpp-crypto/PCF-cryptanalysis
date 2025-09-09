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
    def __init__(self, d, w,):
        self.d = d
        self.w = w
        
        
    def __call__(self, k, x):
        assert len(x) == self.w * self.d**2
        assert len(k) == self.w * self.d**2
        y = 0
        for i in range(0, self.d):
            for j in range(0, self.w):
                t = 1
                for l in range(0, i):
                    index = i*self.d*self.w + j*self.d + l
                    t = t*(x[index] ^ k[index])
            y = y ^ t
        return y



    
