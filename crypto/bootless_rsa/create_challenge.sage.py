

# This file was *autogenerated* from the file create_challenge.sage
from sage.all_cmdline import *   # import sage library

_sage_const_0 = Integer(0); _sage_const_1024 = Integer(1024); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_3 = Integer(3); _sage_const_16 = Integer(16)
import json

def generate_RSA_key_pair(N):
    n = _sage_const_0 
    p = _sage_const_0 
    q = _sage_const_0 
    """Repeat until n has length N because multiplying two numbers of length N/2 can result in n of length N-1"""
    while n.nbits() != _sage_const_1024 :
        p = random_prime(_sage_const_2 **(N//_sage_const_2 ), lbound = _sage_const_2 **(N//_sage_const_2  -_sage_const_1 ))
        q = random_prime(_sage_const_2 **(N//_sage_const_2 ), lbound = _sage_const_2 **(N//_sage_const_2  -_sage_const_1 ))
        n = p*q
    return n

N = generate_RSA_key_pair(_sage_const_1024 )
e = _sage_const_3 

flag = b'dvCTF{RS4_m0dul0_inf1nity}'
flag = int(flag.hex(), _sage_const_16 )

ct = power_mod(flag, e, N)

challenge = {"N": int(N), "e": int(e), "ct": int(ct)}

print(challenge)

with open("supersecret.json", 'w') as output:
    output.write(json.dumps(challenge))

