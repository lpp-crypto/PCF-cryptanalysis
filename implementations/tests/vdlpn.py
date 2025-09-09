from sage.all import *
from wsPRF import *


# 128-bit secure variants
inst_1 = VDLPN(20, 293)
inst_2 = VDLPN(25, 336)
inst_3 = VDLPN(30, 380)
inst_4 = VDLPN(35, 421)
inst_5 = VDLPN(40, 461)

if __name__ == "__main__":
    seed = b""
    prng = ReproducibleBitPRG(seed)
    sequence_length = 500
    # 128-bit security
    d = 40
    w = 120
    # keygen
    k = [prng() for i in range(0, d*w*d)]
    vdlpn_instance = VDLPN(d, w)
    print_sequence([
        vdlpn_instance(k, [prng() for j in range(0, d*w*d)])
        for i in range(0, sequence_length)
    ])

    
