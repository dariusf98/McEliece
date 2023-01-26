# Demo - Brute Force Public Key from Private Key
# 	Attempts to reconstitute a private key from a given Public Key based on H16,11 code.
#   Will need considerably more time than H8,4.
#
#   WARNING: Will take an obnoxious amount of time. This example serves solely as a proof of concept
#   of how long it would take to brute force a larger data set
from mc_core import *

tPriv = privateKeyH1611()
tPriv.printCode()

brute = bruteForcerH1611(tPriv.makeGPrime())
print("Attempting to Crack...")
brute.attemptKey()
brute.printCode()
print("Cracking Successful")
