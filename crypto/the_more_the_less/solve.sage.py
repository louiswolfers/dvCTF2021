

# This file was *autogenerated* from the file solve.sage
from sage.all_cmdline import *   # import sage library

from Crypto.Util.number import long_to_bytes
import json

with open('supersecret.json', 'r') as enonce:
    challenge = json.loads(enonce.read())

N = challenge['N']
ct = challenge['ct']
e = challenge['e']
d = inverse_mod(e, euler_phi(N))
M = long_to_bytes(pow(ct, d, N))
print(M)

