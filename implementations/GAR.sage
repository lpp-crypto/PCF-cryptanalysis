#!/usr/bin/sage
#-*- Python -*-
# Time-stamp: <2024-07-01 15:42:29 leo>

from sage.all import *
from utils import *



def xor_maj(L, a=10, b=64):
    """Takes a list of integers corresponding to the variables that
    are taken to output the PRG and `n` and `m` parameters for the
    function: the first `n` bits are XORed the last is majority

    """
    assert len(L) == a + b
    tmp = sum(L[a:a+b])
    if tmp >= b/2:
        return (sum(L[0:a]) + 1) % 2
    else:
        return sum(L[0:a]) % 2




class GAR:
    """An implementation of the GAR PRF. It uses the parameters: 

    N: the size of the secret key

    t: the number of input bits taken by the predicate

    predicate: the predicate used (xor_maj in the original proposal),
    must take as input a list of booleans of a given size

    key: an integer of value < 2^N

    # !TODO!  add reference
    """

    def __init__(self,
                 _N = 256,
                 _t = 74,
                 predicate = xor_maj,
                 seed = b"seed"):
        # initializing the variables 
        self.N = _N
        self.t = _t
        self.predicate = predicate
        self.prg = ReproduciblePRG(seed)
        self.k = self.prg(0, 1 << self.N)

        
    def __call__(self):
        """Generate a subset of the key bits through their indices,
        then applies the predicate on the bit-vector obtained by
        grabbing said key bits.

        """
        key_bit_indices = []
        while len(key_bit_indices) < self.t:
            random_index = self.prg(0, self.N)
            if random_index not in key_bit_indices:
                key_bit_indices.append(random_index)
        x = [(self.k >> index) & 1 for index in key_bit_indices]
        return self.predicate(x)


# parameters
# !TODO! suggest parameters 
if __name__ == "__main__":
    print(pretty_sequence(get_sequence(GAR(), 50)))


