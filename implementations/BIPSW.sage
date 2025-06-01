#!/usr/bin/sage
#-*- Python -*-
# Time-stamp: <2025-06-01 22:20:20>

from sage.all import *
from utils import *


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
            k                   # value of the key
    ):
        self.n = n
        self.k = k
    
    def __call__(self, x):
        """Evaluates the BIPSW function on an input by considering it
        to be a binary vector {0, ..., 2^n-1}.

        """
        assert x < 2**self.n
        pseudo_rounding = {
            0: 0,
            1: 0,
            2: 0,
            3: 1,
            4: 1,
            5: 1
        }
        return pseudo_rounding[scalar_product(x, self.k) % 6]


if __name__ == "__main__":
    prng = ReproducibleRangePRG(b"")
    sequence_length = 500
    # 128-bit security
    n = 770 
    bipsw_instance = BIPSW(
        n,                      # input length
        prng(0, 2**n)           # key is picked randomly
    )
    print_sequence([
        bipsw_instance(prng(0, 2**n)) # we pick plaintexts in [0,2**n-1]
        for i in range(0, sequence_length)
    ])

