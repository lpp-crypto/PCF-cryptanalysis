#!/usr/bin/sage
#-*- Python -*-
# Time-stamp: <2024-06-24 10:40:18 leo>

from sage.all import *
from prg import ReproduciblePRG

# !TODO! implement GAR

#takes a list of integers corresponding to the variables that are taken to output the PRG and n and m parameters for the function: the first n bits are XORed the last is majority

def xormaj(L,a,b):
	assert len(L) == a + b
	res = 0
	for i in range(a):
		res += L[i]
	tmp = 0
	for j in range(a,a+b):
		tmp += L[i]
	if tmp >= b/2:
		res += 1
	return res%2

#need here to change parameters
def xormajfixed(L):
	return xormaj(L,10,64)

class GAR:
	"""An implementation of the GAR PRF. It uses the parameters: 

	N: the size of the secret key

	n: the number of elements taken by the predicate

	predicate: the predicate used (xormaj in original proposal), uses a list of given size

	key: an integer of value < 2^K

	"""

	def __init__(self, N = 256, n = 74, predicate = xormajfixed, seed = b"seed"):
		# initializing the variables 
		self.N = N
		self.n = n
		self.predicate = predicate
		self.prg = ReproduciblePRG(seed)
		self.k = self.prg(0,1<< self.N)

	def __call__(self):
		"""
		generate random numbers + output bit
		"""
		list = []
		while len(list) < self.n :
			e = self.prg(0,self.N)
			if e not in list:
				list.append((self.k >> e) & 1)
		return self.predicate(list)


# parameters
# !TODO! double check parameters 

proposalGAR = GAR()
row = ""
for t in range(0,100):
	row += "{:d} ".format(proposalGAR())
print(row)

