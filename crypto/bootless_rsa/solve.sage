from Crypto.Util.number import long_to_bytes
import json

with open('bootless_rsa.json', 'r') as enonce:
    challenge = json.loads(enonce.read())

N = Integer(challenge['N'])
ct = Integer(challenge['ct'])
e = Integer(challenge['e'])
print(N.nbits(), ct.nbits())

# Because the modulus is way bigger than the ciphertext, we can do an inverse root to get the plaintext

pt = ct**(1/e)
print(long_to_bytes(pt).decode())
