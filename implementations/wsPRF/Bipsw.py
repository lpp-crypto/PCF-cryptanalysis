#!/usr/bin/sage
#-*- Python -*-


from sage.all import *
from .Utils import *


def scalar_product(x, y):
    """Returns the scalar product in N of the binary
    representation of `x` and `y`.

    """
    t = x & y
    result = 0
    while t != 0:
        if (t & 1) == 1:
            result += 1
        t = t >> 1
    return result 


class BIPSW:
    """Parameters:
    `n` the block size (and security parameter)
    `seed` the seed used to seed the PRG generating the key.
    """
    def __init__(
            self,
            n,                  # input and key bit lengths
    ):
        self.n = n

    
    def __call__(self, k, x):
        """Evaluates the BIPSW function on input x and key k by
        considering both to be binary vectors {0, ..., 2^n-1}.

        """
        assert x < 2**self.n
        assert k < 2**self.n
        pseudo_rounding = {
            0: 0,
            1: 0,
            2: 0,
            3: 1,
            4: 1,
            5: 1
        }
        return pseudo_rounding[scalar_product(x, k) % 6]


