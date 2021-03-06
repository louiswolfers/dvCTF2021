

# This file was *autogenerated* from the file create_challenge.sage
from sage.all_cmdline import *   # import sage library

_sage_const_2 = Integer(2); _sage_const_127 = Integer(127); _sage_const_129 = Integer(129); _sage_const_0x10001 = Integer(0x10001); _sage_const_16 = Integer(16)
import json
from sage.crypto.util import random_blum_prime

p = random_blum_prime(_sage_const_2 **_sage_const_127 , _sage_const_2 **_sage_const_129 )
q = random_blum_prime(_sage_const_2 **_sage_const_127 , _sage_const_2 **_sage_const_129 )

N = p*q

e = _sage_const_0x10001 

flag = b'dvCTF{rs4_f4ctor1z4t10n!!!}'
flag = int(flag.hex(), _sage_const_16 )

print(flag, Integer(flag).nbits())

ct = pow(flag, e, N)

challenge = {"N": int(N), "e": int(e), "ct": int(ct)}

print(challenge)

with open("weak_rsa.json", 'w') as output:
    output.write(json.dumps(challenge))

