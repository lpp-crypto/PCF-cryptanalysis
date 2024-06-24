#!/usr/bin/sage
#-*- Python -*-
# Time-stamp: <2024-06-24 11:35:16 leo>

from sage.all import *


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
                 seed):

        # !TODO! implement verification in initialization
        # !TODO! implement generation of the key from the seed
        self.n = n
    
    def __eval__(self):
        pseudo_rounding = {
            0: 0,
            1: 0,
            2: 0,
            3: 1,
            4: 1,
            5: 1
        }
        # !TODO! generate x randomly 
        return pseudo_rounding[scalar_product(x, self.k)]
