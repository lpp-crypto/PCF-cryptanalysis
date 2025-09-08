from sage.all import *
from wsPRF import *


# parameters
# m is equal to 5N/t, and u to t/l
# -- sage, N=2**45, t=85, l=3ln(5N)=98.4
safe_ealpn = EALPN(
    2**41, # m
    99,    # l
    1      # u
)

# -- aggressive, N=2**45, t=660, l=11
aggressive_ealpn = EALPN(
    2**38, # m
    11,    # l
    60     # u
)
                   


if __name__ == "__main__":
    seed = b""
    prng = ReproducibleRangePRG(seed)
    sequence_length = 500
    # 128-bit secure
    instance = safe_ealpn
    # generating the key
    k = [
        [prng(0, instance.m) for t in range(0, instance.u)]
        for i in range(0, instance.l)
    ]
    # printing sequence
    seq = []
    for t in range(0, sequence_length):
        # generating the random input
        jx = [
            (
                prng(0, instance.u), # j
                prng(0, instance.m), # x
            )
            for i in range(0, instance.l)
        ]
        seq.append(instance(k, jx))
    print_sequence(seq)

    
