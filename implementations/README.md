# Weak Shallow PRF Implementations


## Content of this folder

This folder contains our implementations of multiple weak shallow pseudo-random functions. These are implemented as classes, and they all provide an implementation of the `__call__` function that takes as input a key `k` and an input `x`, and returns a single bit (the output of the corresponding wsPRF). These are intended to be reference implementations of these functions. These implementations are in the folder [wsPRF](./wsPRF).

The expected structures of `x` and `k` are not identical due to the inner workings of these functions. In order to handle the unusual form they may take, we also implemented our pseudo-random generators that output different types of data, from single bits to subsets of an integer interval.


To see how to use each wsPRF, we also provide various sets of parameters for each of them in the [tests](./tests) folder, along with examples of how to setup each of them.

## Installation

You can `cd` to the directory containing this README file and then run the following command to install this module in your SAGE installation.

``` shell
sage -pip install .
```



## Files

### Subroutines

* [Utils.py](./wsPRF/Utils.py) simply contains a function printing a binary sequence
* [Prg.py](./wsPRF/Prg.py) contains the pseudo-random generators needed to generate the keys and inputs of the various wsPRFs. Our implementations basically relies on hashing a counter with SHA-256. We provide various high level interfaces that greatly simplify the logic of the implementation of the wsPRFs.

### wsPRFS

Each wsPRF is implemented in its own file, and relies on the above modules. Several also rely on `SAGE`, which is why consider this project to be a `SAGE` module. At this stage (v1.0), we have implemented the following:
* [BIPSW](./wsPRF/Bipsw.py),
* [EALPN](./wsPRF/Ealpn.py),
* [GAR](./wsPRF/Gar.py), and
* [VDLPN](./wsPRF/Vdlpn.py).
