#!/usr/bin/python3
#-*- Python -*-
# Time-stamp: <2024-06-24 11:55:40 leo>


import hashlib



class ReproduciblePRG:
    """A simple pseudo random number generator based on hashing an
    increasing counter using SHA256, the state of the hash function
    being initialized with the seed.

    """
    def __init__(self, seed):
        """We initialize the state of a SHA256 instance with the given
        seed. This is a deterministic procedure.

        """
        self.state = hashlib.sha256()
        self.state.update(seed)
        self.counter = int(0)
        
    def __call__(self,
                 lower_bound=0,
                 upper_bound=2**128):
        """We absorb the counter into the SHA256 state obtained after
        absorbing the seed, then turn the digest into an integer which
        we cast between the bounds.

        The output d is such that lower_bound <= d < upper_bound (like
        `range`).

        """
        self.counter += 1
        tmp = self.state.copy()
        tmp.update(self.counter.to_bytes(16, "little"))
        digest = tmp.digest()
        digest_as_int = 0
        for b in digest:
            digest_as_int = (digest_as_int << 8) | int(b)
        return lower_bound + (digest_as_int % (upper_bound - lower_bound))
        



if __name__ == "__main__":
    prg = ReproduciblePRG(b"blabli")
    for i in range(1, 100):
        print([
            prg(lower_bound=0, upper_bound=i)
            for j in range(0, 10)
        ])
