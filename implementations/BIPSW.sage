#!/usr/bin/sage
#-*- Python -*-
# Time-stamp: <2024-07-01 15:21:17 leo>

from sage.all import *
from utils import *


def scalar_product(x, y):
    """Returns The scalar product in F_2^n of the binary
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
    def __init__(self,
                 n = 770,
                 seed = b"seed"):
        self.prg = ReproduciblePRG(seed)
        self.n = n
        self.k = self.prg(0, 2**self.n)
    
    def __call__(self):
        """Generate a random element of {0, ..., 2^n-1}, and evaluates
        the function on it.

        """
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
    print(pretty_sequence(get_sequence(BIPSW(), 50)))

