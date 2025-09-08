#!/usr/bin/env sage
#-*- Python -*-


from .Utils import *

# predicates
# ==========

class P_5:
    def __init__(self):
        self.d = 5
        
    def __call__(self, x):
        return (x[0] + x[1] + x[2] + x[3]*x[4]) % 2


class Threshold:
    def __init__(self, th):
        self.th = floor(th)
        self.d = None

    def __call__(self, x):
        if sum(x) < self.th:
            return 0
        else:
            return 1


class XOR_MAJ:
    def __init__(self, l_1, l_2):
        """Initializes the XOR-MAJ predicate.

        l_1 the number of bits that must be XORed, l_2 the number of bits
        whose majority must be taken.

        """
        self.l_1 = l_1
        self.l_2 = l_2
        self.maj = Threshold(l_2/2)
        self.d = l_1 + l_2

    def __call__(self, x):
        assert len(x) == self.l_1 + self.l_2
        return (sum(x[:self.l_1]) + self.maj(x[self.l_1:])) % 2


# the Goldreich PRG
# =================

class GAR:
    """An implementation of the GAR PRF. It uses the parameters: 

    N: the size of the secret key

    t: the number of input bits taken by the predicate

    predicate: the predicate used (xor_maj in the original proposal),
    must take as input a list of booleans of a given size

    """

    def __init__(self,
                 n,             # seed size
                 predicate,     # predicate
                 m=None,        # output size
                 s=None         # stretch
                 ):
        """Initializes a GAR instance. Either `m` or `s` must be
        specified at construction.

        """
        if (m == None and s == None) or (m != None and s != None):
            raise Exception("Either the stretch (x)or the output size must be specified!")
        self.n = n
        self.predicate = predicate
        self.d = predicate.d
        if m != None:
            self.m = m
        else:
            # case where the stretch is specified instead
            self.m = n**s

            
    def __call__(self, k, x):
        """Returns a single bit corresponding to the evaluation of the predicate on a specific subset of the seed bits.

        `k` is the seed,
        `x` is a subset of the key indices.
        
        """
        assert len(x) == self.d
        predicate_input = []
        for i in x: 
            predicate_input.append(k[i])
        return self.predicate(predicate_input)

    
    def prg(self, k, xs):
        seed = k
        y = 0
        for i in range(0, self.m):
            y = (y << 1) | self(seed, x[i])
        return 

