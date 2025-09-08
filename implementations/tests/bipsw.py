from sage.all import *
from wsPRF import *


if __name__ == "__main__":
    prng = ReproducibleRangePRG(b"")
    sequence_length = 500
    # 128-bit security
    n = 770 
    bipsw_instance = BIPSW(n)
    k = prng(0, 2**n)           # key is picked randomly
    print_sequence([
        bipsw_instance(k, prng(0, 2**n)) # we pick plaintexts in [0,2**n-1]
        for i in range(0, sequence_length)
    ])

