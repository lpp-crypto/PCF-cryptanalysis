from sage.all import *
from wsPRF import *


# parameters of 128-bit secure versions
# =====================================

inst_1 = GAR(1024, P_5(), s=1.02)
inst_2 = GAR(2048, P_5(), s=1.10)
inst_3 = GAR(4096, P_5(), s=1.19)
inst_4 = GAR(8192, P_5(), s=1.19)

inst_5 = GAR(1024, XOR_MAJ( 4,  7), s=2)
inst_6 = GAR( 512, XOR_MAJ(10, 64), s=4.5)
inst_7 = GAR( 894, XOR_MAJ(10, 64), s=3.4)
inst_8 = GAR(2048, XOR_MAJ(10, 64), s=3)


# tests
# =====


if __name__ == "__main__":
    seed = b""
    prng_k = ReproducibleBitPRG(seed)
    prng_x = ReproducibleSubsetPRG(seed + b"1")
    sequence_length = 500
    # 128-bit security
    gar_instance = inst_1
    # keygen
    k = [prng_k() for i in range(0, gar_instance.n)]
    seq = []
    # generating sequence
    print_sequence([
        gar_instance(k, prng_x(0, gar_instance.n, gar_instance.d))
        for i in range(0, sequence_length)
    ])




