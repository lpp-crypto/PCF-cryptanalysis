#!/usr/bin/sage
#-*- Python -*-
# Time-stamp: <2024-06-24 14:44:59 leo>

from sage.all import *
from prg import ReproduciblePRG

# !TODO! implement BIPSW


def scalar_product(x, y):
    t = x & y
    result = 0
    while t != 0:
        if (t & 1) == 1:
            result += 1
        t = t >> 1
    return result


class BIPSW:
    """Parameters:
    # !TODO! write description of BIPSW 
    
    """
    def __init__(self,
                 n = 770,
                 seed = b"seed"):
        self.prg = ReproduciblePRG(seed)
        self.n = n
        self.k = self.prg(0, 2**self.n)
    
    def __call__(self):
        pseudo_rounding = {
            0: 0,
            1: 0,
            2: 0,
            3: 1,
            4: 1,
            5: 1
        }
        x = self.prg(0, 2**self.n)
        return pseudo_rounding[scalar_product(x, self.k) % 6]


if __name__ == "__main__":
    pcf = BIPSW()
    row = ""
    for t in range(0, 50):
        row += "{:d} ".format(pcf())
    print(row)

