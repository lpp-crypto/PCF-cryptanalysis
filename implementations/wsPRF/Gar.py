#!/usr/bin/env sage
#-*- Python -*-


from .Utils import *


# !SECTION! Predicates 
# So-called "predicates" are simply Boolean functions that are applied to parts of the internal "seed" of the PRG. Others could easily be added: they simply correspond to classes having an attribute called `d` corresponding to the expected input size (set to None if there is no limit), and a `__call__` method mapping a list of integers in [0,1] of length `d` to a single integer equal to 0 or 1.

class P_5:
    """A specific quadratic Boolean function.

    """
    def __init__(self):
        self.d = 5
        
    def __call__(self, x):
        return (x[0] + x[1] + x[2] + x[3]*x[4]) % 2


class Threshold:
    """Checks whether the number of elements in the input is strictly smaller than the given threshold.

    """
    def __init__(self, th):
        """Initializes the parameters.

        Args:
            th (int): the threshold under which the output is 0. Above it, it will output 1.
        """
        self.th = floor(th)
        self.d = None

    def __call__(self, x):
        if sum(x) < self.th:
            return 0
        else:
            return 1


class XOR_MAJ:
    """Adds (modulo 2) a majority computed on a subset of its input with the sum of the other inputs. The majority over t bits is simply Threshold(t/2).
    
    """
    def __init__(self, l_1, l_2):
        """Initializes the parameters for a XOR_MAJ instance.

        Args:
            l_1 (int): the number of bits that must be XORed
            l_2 (int): the number of bits whose majority must be taken

        """
        self.l_1 = l_1
        self.l_2 = l_2
        self.maj = Threshold(l_2/2)
        self.d = l_1 + l_2

    def __call__(self, x):
        assert len(x) == self.l_1 + self.l_2
        return (sum(x[:self.l_1]) + self.maj(x[self.l_1:])) % 2


# !SECTION! the Goldreich PRG itself


class GAR:
    """An implementation of the GAR PRF, as specified in

    Oded Goldreich. Candidate one-way functions based on expander graphs. Electron. Colloquium Comput. Complex., TR00-090, 2000.

    """

    def __init__(self, n, predicate, m=None, s=None):
        """Initializes a GAR instance. Either `m` or `s` must be specified at construction.

        Args:
            N (int): the size of the secret key
            predicate: the predicate used (xor_maj in the original proposal).
            m (int): the output size in bits. Defaults to "None"
            s (float): the stretch; defaults to "None".

        """
        if (m == None and s == None) or (m != None and s != None):
            raise Exception("Either the stretch or the output size must be specified!")
        self.n = n
        self.predicate = predicate
        self.d = predicate.d
        if m != None: # case where the output size is specified
            self.m = m
        else: # case where the stretch is specified instead
            self.m = n**s

            
    def __call__(self, k, x):
        """Evaluates the GAR instance on the given secret key/seed and public input.

        Args:
            k (int): the seed
            x (list): a subset of the key/seed indices. Its length must match that of the predicate used in this instance, i.e., `self.d`

        Returns:
             int: an integer in [0,1] corresponding to the evaluation of the predicate on a specific subset of the seed bits.
        
        """
        assert len(x) == self.d
        predicate_input = []
        for i in x: 
            predicate_input.append(k[i])
        return self.predicate(predicate_input)

    
    def prg(self, k, xs):
        """Uses GAR not as a weak PRF but as a PRG that can output multiple bits. Its total output size is specified at the construction using either a specific output size in bits, or a "stretch".

        Args:
            k (int): the master/key seed to start from
            xs (int): the public indices to use to generate the pseudo-random sequence

        Returns:
            int: an integer whose binary representation corresponds to the pseudo-random sequence
        """
        assert len(x) == self.m
        seed = k
        y = 0
        for i in range(0, self.m):
            y = (y << 1) | self(seed, x[i])
        return 

