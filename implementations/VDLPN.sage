#!/usr/bin/sage
#-*- Python -*-
# Time-stamp: <2024-06-24 12:13:13 leo>

from sage.all import *

from prg import ReproduciblePRG

# !TODO! implement VDLPN


def triangular(_x):
    x = _x
    counter = 0
    while ((x & 1) != 0) and (x != 0):
        counter += 1
        x = x >> 1
    return counter % 2


class VDLPN:
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
    
