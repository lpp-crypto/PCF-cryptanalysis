#!/usr/bin/python3
#-*- Python -*-
# Time-stamp: <2025-06-01 21:55:49>


import hashlib
from collections import defaultdict
from math import ceil, log


class ReproducibleBytePRG:
    """A simple pseudo random number generator based on hashing an
    increasing counter using SHA256, the state of the hash function
    being initialized with the seed.

    Generates directly bytes, can be used directly, or can be used to
    build the higher level classes
    # !TODO! classes 

    """
    def __init__(self, seed):
        """We initialize the state of a SHA256 instance with the given
        seed. This is a deterministic procedure.

        If mode is BYTE_BASED, then 

        """
        self.state = hashlib.sha256()
        self.state.update(seed)
        self.counter = int(0)
        self.inner_state = []

    def __call__(self):
        """Outputs a single byte. If the internal state is empty, we
        increment the counter and reinitialize a SHA-256 digest.

        """
        if len(self.inner_state) == 0:
            self.counter += 1
            tmp = self.state.copy()
            tmp.update(self.counter.to_bytes(16, "little"))
            self.inner_state = list(tmp.digest())
        return self.inner_state.pop()

    
class ReproducibleRangePRG:
    """A reproducible PRG that outputs an integer in a specific range.

    It works by obtaining random bytes from an inner
    `ReproducibleBytePRG` instance, and building an integer of the
    correct bit length, and then rejecting it if it is above the
    wanted threshold (rejection sampling).

    """
    def __init__(self, seed):
        self.inner_prg = ReproducibleBytePRG(seed)
        
    def __call__(self, lower_bound, upper_bound):
        """Returns a pseudo random integer `d` such that lower_bound
        <= d < upper_bound (like `range`).

        """
        # setting up the computation
        normalized_upper_bound = upper_bound - lower_bound
        needed_bytes = ceil(log(normalized_upper_bound, 256))
        mask = 1
        while mask < normalized_upper_bound:
            mask = (mask << 1) | 1
        while True: # infinite loop because of rejection sampling
            # generating the a bit string
            alea = 0
            for i in range(0, needed_bytes):
                alea = (alea << 8) | self.inner_prg()
            # dropping unneeded bits of high weight
            alea = alea & mask
            if alea < normalized_upper_bound:
                return lower_bound + alea
        

class ReproducibleBitPRG:
    """A PRNG that returns a single bit at each call.

    It maintains a one byte state and extract one bit from it at each
    call. Every eight calls, it queries a new byte from an inner
    `ReproducibleBytePRG` instance.

    """
    def __init__(self, seed):
        self.inner_prg = ReproducibleBytePRG(seed)
        self.current_byte = self.inner_prg()
        self.extracted = 0

    def __call__(self):
        if self.extracted == 8:
            self.current_byte = self.inner_prg()
            self.extracted = 1
        else:
            self.extracted += 1
        result = self.current_byte & 1
        self.current_byte = self.current_byte >> 1
        return result
    

if __name__ == "__main__":
    print("Testing byte PRNG")
    for seed in [b"a", b"b", b"c", b"d", b"e", b"f"]:
        print("seed: {}".format(seed))
        prg = ReproducibleBytePRG(seed)
        counter = defaultdict(int)
        for i in range(1, 10000):
            counter[prg()] += 1
        for c in sorted(counter.keys()):
            print(c, counter[c])
            
    print("\nTesting bit PRNG")
    for seed in [b"a", b"b", b"c", b"d", b"e", b"f"]:
        print("seed: {}".format(seed))
        prg = ReproducibleBitPRG(seed)
        counter = defaultdict(int)
        for i in range(1, 10000):
            counter[prg()] += 1
        for c in sorted(counter.keys()):
            print(c, counter[c])
            
    print("\nTesting range PRNG")
    for seed in [b"a", b"b", b"c", b"d", b"e", b"f"]:
        print("seed: {}".format(seed))
        prg = ReproducibleRangePRG(seed)
        counter = 0
        counter = defaultdict(int)
        for i in range(1, 10000):
            counter[prg(2, 9)] += 1
        for c in sorted(counter.keys()):
            print(c, counter[c])


