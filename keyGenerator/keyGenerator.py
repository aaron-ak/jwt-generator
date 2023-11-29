# Python script to create JWKS public and private keys.
import os
import subprocess
from jwcrypto import jwk
from keyGeneratorConfig import *


key_type = "RSA"
alg = "RSA256"
size = 2048
use = "sig"


def create_keys(key_name):
    """Create all of the keys and save in keys directory"""
    key = jwk.JWK.generate(kty=key_type, size=size, kid=key_name, use=use, alg=alg)

    with open(f"{key_path}/{key_name}_private.json", "w") as writer:
        writer.write(key.export_private())

    with open(f"{key_path}/{key_name}_public.json", "w") as writer:
        writer.write(key.export_public())

    with open(f"{key_path}/{key_name}.pem", "w") as writer:
        writer.write(key.export_to_pem("private_key", password=None).decode("utf-8"))
        
    with open(f"{key_path}/{key_name}_public.pem", "w") as writer:
        writer.write(key.export_to_pem().decode("utf-8"))

    # generate JWKS
    jwks = '{"keys": [' + key.export_public() + ']}'

    with open(f"{key_path}/{key_name}.jwks", "w") as writer:
        writer.write('{"keys": [' + key.export_public() + ']}')

    # Output private key to RSA format for Terraform using openssl
    args = [
        "openssl",
        "rsa",
        "-in",
        f"{key_path}/{key_name}.pem",
        "-out",
        f"{key_path}/{key_name}_rsa.pem",
    ]
    subprocess.run(args)


if not os.path.exists(key_path):
    os.makedirs(key_path)
    create_keys(key_name=key_name)
    print("Keys created: " + key_path)
else:
    print("Please remove existing keys-directory: " + key_path)