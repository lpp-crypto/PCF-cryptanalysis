"""This module contains reference implementations of four weak shallow PRFs.

For more information, check out the corresponding ToSC paper:

SoK: On Shallow Weak PRFs
A Common Symmetric Building Block for MPC Protocols
Christina Boura, Geoffroy Couteau, Léo Perrin, and Yann Rotella
Transactions on Symmetric Cryptology, 2025(3), To Appear.

"""

# Utilities needed to actually use the functions

from .Utils import *
from .Prg import *

# The four wsPRFs

from .Vdlpn import VDLPN
from .Ealpn import EALPN
from .Bipsw import BIPSW

### The Goldreich PRG needs so-called "predicates" to be specified, which we also import from the corresponding module
from .Gar import \
    GAR, \
    P_5, XOR_MAJ, Threshold 
