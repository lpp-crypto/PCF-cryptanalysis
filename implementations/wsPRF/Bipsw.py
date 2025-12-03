#!/usr/bin/sage
#-*- Python -*-


from sage.all import *
from .Utils import *


def scalar_product(x, y):
    """The scalar product as an integer of the binary representation of `x` and `y` is defined as

    x⋅y = \\sum_i x_i y_i

    where x=\\sum_i x_i 2^i, y=\\sum_i y_i y^i, and the sum is *not* reduced modulo 2.

    Args:
        x (int): \\sum_i x_i 2^i
        y (int): \\sum_i y_i 2^i

    Returns:
        int: \\sum_i x_i*y_i

    """
    t = x & y
    result = 0
    while t != 0:
        if (t & 1) == 1:
            result += 1
        t = t >> 1
    return result 


class BIPSW:
    """Implements the BIPSW weak PRF as specified in

    Dan Boneh, Yuval Ishai, Alain Passelègue, Amit Sahai, and David J. Wu. Exploring crypto dark matter: New simple PRF candidates and their applications. In Amos Beimel and Stefan Dziembowski, editors, TCC 2018, Part II, volume 11240 of LNCS, pages 699–729. Springer, Cham, November 2018.
    
    """
    def __init__(self, n,):
        """Initializes the parameter of a BIPSW instance.

        Args:
            n (int): the block size (and security parameter)

        """
        self.n = n

    
    def __call__(self, k, x):
        """Evaluates the BIPSW function on input `x` and key `k` by considering both to be binary vectors {0, ..., 2^n-1}.

        Args:
            k (int): the secret key, equal to \\sum_i k_i 2^i
            x (int): the public input, equal to \\sum_i x_i 2^i

        Returns:
            int: an integer equal to 0 or 1 equal to \\lfloor x.y mod 6 \\rfloor, where the rounding function maps {0,1,2} to 0 and {3,4,5} to 1, and where the scalar product is an integer as returned by the function `scalar_prod`.
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


