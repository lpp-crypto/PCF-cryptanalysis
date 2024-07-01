#!/usr/bin/sage
#-*- Python -*-
# Time-stamp: <2024-07-01 14:58:02 leo>

from sage.all import *
from prg import ReproduciblePRG


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
    """Parameters:
    `d` is the degree of the boolean function
    `w` is the number of binary variables that are simply added
    `seed` is used to seed the PRG used to generate the key


    # !TODO! Add reference 
    """
    def __init__(self,
                 d = 40,
                 w = 120,
                 seed=b"seed"):
        self.prg = ReproduciblePRG(seed)
        self.d = d
        self.w = w
        self.k = [self.prg(lower_bound=0,
                           upper_bound=2**self.d)
                  for i in range(0, self.w)]

    def __call__(self):
        x = [self.prg(lower_bound=0,
                      upper_bound=2**self.d)
             for i in range(0, self.w)]
        xors = [x[i] ^^ self.k[i] for i in range(0, self.w)]
        return sum(triangular(xors[i]) for i in range(0, self.w)) % 2


if __name__ == "__main__":
    pcf = VDLPN()
    print("init")
    for i in range(0, 100):
        print(pcf())
    
