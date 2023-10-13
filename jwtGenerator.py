from jwt import (
    JWT,
    jwk_from_dict,
    jwk_from_pem,
)
from config import *

#https://github.com/GehirnInc/python-jwt
#https://auth0.com/blog/how-to-handle-jwt-in-python/


# read and load the key
with open(pathToKey, 'rb') as fh:
    signing_key = jwk_from_pem(fh.read())

instance = JWT()
compact_jws = instance.encode(payload_data, signing_key, alg='RS256')

print(compact_jws)
print("validate token here: https://jwt.io/")
print("curl -H \"Authorization: Bearer " + compact_jws + "\" " + serviceUrl)