# Weak Shallow PRF Implementations


## Content of this folder

This folder contains our implementations of multiple weak shallow pseudo-random functions. These are implemented as classes, and they all provide an implementation of the `__call__` function that takes as input a key `k` and an input `x`, and returns a single bit (the output of the corresponding wsPRF). These are intended to be reference implementations of these functions, and we also provide various sets of parameters for each of them.

The expected structures of `x` and `k` are not identical due to the inner workings of these functions. In order to handle the unusual form they may take, we also implemented our pseudo-random generators that output different types of data, from single bits to subsets of an integer interval.


## Files

### Subroutines

* `utils.py` simply contains a function printing a binary sequence
* `prg.py` contains the pseudo-random generators needed to generate the keys and inputs of the various wsPRFs. Our implementations basically relies on hashing a counter with SHA-256. We provide various high level interfaces that greatly simplify the logic of the implementation of the wsPRFs.

### wsPRFS

Each wsPRF is implemented in its own file, and relies on the above modules. They also rely on `SAGE`: without this software, they are unusable. We have implemented the following:
* `BIPSW.sage`,
* `EALPN.sage`,
* `GAR.sage`, and
*  `VDLPN.sage`.
