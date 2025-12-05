#!/usr/bin/env sage
#-*- Python -*-


from sage.all import *
from .Utils import *


def triangular(_x):
    """The triangular function used in VDLPN. It is a Boolean function returning x_1(1 + x_2(1 + ... )). While it is not used directly in the evaluation, it could be used in an equivalent representation.

    Args:
        _x (int): an integer whose binary representation is \\sum_i x_i 2^i

    Returns:
        int: an integer in [0,1] equal to x_1(1 + x_2(1 + x_3(1 + ...))).

    """
    x = _x
    counter = 0
    while ((x & 1) != 0) and (x != 0):
        counter += 1
        x = x >> 1
    return counter & 1


class VDLPN:
    """The VDLPN weak PRF, as specified in

    Elette Boyle, Geoffroy Couteau, Niv Gilboa, Yuval Ishai, Lisa Kohl, and Peter Scholl. Correlated pseudorandom functions from variable-density LPN. In 61st FOCS, pages 1069–1080. IEEE Computer Society Press, November 2020.

    """
    def __init__(self, d, w):
        """Initializes the parameters of this VDLPN instance.

        Args:
            d (int): the degree of the triangular function
            w (int): the number of calls to the triangular function
        
        """
        self.d = d
        self.w = w
        
        
    def __call__(self, k, x):
        """Evaluates VDLPN on the given secret key `k` and public input `x`. The evaluation is not made using the sum of triangular functions (as shown at the bottom of page 27 of our paper) but rather using Equation (4) of said paper (see also below in the description of what is returned).

        Args:
            k (list): a list of integers in [0,1] corresponding to the secret key
            x (list): a list of integers in [0,1] corresponding to the public input

        Returns:
            int: an integer in [0,1] equal to F_k(x) = \\sum_{i=1}^D \\sum_{j=1}^w \\prod_{\ell=1}^i (x_{i,j,l} + k_{i,j,l})
        
        """
        assert len(x) == self.w * self.d**2
        assert len(k) == self.w * self.d**2
        y = 0
        for i in range(0, self.d):
            for j in range(0, self.w):
                t = 1
                for l in range(0, i):
                    index = i*self.d*self.w + j*self.d + l
                    t = t*(x[index] ^ k[index])
            y += t
        return y & 1



    
